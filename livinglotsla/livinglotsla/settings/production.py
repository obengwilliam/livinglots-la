import os

from .base import *

ADMINS = (
    ('Eric', 'eric@596acres.org'),
)

# TODO Fill with appropriate managers
MANAGERS = (
    ('', 'manager@example.com'),
)

# TODO Fill with appropriate facilitators
FACILITATORS = {
    'global': [
        'eric@596acres.org',
    ],
}

ALLOWED_HOSTS = get_env_variable('ALLOWED_HOSTS').split(',')
MEDIA_ROOT = get_env_variable('MEDIA_ROOT')
STATIC_ROOT = get_env_variable('STATIC_ROOT')


#
# email
#
INSTALLED_APPS += (
    'mailer',
)
EMAIL_BACKEND = 'mailer.backend.DbBackend'
EMAIL_HOST = get_env_variable('EMAIL_HOST')
EMAIL_HOST_USER = get_env_variable('EMAIL_USER')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = get_env_variable('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = get_env_variable('SERVER_EMAIL')


#
# Caching
#
#INSTALLED_APPS = (
    #'cacheops',
#) + INSTALLED_APPS
#CACHEOPS_REDIS = {
    #'host': 'localhost',
    #'port': get_env_variable('REDIS_PORT'),
    #'db': 1,
    #'socket_timeout': 3,
#}
#CACHEOPS = {
    #'django_monitor.*': ('just_enable', 60 * 1),
    #'*.*': ('all', 60 * 60),
#}
#CACHEOPS_DEGRADE_ON_FAILURE = True


#
# logging
#
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'log_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_ROOT, '../../logs', 'django.log'),
            'maxBytes': '16777216', # 16megabytes
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
    'root': {
        'handlers': ['log_file', 'mail_admins'],
        'level': 'WARNING',
    },
}


#
# SSL
#
# TODO uncomment for SSL
#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True
