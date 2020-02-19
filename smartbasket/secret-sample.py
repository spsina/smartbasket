# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8yj3=&atm#hp3oh%jcm%$iwwtfqogqgv51yy+%^%icm^aaw%1+'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'smartbasket',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
