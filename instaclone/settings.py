import os
from decouple import config
# import  dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
MODE = config("MODE", default="dev")
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&5eh1%0$celnz7n8%^(pq12%q3_&w6stl-izw&!*p9e%cffurl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

UPLOADCARE = {
    'pub_key': config('pub_key'),
    'secret': config('secret'),
}


# Application definition

INSTALLED_APPS = [
    'pyuploadcare.dj',
    'photos',
    'tinymce',
    'bootstrap3',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'csvimport.app.CSVImportConf',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'instaclone.urls'

TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'instaclone.wsgi.application'
LOGIN_REDIRECT_URL = '/home'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# if config('MODE') == "dev":
DATABASES = {
        'default': {
            'ENGINE':  'django.db.backends.postgresql',
            'NAME': config('DBNAME'),
            'USER': config('DBUSER'),
            'PASSWORD': config('DBPASS')
            }
}

# production
# else:
#    DATABASES = {
#        'default': dj_database_url.config(
#            default=config('DATABASE_URL')
#        )
#    }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

db_from_env=dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_STORAGE='whitenoise.django.GzipManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')



# Email configurations remember to install python-decouple
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
LOGIN_REDIRECT_URL = "welcome"
