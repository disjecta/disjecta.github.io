from django.conf import settings

def get_settings(request):
    return {
        'SITE_TITLE': getattr(settings, 'SITE_TITLE', None),
        'SITE_HEAD_TITLE_ENV': getattr(settings, 'SITE_HEAD_TITLE_ENV', None),
    }