#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

if 'TRAVIS_TAG' in os.environ and os.environ.get('TRAVIS_TAG') is not '':
    TAG_DIR = '/' + os.environ.get('TRAVIS_TAG')
else:
    TAG_DIR = ''

SITEURL = 'https://moorepants.github.io/mae223{}'.format(TAG_DIR)
RELATIVE_URLS = False

FEED_ATOM = None
FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-15966419-8"
