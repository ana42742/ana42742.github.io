#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ananya Srivastava'
SITENAME = 'Virtual View'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'


# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'post_stats', 'feed_summary']

# Flex theme stuff
THEME = 'themes/Flex'

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# DISQUS
DISQUS_SITENAME = 'ana42742'

### Flex configurations

PLUGINS = ['sitemap', 'post_stats', 'feed_summary']
SITEURL = 'http://localhost:8000'
SITETITLE = 'Virtual View'  
SITESUBTITLE = 'Ideas and Thoughts'
SITELOGO = '/images/profile.JPG'
FAVICON = '/images/icons/favicon.png'

# Sitemap Settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# Add a link to your social media accounts
SOCIAL = (
    ('github', 'https://github.com/ana42742'),
    ('envelope', 'mailto:rebellajoy@gmail.com'),
    ('linkedin','https://www.linkedin.com/in/ananya-srivastava-9336b4220/'),
)

STATIC_PATHS = ['images', 'extra']

# Main Menu Items
MAIN_MENU = True
MENUITEMS = (('Archives', '/archives'),('Categories', '/categories'),('Tags', '/tags'))

# Code highlighting the theme
PYGMENTS_STYLE = 'friendly'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# HOME_HIDE_TAGS = True
FEED_USE_SUMMARY = True