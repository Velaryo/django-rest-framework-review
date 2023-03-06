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