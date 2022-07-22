from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # ------------------------------------------------------
    # APPS
    # ------------------------------------------------------
    path('', include('aaa.apps.blog.urls')),

    # ------------------------------------------------------
    # OTHER
    # ------------------------------------------------------
    path('admin/', admin.site.urls),
]
