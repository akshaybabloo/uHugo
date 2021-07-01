import logging
from typing import Text

import click

from . import __version__

log = logging.getLogger(__name__)


@click.group(name="uhugo",
             help="uhugo is a Hugo binary helper that downloads and set ups the environment.")
@click.option('--debug/--no-debug', help="Use debug mode", default=False)
@click.version_option(__version__, package_name="uHugo", prog_name="uHugo")
@click.pass_context
def cli(ctx: click.core.Context, debug: bool):
    ctx.ensure_object(dict)
    ctx.obj['debug'] = debug

    if debug:
        logging.basicConfig(level='DEBUG')


@cli.command(help="Install latest Hugo binary files")
@click.option("--ver", help="Hugo version to download")
@click.pass_context
def install(ctx: click.core.Context, ver: Text):
    pass


@cli.command(help="Updates Hugo binary files and any associated configurations")
@click.option("--to", help="Updates to a specified version")
@click.pass_context
def update(ctx: click.core.Context, to: Text):
    pass


@cli.command(help="Delete, reinstall Hugo binary and update paths accordingly")
def reset(ctx: click.core.Context):
    pass


def main():
    cli(obj={})
