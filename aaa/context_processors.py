import platform, subprocess
from importlib.metadata import version
from django.utils import timezone as aware
# from django.conf import settings


def dynamic_build_time(request):
    return {
        # https://docs.djangoproject.com/en/stable/topics/i18n/timezones/
        # https://strftime.org/
        "CURRENT_AWARE_DATETIME": aware.now().strftime("%a %d %b %Y at \
            %H:%M:%S %Z %z (%s Unix)"),
    }




def dynamic_platform_info(request):

    os_ver_cmd = 'lsb_release -drcs | tr -d \'"\''
    lsb_status, lsb_result = subprocess.getstatusoutput(os_ver_cmd)

    if lsb_status == 0:
        OS_VERSION = subprocess.check_output('\
            lsb_release -drcs | tr -d \'"\'', \
                shell=True, universal_newlines = True)
    else:
        OS_VERSION = ''

    return {
        # https://note.nkmk.me/en/python-sys-platform-version-info/
        # https://itsmycode.com/how-to-check-and-print-python-version/
        # https://stackoverflow.com/questions/20180543/how-to-check-the-version-of-python-modules
        "PYTHON_VERSION_PLATFORM": platform.python_version(),
        
        "PIP_VERSION_IMPORTLIB":  version("pip"),

        "DJANGO_VERSION_IMPORTLIB": version("django"),
        "DISTILL_VERSION_IMPORTLIB": version("django_distill"),
        # django-cachekiller ?

        "OS_VERSION": OS_VERSION,
    }
