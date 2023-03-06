# Pasos para deploy

## 1. Instalar dependencias
```
pip install gunicorn

pip install django-environ
```

## 2. Crear requirements.txt
```
pip freeze > requirements.txt
```

## 3. Crear Procfile

```
web: python manage.py migrate && gunicorn movies.wsgi
```

## 4. Crear DB en Railway
Se está usando mysql por defecto.

[railway.app](https://railway.app/)

## 5. Configurar variables de entorno
```
MYSQLDATABASE=''
MYSQLUSER=''
MYSQLPASSWORD=''
MYSQLHOST=''
MYSQLPORT=''
```

## 6. Configuración del dominio
```py
ALLOWED_HOSTS = [
    "localhost", 
    "django-rest-framework-review-production-4dca.up.railway.app"
]

CSRF_TRUSTED_ORIGINS = [
    "https://django-rest-framework-review-production-4dca.up.railway.app"
]
```

## 7. Configuración para archivos estáticos

```py

INSTALLED_APPS = [
    ...
    'whitenoise.runserver_nostatic',
    ...
]

MIDDLEWARE = [
    ...
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

```