import os

if os.name == 'nt':
    from .terminal_commands.windows import *
elif os.name == 'posix':
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