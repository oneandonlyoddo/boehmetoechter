# Django settings for weingut_Boehme project.

import os
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Jonas Otto', 'helloworld@jonasotto.de'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'django',
        'PASSWORD': 'o1t2t3o4',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['127.0.0.1']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de'



LANGUAGES = [
    ('de', 'Deutsch'),
    #('en', 'English'),
]

CMS_FALLBACK_LANGUAGE=False

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '' #os.path.join(PROJECT_PATH, "static")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"

STATIC_URL = "/static/"

# Additional locations of static files

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, "static"),

)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'z3fwr7hbm2o9$h=peg-$o10&vl$%6hbek=yki8t**k!x$qdio2'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
   
    
)

ROOT_URLCONF = 'weingut_Boehme.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'weingut_Boehme.wsgi.application'

TEMPLATE_DIRS = (
    # The docs say it should be absolute path: PROJECT_PATH is precisely one.
    # Life is wonderful!
    os.path.join(PROJECT_PATH, "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
     'zinnia.context_processors.version'
)

CMS_TEMPLATES = (
    ('home.html', 'Startseite'),
    ('weingut.html', 'Weingutinfoseite'),
    ('lage.html', 'Lagen'),
    ('lageFreyburgerEdel.html', 'Freyburger Edelacker'),
    ('lageFreyburgerMuehl.html', 'Freyburger Muehlberg'),
    ('lageDorndorf.html', 'Dorndorfer Rappental'),
    ('kontakt.html', 'Kontaktseite'),
    ('impressum_agb.html', 'Impressum oder AGB'),
    ('empfehlungen.html', 'Empfehlungen'),
    ('aktuelles.html', 'Aktuelles und Presse'),
)



INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms', 
    'mptt', 
    'menus',
    'south',
    'sekizai',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'filer',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    #'cmsplugin_filer_video',
    #'cms.plugins.file',
    #'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    #'cms.plugins.snippet',
    #'cms.plugins.teaser',
    'cms.plugins.text',
    #'cms.plugins.video',
    #'cms.plugins.twitter',
    'cmsplugin_contact',
    'djangocms_utils',
    #'simple_translation',
    'tagging',
    'missing',
    #'guardian',
    'django.contrib.comments',
    'zinnia',
    'cmsplugin_zinnia',
    'random_image',
    'hvad',
    'simple_events',
    'glossar',
    'tinymce',
    'easy_thumbnails',
    'cmsplugin_filery',
    'auszeichnungen',
     #'zinnia_extrafields',
     'shop', # The django SHOP application
    'myaddressmodel', # The default Address and country models
    #'weine',
    'webshop',
    'weinkategorien',
    'zinnia_gallery_extrafields',
    #'zinnia_gallery2',
    #'random_image_uploader',
    #'cmsplugin_configurableproduct',
    'shop_categories',
    'shop_simplenotifications',
    'mathfilters',
    'cmsplugin_vimeo',
    'cmsplugin_youtube',
    'imagekit',

    )



RANDOM_IMAGE_DIR = (
    os.path.join(PROJECT_PATH, "/local_static/HomeBackgrounds"),
)

CMS_REDIRECTS = True



CMSPLUGIN_ZINNIA_APP_MENUS = ('cmsplugin_zinnia.menu.EntryMenu',
 'cmsplugin_zinnia.menu.CategoryMenu',
 'cmsplugin_zinnia.menu.TagMenu',
 'cmsplugin_zinnia.menu.AuthorMenu')

CMSPLUGIN_ZINNIA_HIDE_ENTRY_MENU = True

#ZINNIA_ENTRY_BASE_MODEL = 'zinnia_extrafields.models.EntryExtrafields'
#ZINNIA_ENTRY_BASE_MODEL = 'zinnia_gallery2.models.EntryGallery'
#ZINNIA_ENTRY_BASE_MODEL = 'zinnia_gallery_extrafields.models.EntryExtrafields'
#ZINNIA_ENTRY_BASE_MODEL = 'cmsplugin_zinnia.placeholder.EntryPlaceholder'
SHOP_CART_MODIFIERS=(
    #'webshop.cartmodifiers.ShippingDHL',
    #'webshop.cartmodifiers.PreisOhneMehrwertsteuer',
    #'webshop.cartmodifiers.PreisMitMehrwertsteuer',
    )
SHOP_CATEGORIES_CATEGORY_MODEL = 'weinkategorien.models.category.Category'
SHOP_PRODUCT_MODEL='webshop.models.Wein'
SHOP_PAYMENT_BACKENDS=('webshop.payment.backends.vorkasse.Vorkasse',)
SHOP_SHIPPING_BACKENDS=('webshop.shipping.backends.dhl.ShippingDHL',)
SHOP_ADDRESS_MODEL = 'myaddressmodel.models.Address'
#SHOP_SHIPPING_ADDRESS_MODEL = 'myaddressmodel.models.Address'
#SHOP_BILLING_ADDRESS_MODEL = 'myaddressmodel.models.Address'
SHOP_ORDER_MODEL ='webshop.models.myOrder'
THUMBNAIL_TRANSPARENCY_EXTENSION = 'png'
DEFAULT_FROM_EMAIL = 'noreply@myshop.com'

EMAIL_PORT="1025"

CMS_VIMEO_DEFAULT_WIDTH = '640'
CMS_VIMEO_DEFAULT_HEIGHT = '480'
CMS_YOUTUBE_DEFAULT_WIDTH = '640'
CMS_YOUTUBE_DEFAULT_HEIGHT = '480'


#CMSPLUGIN_ZINNIA_TEMPLATES=()

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

# JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'
# JQUERY_UI_JS = 'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js'
# JQUERY_UI_CSS = 'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/jquery-ui.css'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
