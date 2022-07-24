from django.urls import path, include


urlpatterns = [
    # ------------------------------------------------------
    # MY APPS
    # ------------------------------------------------------
    path('', include('apps.a0_foundation.urls')),
    path('', include('apps.blog.urls')),

    # ------------------------------------------------------
    # ROOT URLCONF PARTIALS
    # ------------------------------------------------------
    path('', include('config.urls.inc.admin_urls')),
]
