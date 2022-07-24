import subprocess


def get_os(request):

    """
    https://linuxhint.com/python-subprocess-check_output-method/

    https://superuser.com/questions/148851/python-check-existence-of-shell-command-before-execution

    https://unix.stackexchange.com/questions/676370/store-a-value-from-os-release-text-file-after-an-sign-individually

    to tempoarily remove lsb_release on Manjaro, so that elif condition succeeds:
    sudo pacman -R manjaro-hello web-installer-url-handler python-manjaro-sdk manjaro-release lsb-release

    elif contion works locally, but not on GitLab Pages CI, even though the GLP
    CI log outputs PRETTY_NAME="Debian GNU/Linux 11 (bullseye)"
    """

    lsb_cmd = 'lsb_release -drcs | tr -d \'"\''
    lsb_status, lsb_result = subprocess.getstatusoutput(lsb_cmd)

    osr_cmd = '( . /etc/os-release && printf \'%s\n\' "$PRETTY_NAME" )'
    osr_status, osr_result = subprocess.getstatusoutput(osr_cmd)

    result_fail = 'command not found'

    if lsb_status == 0 and lsb_result.find(result_fail) == -1:
        OS_VERSION = subprocess.check_output(lsb_cmd, shell=True, \
            universal_newlines = True)
    elif osr_status == 0 and osr_result.find(result_fail) == -1:
        OS_VERSION = subprocess.check_output(osr_cmd, shell=True, \
            universal_newlines = True)

    return {
        "OS_VERSION": OS_VERSION,
    }
