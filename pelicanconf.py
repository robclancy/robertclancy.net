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
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PLUGIN_PATHS = ['plugins', 'plugins/pelican-plugins']
PLUGINS = ['assets']

THEME = 'themes/dragon'
THEME_STATIC_DIR = 'assets'
THEME_STATIC_PATHS = ['static']
ASSET_SOURCE_PATHS = ['assets']
PAGINATED_DIRECT_TEMPLATES = ()

YEAR = date.today().year

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
