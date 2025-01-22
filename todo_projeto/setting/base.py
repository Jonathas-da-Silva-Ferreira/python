import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'sua_chave_secreta_aqui'

INSTALLED_APPS = [
    'django.contrib.adimin'
    'django.contrib.auth'
    'django.contrib.contenttypes'
    'django.contrib.sessions'
    'django.contrib.messages'
    'django.contrib.staticfiles'
    'tasks'
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware'
    'django.contrib.sessions.middleware.SessionMiddleware'
    'django.middleware.common.CommonMiddleware'
    'django.middleware.csrf.CsrfViewMiddleware'
    'django.contrib.auth.middlware.AuthenticationMiddlewa'
    'django.contrib.messages.middleware.MessageMiddleware'
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'todo_projeto.urls'

DATABASE = {
        'default':{
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
}