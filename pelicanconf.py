#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import yaml

AUTHOR = u'Jason K. Moore'
SITENAME = u'MAE/BIM 223: Multibody Dynamics'
SITEURL = ''

PATH = 'content'
THEME = 'theme'
PAGE_ORDER_BY = 'sortorder'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# This sets the default pages to be top level items.
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_ORDER_BY = 'sortorder'

STATIC_PATHS = ['lecture-notes', 'lecture-notebooks']
IGNORE_FILES = ['README*']

DEFAULT_PAGINATION = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

try:
    with open('local-config.yml', 'r') as config_file:
        config_data = yaml.load(config_file)
except IOError:
    THEME = ''
    PLUGIN_PATHS = ''
else:
    THEME = config_data['THEME_PATH']
    PLUGIN_PATHS = config_data['PLUGIN_PATHS']

## THEME

# Alchemy theme settings
SITESUBTITLE = ''
SITEIMAGE = ''
DESCRIPTION = ''
PYGMENTS_STYLE = 'emacs'

## PLUGINS

PLUGINS = ['render_math', 'code_include']
