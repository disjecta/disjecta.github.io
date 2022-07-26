import os

from .inc.middleware import *  # noqa

SITE_TITLE = 'Disjecta'

BASE_DIR = \
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = 'some-secret-key'

# inst
# middleware

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


ROOT_URLCONF = 'config.urls.root'  # allow for partials


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # project custom context processors
                "config.context_processors.dependency_reporting.get_dep_versions",
                "config.context_processors.os_detection.get_os",
                "config.context_processors.settings_injection.get_settings",
                "config.context_processors.timestamp_creation.get_build_time",
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data/rels.sqlite3'),
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../public_collect_static')

DISTILL_DIR = os.path.join(BASE_DIR, '../public')
