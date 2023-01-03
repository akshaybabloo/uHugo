__version__ = "0.2.0"

import json
from pathlib import Path

# Creates a .uhugo folder in user folder
if not Path.home().joinpath(".uhugo").is_dir():
    Path.home().joinpath(".uhugo").mkdir(exist_ok=True)

# Creates a .uhugo\config.json file in user folder
if not Path.home().joinpath(".uhugo", "config.json").is_file():
    config = {
        "last_checked": None
    }
    with open(Path.home().joinpath(".uhugo", "config.json"), "w") as f:
        json.dump(config, f, indent=4)
