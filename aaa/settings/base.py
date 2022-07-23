import os

from .inc.middleware import *  # noqa


BASE_DIR = \
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = 'some-secret-key'
DEBUG = True


ALLOWED_HOSTS = []

# inst
# middleware

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


ROOT_URLCONF = 'aaa.urls_root'


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
                "aaa.context_processors.dynamic_build_time",
                "aaa.context_processors.dynamic_platform_info",
            ],
        },
    },
]


WSGI_APPLICATION = 'aaa.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'aaa/data/rels.sqlite3'),
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
STATIC_ROOT = os.path.join(BASE_DIR, 'public_collect_static')

DISTILL_DIR = os.path.join(BASE_DIR, 'public')

HTML_MINIFY = True
