from django.utils import timezone as aware


def get_build_time(request):
    return {
        # https://docs.djangoproject.com/en/stable/topics/i18n/timezones/

        # https://strftime.org/

        "CURRENT_AWARE_DATETIME": aware.now().strftime("%a %d %b %Y at \
            %H:%M:%S %Z %z (%s Unix)"),
    }
