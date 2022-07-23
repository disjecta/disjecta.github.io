MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #  the order of these matters when using Django's caching middleware
    'htmlmin.middleware.HtmlMinifyMiddleware',  # not in dev
    'htmlmin.middleware.MarkRequestMiddleware',  # not in dev
]
