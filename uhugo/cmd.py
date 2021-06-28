import click
from . import __version__


@click.group(name="uhugo",
             help="uhugo is a Hugo binary helper that downloads and set ups the environment.")
@click.option('--debug', help="Use debug mode", is_flag=True)
@click.version_option(__version__, package_name="uHugo", prog_name="uHugo")
@click.pass_context
def cli(ctx, debug: bool):
    ctx.obj['debug'] = debug


@cli.command(help="Install latest Hugo binary files")
@click.option("--ver", help="Hugo version to download")
@click.pass_context
def install(ctx, ver: str):
    pass


@cli.command(help="Updates Hugo binary files and any associated configurations")
@click.option("--to", help="Updates to a specified version")
@click.pass_context
def update(ctx, to: str):
    pass


@cli.command(help="Delete, reinstall Hugo binary and update paths accordingly")
def reset(ctx):
    pass


def main():
    cli(obj={})
