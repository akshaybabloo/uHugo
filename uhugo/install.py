import logging
import tarfile
import zipfile

from .checks import bin_folder

log = logging.getLogger(__name__)


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
