#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Robbo'
SITENAME = 'Robert Clancy'
SITEURL = 'http://localhost:8000'

PATH = 'content'
PATH_METADATA = '(?P<date>\d{4}-\d{2}-\d{2}).*'
DIRECT_TEMPLATES = ('index', 'tags', 'archives')
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
TAG_URL = 'blog/{slug}'
TAG_SAVE_AS = TAG_URL + '/index.html'
TAGS_URL = ''
TAGS_SAVE_AS = ''
PAGE_URL = '{slug}'
PAGE_SAVE_AS = PAGE_URL + '/index.html'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = ARTICLE_URL + '/index.html'
STATIC_PATHS = ['images']
SLUGIFY_SOURCE = 'basename'

PLUGIN_PATHS = ['plugins', 'plugins/pelican-plugins']
PLUGINS = ['assets']

THEME = 'themes/dragon'
THEME_STATIC_DIR = 'assets'
THEME_STATIC_PATHS = ['static']
ASSET_SOURCE_PATHS = ['assets']
DEFAULT_DATE_FORMAT = ('%B %d, %Y')
INDEX_SAVE_AS = 'blog/index.html'
TEMPLATE_PAGES = {'home.html': 'index.html'}
DISQUS_SITENAME = 'robbo'

YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/index.html'

YEAR = date.today().year

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'

def sortTags(tags):
    return sorted(tags, key=lambda k: len(k[1]), reverse=True)

JINJA_FILTERS = {
    'sortTags': sortTags
}

FEED_ATOM = 'blog/feeds/atom.xml'
FEED_RSS = 'blog/feeds/rss.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CACHE_CONTENT = False

DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page-{number}/', '{base_name}/page-{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
