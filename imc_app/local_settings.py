# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--1%i3xi_lz0x2gga%4&(v$-%hs+(%d$7=uc$3#!@_@g$p%sc18'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'imc',
        'USER': 'imcadmin',
        'PASSWORD': 'JULOez1.',
        'HOST': 'localhost'

    }
}

