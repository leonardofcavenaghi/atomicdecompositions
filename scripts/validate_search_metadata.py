#!/usr/bin/env python3
"""Check the built site's sitemap, canonical URLs, and search metadata."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET

BASE = 'https://leonardofcavenaghi.github.io/atomicdecompositions/'


class Head(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonicals = []
        self.description = ''
        self.robots = ''

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonicals.append(attrs.get('href'))
        if tag == 'meta' and attrs.get('name') == 'description':
            self.description = attrs.get('content', '')
        if tag == 'meta' and attrs.get('name') == 'robots':
            self.robots = attrs.get('content', '')


def validate(directory):
    sitemap = ET.parse(directory / 'sitemap.xml')
    urls = [element.text for element in sitemap.findall('.//{*}loc')]
    assert urls and len(urls) == len(set(urls)), 'Empty or duplicated sitemap URLs'
    assert BASE in urls, 'Home page absent from sitemap'
    for url in urls:
        assert url.startswith(BASE), f'Wrong sitemap origin: {url}'
        assert 'peskine' not in url.lower(), 'Withdrawn example in sitemap'
        relative = url[len(BASE):]
        path = directory / relative / 'index.html' if url.endswith('/') else directory / relative
        parser = Head()
        parser.feed(path.read_text())
        assert parser.canonicals == [url], f'Canonical mismatch: {url}'
        assert parser.description.strip(), f'Missing description: {url}'
        assert 'noindex' not in parser.robots.lower(), f'Unexpected noindex: {url}'
    robots = (directory / 'robots.txt').read_text()
    assert 'Disallow: /' not in robots, 'Project robots.txt denies crawling'
    assert f'Sitemap: {BASE}sitemap.xml' in robots, 'Missing sitemap instruction'
    assert not (directory / 'peskine').exists(), 'Withdrawn example still built'
    print(f'Search metadata validation passed: {len(urls)} canonical pages')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site-dir', type=Path, default=Path('site'))
    validate(parser.parse_args().site_dir)
