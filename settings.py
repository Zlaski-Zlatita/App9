# Build paths inside the project oike this: os.path.join (BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production 
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET KEY = 'dti-35gg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True 

ALLOWED_HOSTS = []


# Application definition 

INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
]

MIDDLEWARE = [
        'django.middleware.settingsSecurityMiddleware',
        'django.contrib.sessions.middlewareSessionMiddleware',
        'django.contrib.common.CommonMiddleware',
  

