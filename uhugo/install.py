import tarfile
import zipfile
from pathlib import Path
import logging

log = logging.getLogger(__file__)


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


def install(extract_from: str, os_type: str, move_to: str = bin_folder()):
    """
    Installs the ``hugo`` binary at a given path

    :param extract_from: The path zip/tar file downloaded
    :param os_type: Type of OS - ``Windows``, ``Darwin`` or ``posix``.
    :param move_to: Instillation location. Defaults to :py:func:`bin_folder`
    """

    print("Extracting and moving file to: ", move_to)
    if os_type == 'Darwin' or os_type == 'posix':
        with tarfile.open(extract_from, "r:gz") as f:
            f.extract("hugo", move_to)
    elif os_type == 'Windows':
        with zipfile.ZipFile(extract_from, "r") as f:
            f.extract("hugo.exe", move_to)
