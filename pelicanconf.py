#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
from os.path import join, expanduser

AUTHOR = u'Jason K. Moore'
SITENAME = u'MAE 223: Multibody Dynamics'
SITEURL = ''

PATH = 'content'
THEME = 'theme'
PAGE_ORDER_BY = 'sortorder'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

TEMPLATE_PAGES = {'projects.html': 'projects.html'}

STATIC_PATHS = ['lecture-notes', 'lecture-notebooks']

# NOTE: The order here is important. The last item is the first to be searched
# it seems.
if "TRAVIS" in os.environ:
    PLUGIN_PATHS = ['pelican-plugins', "plugins"]
else:
    PLUGIN_PATHS = [join(expanduser("~"), 'src', 'pelican-plugins'), "plugins"]
print(PLUGIN_PATHS)
PLUGINS = ['neighbors', 'render_math', 'headerid', 'jinja2content']

# headerid options
HEADERID_LINK_CHAR = "¶"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

IGNORE_FILES = ['README*']
