"""
Django settings for roster_project project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from pathlib import Path
from environs import Env
from django.conf import settings
from django.contrib.messages import constants as messages

# Use
env = Env()
env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'g0nc)qr-zirf740+ipxyoqb(+@clpa$8^jq4x!j@rd!dh9*l2#'
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = tuple(env.list("ALLOWED_HOSTS", default=[]))


# Application definition

INSTALLED_APPS = [
    "users.apps.UsersConfig",
    "rosters.apps.RostersConfig",
    "api.apps.ApiConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rangefilter",
    "crispy_forms",
    "rest_framework",
]

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware"
    ] + MIDDLEWARE

ROOT_URLCONF = "roster_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "rosters.context_processors.get_roster_name",
            ]
        },
    }
]

WSGI_APPLICATION = "roster_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": env.dj_db_url(
        "DATABASE_URL", default="postgres://postgres@db/postgres"
    ),
    #             {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "webserver/static")

AUTH_USER_MODEL = "users.CustomUser"

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
LOGIN_URL = "login"

# Security
SECURE = env.bool("SECURE")
if not DEBUG and SECURE:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = "DENY"
    SECURE_HSTS_PRELOAD = True

# Logging
LOGLEVEL = env("LOGLEVEL")
LOGFORMAT = env("LOGFORMAT")
LOGTOFILE = env.bool("LOGTOFILE")
if not LOGTOFILE:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "[%(asctime)s] [DJANGO] %(levelname)s %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
            "verbose": {
                "format": "[%(asctime)s] [DJANGO] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "handlers": {
            "console": {
                "level": LOGLEVEL,
                "class": "logging.StreamHandler",
                "formatter": LOGFORMAT,
            },
        },
        "loggers": {
            "": {
                "handlers": ["console"],
                "level": LOGLEVEL,
                "propagate": True,
            }
        },
    }
else:
    LOGSIZE = 1024 * 1024 * 15  # 15MB
    LOGCOUNT = 10
    LOGFILENAME = os.path.join(BASE_DIR, "logs/django.log")
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "[%(asctime)s] [DJANGO] %(levelname)s %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
            "verbose": {
                "format": "[%(asctime)s] [DJANGO] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "handlers": {
            "console": {
                "level": LOGLEVEL,
                "class": "logging.StreamHandler",
                "formatter": LOGFORMAT,
            },
            "file": {
                "level": LOGLEVEL,
                "class": "logging.handlers.RotatingFileHandler",
                "filename": LOGFILENAME,
                "maxBytes": LOGSIZE,
                "backupCount": LOGCOUNT,
                "formatter": LOGFORMAT,
            },
        },
        "loggers": {
            "": {
                "handlers": ["console", "file"],
                "level": LOGLEVEL,
                "propagate": True,
            },
        },
    }

# IPs that can access Debug Toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]


def show_toolbar(request):
    """Determine if toolbar will be displayed."""
    return settings.DEBUG


DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": show_toolbar}

# Crispy forms
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Roster name
ROSTER_NAME = env("ROSTER_NAME")

# Celery
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")

# DRF
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ]
}

# Message colours
MESSAGE_TAGS = {
    messages.SUCCESS: "alert-success",
    messages.ERROR: "alert-danger",
    messages.DEBUG: "alert-secondary",
    messages.INFO: "alert-info",
    messages.WARNING: "alert-warning",
}
