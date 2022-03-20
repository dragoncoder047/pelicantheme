#! /usr/bin/env python3
import base64
import zlib
import pymdownx.superfences

PORT = 8080
BIND = '192.168.1.158'
SITEURL = f'http://{BIND}:{PORT}'

AUTHOR = 'dragoncoder047'
THEME_MAIN_CSS = '/static/css/main.css'
THEME_STATIC_DIR = 'static/'

PATH = 'aaaa/'
OUTPUT_PATH = './'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en_US'

# maybe later...
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SEO_REPORT = True

DISPLAY_PAGES_ON_MENU = DISPLAY_CATEGORIES_ON_MENU = False

# Blogroll
LINKS = (
    ('Conwaylife', 'https://www.conwaylife.com/'),
    ('Python', 'https://www.python.org/'),
)

# Social
SOCIAL = (
    (f'{AUTHOR} on GitHub', f'https://github.com/{AUTHOR}'),
)

MENUITEMS = (
    #('Archives', f'/archives.html'),
    ('Projects', '#', (
        ('Phoo', f'https://github.com/{AUTHOR}/phoo'),
        ('Thuepaste', f'https://{AUTHOR}.github.io/thuepaste')
    )),
)

DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 3
PAGINATION_PATTERNS = (
    (1, '{name}{extension}', '{name}{extension}'),
    (2, '{name}_{number}{extension}', '{name}_{number}{extension}'),
)

THEME = './pelicantheme'

RELATIVE_URLS = False

READERS = {'html': None}


def lv_fence(source, language, css_class, options, md, **kwargs):
    return f'<div class="lifeviewer"><textarea>{source}</textarea><canvas height="{options.get("height", 400)}" width="{options.get("width", 600)}"></canvas></div>'


def kroki_fence(source, language, css_class, options, md, **kwargs):
    data = base64.urlsafe_b64encode(zlib.compress(
        source.encode('utf-8'), 9)).decode('ascii')
    lang = options.get('type', options.get('name', 'svgbob'))
    attr = ''
    if 'width' in options and 'height' in options:
        attr = f' width="{options["width"]}" height="{options["height"]}"'
    return f'<img src="https://kroki.io/{lang}/svg/{data}"{attr} />'


def circuit_fence(source, language, css_class, options, md, **kwargs):
    return '<span style="color: red; background: yellow;">TODO</span>'


MARKDOWN = {
    'extension_configs': {
        'meta': {},
        'pymdownx.extra': {},
        'pymdownx.caret': {},
        'pymdownx.details': {},
        'pymdownx.highlight': {
            'use_pygments': False,  # I use Prism.js
        },
        'pymdownx.inlinehilite': {},
        "pymdownx.superfences": {
            "custom_fences": [
                {
                    'name': 'mermaid',
                    'class': 'mermaid',
                    'format': pymdownx.superfences.fence_div_format
                },  # covered by kroki, but needed for compatibility with github
                {
                    'name': 'lifeviewer',
                    'class': 'lifeviewer',
                    'format': lv_fence
                },
                {
                    'name': 'kroki',
                    'class': 'kroki',
                    'format': kroki_fence
                }
            ]
        },
        'pymdownx.saneheaders': {},
        'pymdownx.magiclink': {},
        'pymdownx.smartsymbols': {},
        'smarty': {},
        'pymdownx.tabbed': {},
        'pymdownx.tasklist': {},
        'pymdownx.tilde': {},
        'sane_lists': {},
        'admonition': {},
        'abbr': {},
        'def_list': {},
        'toc': {},
        'footnotes': {},
        'attr_list': {},
        'markdown_figcap': {},
        'python_markdown_comments:CommentsExtension': {},
    },
    'output_format': 'html5',
}

PLUGINS = [
    # 'seo',
    'pelican.plugins.share_post',
    # 'sitemap',
    'pelican.plugins.related_posts',
    'minchin.pelican.plugins.nojekyll',
    'pelican.plugins.read_more',
    'jinja2content',
    'series',
    'pelican.plugins.more_categories'
]

if __name__ == '__main__':
    import os
    os.system(f'pelican {PATH} -o {OUTPUT_PATH} -s {__file__}')
