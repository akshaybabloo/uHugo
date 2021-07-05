import os.path
import platform
import tempfile

import requests
from tqdm import tqdm


def download_hugo_zip(version: str, os_type: str = platform.system(), download_to: str = tempfile.gettempdir()) -> str:
    """
    Download the Hugo file to temp folder.

    :param os_type: OS type
    :param version: Version number to download
    :param download_to: Path to download to
    """

    download_to = os.path.join(download_to, f"hugo_{version}")

    with open(download_to, "wb") as file:
        if os_type == 'Darwin':
            response = requests.get(
                f"https://github.com/gohugoio/hugo/releases/download/v{version}/hugo_extended_{version}_macOS-64bit.tar.gz",
                stream=True)
        elif os_type == 'Windows' or os_type == 'nt':
            response = requests.get(
                f"https://github.com/gohugoio/hugo/releases/download/v{version}/hugo_extended_{version}_Windows-64bit.zip",
                stream=True)
        elif os_type == "posix" or os_type == "Linux":
            response = requests.get(
                f"https://github.com/gohugoio/hugo/releases/download/v{version}/hugo_extended_{version}_Linux-64bit.zip",
                stream=True)
        else:
            raise OSError(f"{os_type} not supported.")

        if response.headers.get('Status') == "404 Not Found":
            raise requests.exceptions.HTTPError("File not found")

        print(f"Downloading Hugo v{version} to: ", download_to)
        total_length = int(response.headers.get('content-length'))

        if total_length is None:
            file.write(response.content)
        else:
            with tqdm(total=total_length, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
                for data in response.iter_content(chunk_size=4096):
                    file.write(data)
                    pbar.update(len(data))

    return download_to
