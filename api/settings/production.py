from base import *

# paths
LOG_PATH = ""

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k7t!okgf5g=t#3#k)yl#4*q_qqm#z2l8#r+du70gsq77f2y9qy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

STATIC_URL = '/static/'

LOGGING.update( {
    'handlers': {
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH,
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'api': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
        },
    }
})