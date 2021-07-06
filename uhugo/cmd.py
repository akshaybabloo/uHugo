import logging
import os
from typing import Text

import click
from rich.console import Console
from rich.panel import Panel

from . import __version__
from .checks import check_hugo, get_latest_version_api
from .download import download_hugo_zip
from .install import install_hugo

log = logging.getLogger(__name__)


@click.group(name="uhugo",
             help="uhugo is a Hugo binary helper that downloads and set ups the environment.")
@click.option('--debug', help="Use debug mode", default=False, is_flag=True)
@click.version_option(__version__, package_name="uHugo", prog_name="uHugo")
@click.pass_context
def cli(ctx: click.core.Context, debug: bool):
    ctx.ensure_object(dict)
    ctx.obj['debug'] = debug

    if debug:
        logging.basicConfig(level='DEBUG',
                            format="%(asctime)s %(name)s - %(levelname)s:'%(message)s'",
                            datefmt='%d-%b-%y %H:%M:%S')


@cli.command(help="Install latest Hugo binary files")
@click.option('--version', '-v', 'ver', default=None, help="Hugo version to download")
@click.option('--force', is_flag=True, default=False, help="Reinstall Hugo")
def install(ver: Text, force: bool):
    console = Console()

    hugo = check_hugo()
    if hugo.exists and not force:
        click.echo(console.print("Hugo has already been installed. Use 'uhugo update' to update.",
                                 style="red"))
        exit(0)

    if force:
        log.debug(f"Deleting existing Hugo at {hugo.path}")
        os.remove(hugo.path)

    with console.status("Fetching latest version", spinner="dots"):
        _ver = get_latest_version_api(ver)
    click.echo(console.print(f"- Latest version is v{_ver}", style="yellow bold"), color=True)

    download_path = download_hugo_zip(_ver)

    with console.status(f"Installing Hugo {_ver}", spinner="dots"):
        installed_path = install_hugo(download_path)

    console.print("\nHugo installed! :tada:\n", style='green bold')

    console.print(Panel.fit(f"[bold green]Make sure {installed_path!r} is in your $PATH", title="Note"))


@cli.command(help="Updates Hugo binary files and any associated configurations")
@click.option("--to", help="Updates to a specified version")
def update(to: Text):
    console = Console()
    pass


def main():
    cli(obj={})
