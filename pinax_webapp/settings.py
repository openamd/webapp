# -*- coding: utf-8 -*-
# Django settings for private beta project.

import os.path
import posixpath
import pinax

PINAX_ROOT = os.path.abspath(os.path.dirname(pinax.__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# tells Pinax to use the default theme
PINAX_THEME = 'default'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through django.views.static.serve.
SERVE_MEDIA = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = '/var/www/pinax_webapp/dev.db'       # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'US/Eastern'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'site_media', 'media')
#MEDIA_ROOT = '/var/www/pinax_webapp/media/'

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/site_media/media/'

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = '/var/www/pinax_webapp/site_media/'

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = '/site_media/media/'

# Additional directories which hold static files
STATICFILES_DIRS = (
    ('pinax_webapp', os.path.join(PROJECT_ROOT, 'media')),
    ('pinax', os.path.join(PINAX_ROOT, 'media', PINAX_THEME)),
)

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_openid.consumer.SessionConsumer',
    'account.middleware.LocaleMiddleware',
    'account.middleware.AuthenticatedMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'pinax.middleware.security.HideSensistiveFieldsMiddleware',
)

ROOT_URLCONF = 'pinax_webapp.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
    os.path.join(PINAX_ROOT, "templates", PINAX_THEME),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",

    "pinax.core.context_processors.pinax_settings",
    
    "notification.context_processors.notification",
    "announcements.context_processors.site_wide_announcements",
    "account.context_processors.openid",
    "account.context_processors.account",
    #"socialauth.context_processors.facebook_api_key",

)

INSTALLED_APPS = (
    # included
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.webdesign',

    'pinax.templatetags',
    
    # external
    'avatar',
    'notification', # must be first
    'django_openid',
    'emailconfirmation',
    'mailer',
    'announcements',
    'pagination',
    'timezones',
    'ajax_validation',
    'uni_form',
    'staticfiles',
    'django_extensions',

   # external
    'notification', # must be first
    'django_openid',
    'emailconfirmation',
    'django_extensions',
    'robots',
    'friends',
    'mailer',
    'messages',
    'announcements',
    'oembed',
    'djangodblog',
    'pagination',
#    'gravatar',
    'threadedcomments',
    'threadedcomments_extras',
    'timezones',
    'voting',
    'voting_extras',
    'tagging',
    'blog',
    'ajax_validation',
    'photologue',
    'avatar',
    'flag',
    'locations',
    'uni_form',
    'django_sorting',
    'django_markup',
    'staticfiles',
    
    # internal (for now)


    'analytics',
    'profiles',
    'account',
    'photos',
    'topics',
    'privacy',
    'mining',
    'visual_locations',

    'account',
    'signup_codes',
    
    'about',
    'profiles',
    
    'django.contrib.admin',

)

ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda o: "/profiles/profile/%s/" % o.username,
}

MARKUP_FILTER_FALLBACK = 'none'
MARKUP_CHOICES = (
    ('restructuredtext', u'reStructuredText'),
    ('textile', u'Textile'),
    ('markdown', u'Markdown'),
    ('creole', u'Creole'),
)
WIKI_MARKUP_CHOICES = MARKUP_CHOICES

AUTH_PROFILE_MODULE = 'profiles.Profile'
NOTIFICATION_LANGUAGE_MODULE = 'account.Account'

ACCOUNT_OPEN_SIGNUP = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG
CONTACT_EMAIL = "amd@hope.net"
SITE_NAME = "HOPE AMD"
LOGIN_URL = "/account/login" # "/accounts/login/"
LOGIN_REDIRECT_URL = "/profiles"
LOGIN_REDIRECT_URLNAME = "what_next"

AUTHENTICATED_EXEMPT_URLS = [
    r"^/$",
    r"^/admin$",

    r"^/account/signup/$",
    r"^/account/login",
    r"^/success/$",
    r"^/register/$",
    r"^/account/password_reset",
    r"^/account/confirm_email",

    r"/map",
    r"/xd_receiver.htm",
]

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass
