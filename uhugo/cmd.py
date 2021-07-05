import logging
from typing import Text
from packaging import version
import platform
from rich.console import Console

import click

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
        logging.basicConfig(level='DEBUG', format="%(asctime)s %(name)s - %(levelname)s:'%(message)s'", datefmt='%d-%b-%y %H:%M:%S')


@cli.command(help="Install latest Hugo binary files")
@click.option("--version/-v", 'ver', help="Hugo version to download")
@click.pass_context
def install(ctx: click.core.Context, ver: Text):
    console = Console()

    hugo = check_hugo()
    if hugo.exists:
        click.echo("Hugo has already been installed. Use 'uhugo update' to update.")
        exit(0)

    _ver = get_latest_version_api(ver)
    download_path = download_hugo_zip(_ver)
    installed_path = install_hugo(download_path)

    click.echo(console.print("Hugo installed! :tada:", style='green bold'), color=True)
    click.echo(console.print(f"Make sure '{installed_path}' is in your $PATH", style="bold"), color=True)


@cli.command(help="Updates Hugo binary files and any associated configurations")
@click.option("--to", help="Updates to a specified version")
@click.pass_context
def update(ctx: click.core.Context, to: Text):
    pass


@cli.command(help="Delete, reinstall Hugo binary and update paths accordingly")
@click.pass_context
def reset(ctx: click.core.Context):
    pass


def main():
    cli(obj={})
