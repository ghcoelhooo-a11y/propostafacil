from pathlib import Path
from django.contrib.messages import constants as messages

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# ⚠️ Troque esse valor por um gerado com
# >>> from django.core.management.utils import get_random_secret_key
# >>> print(get_random_secret_key())
SECRET_KEY = 'django-insecure-*8uilf48_+!3f^-5nt1i2$*=4o^+@px2drjqwkyq_#=q1bq^'

# Ambiente de desenvolvimento → True
# Quando for publicar em produção → False
DEBUG = True

# Hosts permitidos
# Em desenvolvimento: vazio ou localhost/127.0.0.1
# Em produção: coloque o domínio do site (ex.: 'meuprojeto.com')
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# ==============================
# Apps instalados
# ==============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # seu app principal
    'core',
]

# ==============================
# Middlewares
# ==============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==============================
# URLs principais
# ==============================
ROOT_URLCONF = 'meu_projeto.urls'

# ==============================
# Templates
# ==============================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # pasta /templates na raiz do projeto
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'meu_projeto.wsgi.application'


# ==============================
# Banco de dados (SQLite por padrão)
# ==============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==============================
# Configurações regionais
# ==============================
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


# ==============================
# Autenticação
# ==============================
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'cliente_list'
LOGOUT_REDIRECT_URL = 'login'


# ==============================
# Arquivos estáticos
# ==============================
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]


# ==============================
# Configuração de mensagens
# ==============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}
