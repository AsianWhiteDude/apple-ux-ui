"""Offline behavioral tests using synthetic DocC content and mocked transports."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch
from urllib.error import URLError


SCRIPT = Path(__file__).resolve().parents[1] / 'skills/apple-ux-ui/scripts/hig.py'
SPEC = importlib.util.spec_from_file_location('hig', SCRIPT)
hig = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(hig)


def paragraph(text):
    return {'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': text}]}


def page(title='Synthetic guide'):
    return {'metadata': {'title': title}, 'primaryContentSections': [
        {'content': [paragraph('A synthetic example, independent of Apple content.')]}]}


class FetchTests(unittest.TestCase):
    def test_python_success_needs_no_curl(self):
        expected = page()
        with patch.object(hig.urllib.request, 'urlopen', return_value=io.BytesIO(json.dumps(expected).encode())) as request, \
                patch.object(hig.subprocess, 'run') as curl:
            self.assertEqual(hig.fetch('/feedback/'), expected)
        self.assertEqual(request.call_args.args[0].full_url, hig.BASE_JSON + 'feedback.json')
        self.assertEqual(request.call_args.kwargs['timeout'], 30)
        curl.assert_not_called()

    def test_network_failure_uses_bounded_checked_curl(self):
        expected = page()
        with patch.object(hig.urllib.request, 'urlopen', side_effect=URLError('TLS failed')), \
                patch.object(hig.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, json.dumps(expected), '')) as curl:
            self.assertEqual(hig.fetch('feedback'), expected)
        command = curl.call_args.args[0]
        self.assertIn('--fail', command)
        self.assertIn('--max-time', command)
        self.assertNotIn('--insecure', command)
        self.assertTrue(curl.call_args.kwargs['check'])
        self.assertEqual(command[-1], hig.BASE_JSON + 'feedback.json')

    def test_invalid_python_json_can_recover_with_curl(self):
        with patch.object(hig.urllib.request, 'urlopen', return_value=io.BytesIO(b'<html>Proxy</html>')), \
                patch.object(hig.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, json.dumps(page()), '')):
            self.assertEqual(hig.fetch('feedback'), page())

    def test_curl_failures_are_actionable(self):
        cases = [
            (FileNotFoundError(), 'curl is not installed'),
            (subprocess.TimeoutExpired('curl', 65), 'curl timed out'),
            (subprocess.CalledProcessError(22, 'curl', stderr='HTTP 404'), 'curl exited 22: HTTP 404'),
        ]
        for failure, message in cases:
            with self.subTest(message=message), \
                    patch.object(hig.urllib.request, 'urlopen', side_effect=URLError('network unavailable')), \
                    patch.object(hig.subprocess, 'run', side_effect=failure):
                with self.assertRaises(hig.FetchError) as caught:
                    hig.fetch('feedback')
                self.assertIn('network unavailable', str(caught.exception))
                self.assertIn(message, str(caught.exception))

    def test_malformed_fallback_is_not_rendered_as_a_page(self):
        for body in ('not JSON', '[]', 'null'):
            with self.subTest(body=body), \
                    patch.object(hig.urllib.request, 'urlopen', side_effect=URLError('offline')), \
                    patch.object(hig.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, body, '')):
                with self.assertRaisesRegex(hig.FetchError, 'no usable page'):
                    hig.fetch('feedback')

    def test_invalid_slug_never_reaches_network(self):
        for slug in ('../feedback', 'https://example.org', 'feedback?x=1', ''):
            with self.subTest(slug=slug), patch.object(hig.urllib.request, 'urlopen') as request:
                with self.assertRaises(ValueError):
                    hig.fetch(slug)
                request.assert_not_called()


class RenderingTests(unittest.TestCase):
    def test_inline_styles_and_reference_urls(self):
        refs = {'guide': {'title': 'Related guide', 'url': '/design/related'}}
        rendered = hig.inl([
            {'type': 'strong', 'inlineContent': [{'type': 'text', 'text': 'Save'}]},
            {'type': 'text', 'text': ' with '},
            {'type': 'codeVoice', 'code': 'Enter'},
            {'type': 'text', 'text': '; see '},
            {'type': 'reference', 'identifier': 'guide'},
        ], refs)
        self.assertEqual(rendered, '**Save** with `Enter`; see [Related guide](https://developer.apple.com/design/related)')

    def test_markdown_includes_source_nested_blocks_and_topics(self):
        document = page()
        document['references'] = {'next': {'title': 'Next guide', 'url': '/design/next'}}
        document['primaryContentSections'][0]['content'] = [
            {'type': 'heading', 'level': 2, 'text': 'Example'},
            {'type': 'row', 'columns': [{'content': [paragraph('Column text')]}]},
            {'type': 'orderedList', 'items': [{'content': [paragraph('First')]}, {'content': [paragraph('Second')]}]},
            {'type': 'aside', 'name': 'Note', 'content': [paragraph('Check the result.')]},
            {'type': 'table', 'rows': [[[paragraph('Label')], [paragraph('Value')]], [[paragraph('A')], [paragraph('B')]]]},
            {'type': 'codeListing', 'code': ['example()']},
        ]
        document['topicSections'] = [{'title': 'Continue', 'identifiers': ['next']}]
        output = hig.to_md(document, 'feedback')
        for expected in (
            '# Synthetic guide', 'Source: ' + hig.BASE_HTML + 'feedback',
            '## Example', 'Column text', '1. First\n2. Second',
            '> **Note.** Check the result.', '| Label | Value |\n|---|---|\n| A | B |',
            '```\nexample()\n```', '## Continue', '[Next guide](https://developer.apple.com/design/next)',
        ):
            self.assertIn(expected, output)

    def test_components_expand_their_groups(self):
        document = {'topicSections': [{'identifiers': ['doc://buttons']}], 'references': {}}
        with patch.object(hig, 'fetch', return_value=document), \
                patch.object(hig, 'list_group', return_value=['push-buttons  Description']) as group, \
                contextlib.redirect_stdout(io.StringIO()) as output:
            hig.list_section('components')
        group.assert_called_once_with('buttons')
        self.assertIn('    push-buttons  Description', output.getvalue())


class CliTests(unittest.TestCase):
    def test_closed_output_pipe_exits_without_a_traceback(self):
        code = (
            'import io, json, runpy, sys, urllib.request\n'
            f'payload = {page()!r}\n'
            'urllib.request.urlopen = lambda *a, **kw: io.BytesIO(json.dumps(payload).encode())\n'
            f'sys.argv = [{str(SCRIPT)!r}, "feedback"]\n'
            f'runpy.run_path({str(SCRIPT)!r}, run_name="__main__")\n'
        )
        with subprocess.Popen([sys.executable, '-B', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
            process.stdout.close()
            process.stdout = None
            _, errors = process.communicate(timeout=10)
        self.assertEqual(process.returncode, 0, errors)
        self.assertEqual(errors, '')

    def test_no_arguments_prints_help_without_network(self):
        with patch.object(hig, 'fetch') as fetch, contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(hig.main([]), 0)
        self.assertIn('--list', output.getvalue())
        fetch.assert_not_called()

    def test_invalid_arguments_fail_before_network(self):
        for args in (['--unknown'], ['--list', 'feedback'], ['../feedback']):
            with self.subTest(args=args), patch.object(hig, 'fetch') as fetch, \
                    contextlib.redirect_stderr(io.StringIO()) as errors:
                with self.assertRaises(SystemExit) as caught:
                    hig.main(args)
                self.assertEqual(caught.exception.code, 2)
                self.assertNotIn('Traceback', errors.getvalue())
                fetch.assert_not_called()

    def test_page_failure_does_not_discard_following_success(self):
        with patch.object(hig, 'fetch', side_effect=[hig.FetchError('HTTP 404'), page()]), \
                contextlib.redirect_stdout(io.StringIO()) as output, \
                contextlib.redirect_stderr(io.StringIO()) as errors:
            self.assertEqual(hig.main(['missing', 'feedback']), 1)
        self.assertIn('ERROR missing: HTTP 404', errors.getvalue())
        self.assertIn('# Synthetic guide', output.getvalue())

    def test_list_failure_is_reported_without_traceback(self):
        with patch.object(hig, 'list_section', side_effect=hig.FetchError('offline')), \
                contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()) as errors:
            self.assertEqual(hig.main(['--list', 'foundations']), 1)
        self.assertEqual(errors.getvalue(), 'ERROR foundations: offline\n')


if __name__ == '__main__':
    unittest.main()
