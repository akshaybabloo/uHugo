import os
from pathlib import Path
from typing import Union, List

from pydantic import BaseModel


class Provider(BaseModel):
    """
    This holds the information about the provider
    """

    name: Union[str, None] = None
    project: Union[str, None] = None
    file_name: Union[str, None] = None
    api_key: Union[str, None] = None
    account_id: Union[str, None] = None
    email_address: Union[str, None] = None
    path: Union[str, None] = None


def check_hugo_file(cwd=os.getcwd()) -> Provider:
    """
    Checks for ``config.yaml`` or ``config.toml``, if exists then it checks for ``uhugo`` key

    :return Provider: An object with ``name`` and ``file_name``
    """

    path = Path(cwd, "config.toml")
    if not path.exists():
        path = Path(cwd, "config.yaml")
        if not path.exists():
            return Provider()
        else:
            import yaml

            try:
                from yaml import CLoader as Loader, CDumper as Dumper
            except ImportError:
                from yaml import Loader, Dumper
            with open(path) as f:
                data = yaml.load(f, Loader=Loader)
    else:
        import toml

        with open(path) as f:
            data = toml.load(f)

    if "uhugo" not in data:
        return Provider()

    return Provider(**data["uhugo"])


def check_providers_fs(cwd=os.getcwd()) -> List[Provider]:
    """
    Checks file system for any providers that matches the list

    :return: A Provider
    """

    files = ["netlify.yaml", "vercel.json", "netlify.toml", "wrangler.jsonc"]
    providers: List[Provider] = []

    for file in files:
        path = Path(cwd, file)
        if path.exists():
            providers.append(
                Provider(**{"name": path.name.split(".")[0], "path": path.__str__()})
            )

    return providers
