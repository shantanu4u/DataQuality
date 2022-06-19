import os

DB_USERNAME=os.environ.get("DB_USERNAME")
DB_PASSWORD=os.environ.get("DB_PASSWORD")
DB_HOST=os.environ.get("DB_HOST")
DB_PORT=os.environ.get("DB_PORT")
DB_DATABASE=os.environ.get("DB_DATABASE")
DB_IS_AVAIL = all([
        DB_USERNAME, 
        DB_PASSWORD, 
        DB_HOST,
        DB_PORT,
        DB_DATABASE
])

if DB_IS_AVAIL:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DB_DATABASE,
            "USER": DB_USERNAME,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
            "PORT": DB_PORT,
        }
    }