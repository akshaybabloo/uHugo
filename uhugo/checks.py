import json
import platform
from pathlib import Path
import logging

import requests

log = logging.getLogger(__name__)

if platform.system() == 'Windows':
    from .terminal_commands.windows import *
elif platform.system() == 'Linux' or platform.system() == 'Darwin':
    from .terminal_commands.posix import *
else:
    raise OSError("Unknown OS")


def bin_folder() -> str:
    """
    Gives the path of the user bin folder if exists else a bin folder is created in the
    ``<user home>/bin``

    :return: ``bin`` location
    """

    bin_path = Path(Path.home(), "bin")

    if not bin_path.is_dir():
        log.debug(f"bin directory does not exists. Creating one now. New path: {bin_path!r}")
        bin_path.mkdir()

    return str(bin_path)


def get_latest_version_api(override_version: str = None) -> str:
    """
    Get the latest Hugo version

    :return: version number
    """

    if override_version is not None:
        return override_version

    hugo_response = requests.get("https://api.github.com/repos/gohugoio/hugo/releases/latest")
    hugo_response = json.loads(hugo_response.content.decode('utf-8'))['tag_name'][1:]

    return hugo_response
