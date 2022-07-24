from django.contrib import admin
from django.urls import path
from django.conf import settings


admin.site.site_title = settings.SITE_TITLE
admin.site.index_title = "Admin Home"
admin.site.site_header = settings.SITE_TITLE + " admin dash"


urlpatterns = [
    path('admin/', admin.site.urls),
]
