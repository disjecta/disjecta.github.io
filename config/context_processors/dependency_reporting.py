import platform
from importlib.metadata import version
import htmlmin # for version


def get_dep_versions(request):

    return {
        # https://note.nkmk.me/en/python-sys-platform-version-info/

        # https://itsmycode.com/how-to-check-and-print-python-version/

        # https://stackoverflow.com/questions/20180543/how-to-check-the-version-of-python-modules

        "PYTHON_VERSION": platform.python_version(),

        "PIP_VERSION":  version("pip"),
        "DJANGO_VERSION": version("django"),
        "DISTILL_VERSION": version("django_distill"),

        "HTMLMIN_VERSION": htmlmin.__version__,

        # django-cachekiller? compressor? django-bakery?
    }
