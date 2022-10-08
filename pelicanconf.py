AUTHOR = 'Rhys Deimel'
SITENAME = 'Rage Driven Development'
SITEURL = 'https://www.ragedriven.dev'
THEME = "theme"

PATH = 'content'
STATIC_PATHS = ['images', 'extra/',]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extra/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extra/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'extra/site.webmanifest': {'path': 'site.webmanifest'},
    'extra/tile.png': {'path': 'tile.png'},
    'extra/tile-wife.png': {'path': 'tile-wife.png'},
    'extra/humans.txt': {'path': 'humans.txt'},
    'extra/robots.txt': {'path': 'robots.txt'}
}

MARKDOWN = {
    "extension_configs": {
        # Needed for code syntax highlighting
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        # This is for enabling the TOC generation
        "markdown.extensions.toc": {
            "title": "Table of Contents",
            "toc_depth": "2"
        },
    },
    "output_format": "html5",
}



TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


PAGINATED_TEMPLATES = {'index': None, 'tag': None, 'category': None, 'archives': None}
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
