REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': 'rest_framework.permissions.IsAuthenticates',
    'PAGE_SIZE': 10
}

INSTALLED_APPS = ['corsheaders'] 
MIDLLEWARE = ['corsheaders.middleware.CorsMiddleware']
CORS_ALLOW_ALL_ORIGINS = True