"""Production settings and globals."""

from pathlib import Path

from .base import *  # noqa

DEBUG = False
PRODUCTION = True
ALLOWED_HOSTS = [
    "www.example.com",
]

TEMP_ROOT = "/tmp"
WEB_ROOT = Path("/home/foobar/html")
STATIC_ROOT = WEB_ROOT / "static"
STATIC_URL = "/static/"
MEDIA_ROOT = WEB_ROOT / "media"
MEDIA_URL = "/media/"


# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ["https://www.example.com"]

# EMAIL CONFIGURATION
# This is default used for error reports
# For updates, use utilities.mailer
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_PORT = 25
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
DEFAULT_FROM_EMAIL = (
    "chatbot <no-reply@www.example.com>"
)
SERVER_EMAIL = (
    "chatbot Server <no-reply@www.example.com>"
)

# CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches

# See the memcache utilisation using: $ memcstat --servers="127.0.0.1"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
        "TIMEOUT": 30000,  # Every 8 hours
        # can use below in case of memcache error
        # "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        # "LOCATION": "unique-snowflake",
    }
}

CACHE_MIDDLEWARE_KEY_PREFIX = "dj51"

# cached_db is write-through cache where all reads are from cache
# while writes in both in db and cache
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
