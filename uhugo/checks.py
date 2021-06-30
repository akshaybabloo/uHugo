import os

if os.name == 'nt':
    from .terminal_commands.windows import *
elif os.name == 'posix':
    from .terminal_commands.posix import *
else:
    raise OSError("Unknown OS")

