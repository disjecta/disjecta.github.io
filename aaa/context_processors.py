# from django.conf import settings
from django.utils import timezone as aware

# for version info on status page
import platform, subprocess
from importlib.metadata import version
import htmlmin # for version


def dynamic_build_time(request):
    return {
        # https://docs.djangoproject.com/en/stable/topics/i18n/timezones/
        # https://strftime.org/
        "CURRENT_AWARE_DATETIME": aware.now().strftime("%a %d %b %Y at \
            %H:%M:%S %Z %z (%s Unix)"),
    }


def dynamic_platform_info(request):

    # https://linuxhint.com/python-subprocess-check_output-method/

    # https://superuser.com/questions/148851/python-check-existence-of-shell-command-before-execution

    # https://unix.stackexchange.com/questions/676370/store-a-value-from-os-release-text-file-after-an-sign-individually

    lsb_cmd = 'lsb_release -drcs | tr -d \'"\''
    lsb_status, lsb_result = subprocess.getstatusoutput(lsb_cmd)

    osr_cmd = '( . /etc/os-release && printf \'%s\n\' "$PRETTY_NAME" )'
    osr_status, osr_result = subprocess.getstatusoutput(osr_cmd)

    if lsb_status == 0:
        OS_VERSION = subprocess.check_output('\
            lsb_release -drcs | tr -d \'"\'', \
                shell=True, universal_newlines = True)
    elif osr_status == 0:
        OS_VERSION = subprocess.check_output('\
            ( . /etc/os-release && printf \'%s\n\' "$PRETTY_NAME" )', \
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
        "DJANGO_HTMLMIN_VERSION_IMPORTLIB": htmlmin.__version__,
        "OS_VERSION": OS_VERSION,
    }
