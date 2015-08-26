ROOT_URLCONF = "example.app.urls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "default",
    }
}

INSTALLED_APPS = (
    "example.app",
)

SECRET_KEY = "wow much secure"

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
)
