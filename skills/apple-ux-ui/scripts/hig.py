#!/usr/bin/env python3
"""Fetch a live Apple Human Interface Guidelines page and print it as Markdown.

Usage:
  python3 hig.py <slug> [<slug> ...]      print one or more HIG pages as Markdown
  python3 hig.py --list [<section>]       list page slugs; sections: getting-started,
                                          foundations, patterns, components, inputs, technologies
Slug = the last path segment of the page URL, e.g. `feedback` for
https://developer.apple.com/design/human-interface-guidelines/feedback

Reads Apple's DocC JSON behind developer.apple.com; no third-party dependencies.
Pipe through `head` or save to a file; a page is typically 500–10 000 words.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request

BASE_JSON = "https://developer.apple.com/tutorials/data/design/human-interface-guidelines/"
BASE_HTML = "https://developer.apple.com/design/human-interface-guidelines/"


class FetchError(RuntimeError):
    """A page could not be retrieved as a DocC JSON object."""


def normalize_slug(slug):
    slug = slug.strip('/')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
        raise ValueError(f"invalid page slug: {slug!r}; use the final URL segment, e.g. feedback")
    return slug


def page_object(value):
    if not isinstance(value, dict):
        raise ValueError("expected a DocC JSON object")
    return value


def fetch(slug):
    slug = normalize_slug(slug)
    url = BASE_JSON + slug + ".json"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return page_object(json.load(r))
    except (OSError, ValueError) as exc:
        python_error = str(exc)
    # curl can use a different certificate store when Python's TLS setup fails.
    # Keep certificate verification enabled and reject HTTP errors before parsing.
    try:
        response = subprocess.run(
            ["curl", "--fail", "--silent", "--show-error", "--location",
             "--connect-timeout", "15", "--max-time", "60",
             "-A", "Mozilla/5.0", url],
            capture_output=True, text=True, encoding="utf-8", timeout=65, check=True,
        )
        return page_object(json.loads(response.stdout))
    except FileNotFoundError:
        fallback_error = "curl is not installed"
    except subprocess.TimeoutExpired:
        fallback_error = "curl timed out"
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or "").strip()[:500]
        fallback_error = f"curl exited {exc.returncode}" + (f": {detail}" if detail else "")
    except (OSError, ValueError) as exc:
        fallback_error = f"curl returned no usable page: {exc}"
    raise FetchError(f"Python request failed: {python_error}; {fallback_error}")

def inl(items, refs):
    s = ''
    for i in items or []:
        t = i.get('type')
        if t == 'text': s += i.get('text', '')
        elif t == 'strong': s += '**' + inl(i.get('inlineContent'), refs) + '**'
        elif t == 'emphasis': s += '*' + inl(i.get('inlineContent'), refs) + '*'
        elif t == 'codeVoice': s += '`' + i.get('code', '') + '`'
        elif t == 'reference':
            r = refs.get(i.get('identifier', ''), {})
            title = r.get('title') or i.get('identifier', '').split('/')[-1]
            u = r.get('url', '')
            if u.startswith('/'): u = 'https://developer.apple.com' + u
            s += f'[{title}]({u})' if u else title
        elif t == 'image': s += ''
        elif t == 'newTerm': s += inl(i.get('inlineContent'), refs)
        elif t == 'inlineHead': s += '**' + inl(i.get('inlineContent'), refs) + '**'
        else: s += inl(i.get('inlineContent'), refs)
    return s

def walk(blocks, refs, out, depth=0):
    for b in blocks or []:
        t = b.get('type')
        if t == 'heading':
            out.append('\n' + '#' * min(6, b.get('level', 2)) + ' ' + b.get('text', ''))
        elif t == 'paragraph':
            txt = inl(b.get('inlineContent'), refs).strip()
            if txt: out.append(txt)
        elif t == 'row':
            for c in b.get('columns', []): walk(c.get('content'), refs, out, depth + 1)
        elif t in ('unorderedList', 'orderedList'):
            for n, it in enumerate(b.get('items', []), 1):
                sub = []; walk(it.get('content'), refs, sub, depth + 1)
                bullet = f'{n}.' if t == 'orderedList' else '-'
                out.append(bullet + ' ' + ' '.join(x.strip() for x in sub if x.strip()))
        elif t == 'aside':
            sub = []; walk(b.get('content'), refs, sub, depth + 1)
            out.append('> **' + (b.get('name') or b.get('style', 'Note')) + '.** ' + ' '.join(x.strip() for x in sub))
        elif t == 'termList':
            for it in b.get('items', []):
                sub = []; walk(it.get('definition', {}).get('content'), refs, sub, depth + 1)
                out.append('- **' + inl(it.get('term', {}).get('inlineContent'), refs) + '** — ' + ' '.join(x.strip() for x in sub))
        elif t == 'table':
            rows = b.get('rows', [])
            for ri, row in enumerate(rows):
                cells = []
                for cell in row:
                    sub = []; walk(cell, refs, sub, depth + 1)
                    cells.append(' '.join(x.strip() for x in sub).replace('|', '/'))
                out.append('| ' + ' | '.join(cells) + ' |')
                if ri == 0: out.append('|' + '---|' * len(cells))
        elif t == 'links':
            for i in b.get('items', []):
                r = refs.get(i, {})
                u = r.get('url', '')
                if u.startswith('/'): u = 'https://developer.apple.com' + u
                out.append(f"- [{r.get('title', i.split('/')[-1])}]({u}) — {inl(r.get('abstract'), refs)}")
        elif t == 'tabNavigator':
            for tab in b.get('tabs', []):
                out.append('\n**Tab: ' + tab.get('title', '') + '**')
                walk(tab.get('content'), refs, out, depth + 1)
        elif t == 'codeListing':
            out.append('```\n' + '\n'.join(b.get('code', [])) + '\n```')
        elif t == 'small':
            walk(b.get('inlineContent') and [{'type': 'paragraph', 'inlineContent': b['inlineContent']}], refs, out, depth + 1)
        else:
            for k in ('content', 'items', 'columns', 'tabs'):
                if isinstance(b.get(k), list): walk(b[k], refs, out, depth + 1)

def to_md(d, slug):
    refs = d.get('references', {})
    title = d.get('metadata', {}).get('title', slug)
    out = [f'# {title}', f'Source: {BASE_HTML}{slug}', '', inl(d.get('abstract'), refs)]
    for s in d.get('primaryContentSections', []):
        walk(s.get('content'), refs, out)
    for s in d.get('topicSections', []):
        out.append('\n## ' + (s.get('title') or 'Topics'))
        for i in s.get('identifiers', []):
            r = refs.get(i, {})
            u = r.get('url', '')
            if u.startswith('/'): u = 'https://developer.apple.com' + u
            out.append(f"- [{r.get('title', i.split('/')[-1])}]({u}) — {inl(r.get('abstract'), refs)}")
    return '\n'.join(out).strip() + '\n'

SECTIONS = ['getting-started', 'foundations', 'patterns', 'components', 'inputs', 'technologies']

def list_section(section):
    d = fetch(section)
    refs = d.get('references', {})
    for s in d.get('topicSections', []):
        for i in s.get('identifiers', []):
            slug = i.split('/')[-1]
            r = refs.get(i, {})
            print(f"{slug:36} {inl(r.get('abstract'), refs)[:110]}")
            if section == 'components':
                for line in list_group(slug): print('    ' + line)

def list_group(slug):
    d = fetch(slug)
    refs = d.get('references', {})
    out = []
    for s in d.get('topicSections', []):
        for i in s.get('identifiers', []):
            r = refs.get(i, {})
            out.append(f"{i.split('/')[-1]:32} {inl(r.get('abstract'), refs)[:100]}")
    return out

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--list', action='store_true', help='list page slugs in the given sections (all if omitted)')
    parser.add_argument('slugs', nargs='*', help='page slugs, or section names with --list')
    args = parser.parse_args(argv)
    if not args.list and not args.slugs:
        parser.print_help()
        return 0
    try:
        slugs = [normalize_slug(slug) for slug in args.slugs]
    except ValueError as exc:
        parser.error(str(exc))
    if args.list and any(slug not in SECTIONS for slug in slugs):
        parser.error('--list sections must be: ' + ', '.join(SECTIONS))
    status = 0
    for slug in (slugs or SECTIONS):
        try:
            if args.list:
                print(f'## {slug}')
                list_section(slug)
                print()
            else:
                print(to_md(fetch(slug), slug))
        except FetchError as e:
            print(f'ERROR {slug}: {e}', file=sys.stderr); status = 1
    return status


if __name__ == '__main__':
    try:
        status = main()
        sys.stdout.flush()
        sys.exit(status)
    except BrokenPipeError:
        # A reader such as `head` may close the pipe before the whole page is printed.
        with open(os.devnull, 'w') as sink:
            os.dup2(sink.fileno(), sys.stdout.fileno())
        sys.exit(0)
