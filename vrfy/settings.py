"""
Django settings for vrfy project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '#yu7$c#_y#2sip5i@hi^#iocpoa0))m14@e3ob_#0&#rvj_)w+'
DEBUG = True
TEST = True
ALLOWED_HOSTS = ["localhost"]
INTERNAL_IPS = ['127.0.0.1','localhost']

#Grappelli settings
GRAPPELLI_ADMIN_TITLE = "CS@Reed Admin"
GRAPPELLI_INDEX_DASHBOARD = "vrfy.dashboard.CustomIndexDashboard"

# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vrfy',
    'vrfy.apps.LDAPAuthConfig',
    'vrfy.apps.CourseConfig',
    'vrfy.apps.CatalogConfig',
)

#Authentication Settings (With ModelBackend as a fallback)
AUTHENTICATION_BACKENDS = (
    'ldap_auth.auth_backend.LDAPRemoteUserBackend',
    'django.contrib.auth.backends.ModelBackend',
    # 'django.contrib.auth.backends.RemoteUserBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'ldap_auth.auth_middleware.LDAPRemoteUserMiddleware',
    # 'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'vrfy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'vrfy.wsgi.application'


# Database Info
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vrfy_dev',
        'USER': 'vrfy_dev_usr',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SERVER_EMAIL = 'isjoriss@reed.edu'

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = 'staticfiles/'
STATIC_URL = '/static/'
MEDIA_ROOT = 'problem_assets/'
MEDIA_URL = '/problem_assets/'
STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "bower_components"),
)

#TANGO Settings (for more info see documentation/tango.md)

#address of the tango server
TANGO_ADDRESS = "http://localhost:3300/"
#key to access tango server
TANGO_KEY = "test"
#location of the tango courselabs folder
TANGO_COURSELAB_DIR = "/home/alex/verify_project/courselabs/"
#name of the makefile to be called in Tango
MAKEFILE_NAME="autograde-Makefile"
