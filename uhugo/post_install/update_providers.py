import logging
import os
from typing import List

from rich.console import Console
from rich.prompt import Prompt

from uhugo.post_install.detect_providers import Provider

log = logging.getLogger(__name__)


class UpdateProvider:
    """
    Update providers with Hugo version
    """

    def __init__(self, providers: List[Provider], console: Console, version: str):
        """
        :param providers: List of Provider objects
        :param console: Rich Console object
        :param version: Hugo version
        """
        self.providers = providers
        self.console = console
        self.version = version

    def update(self):
        """
        Update providers with Hugo version
        """
        for provider in self.providers:
            if provider.name == "netlify":
                self.update_netlify()
            elif provider.name == "vercel":
                self.update_vercel()
            elif provider.name == "cloudflare":
                self.update_cloudflare(provider)

    def update_netlify(self):
        pass

    def update_vercel(self):
        pass

    def update_cloudflare(self, provider: Provider):
        """
        Update Cloudflare provider with environment variables

        :param provider: Provider object
        """
        for key, val in provider.dict().items():
            if val and val.startswith("env"):
                try:
                    setattr(provider, key, os.environ[val.split(":")[1]])
                except KeyError as e:
                    log.debug(e)
                    self.console.print(f"Environment variable '{val.split(':')[1]}' not found", style="bold red")
                    exit(1)

        from ..post_install.providers.cloudflare import Cloudflare

        cf = Cloudflare(provider.api_key, provider.email_address, provider.account_id, self.version)
        projects = cf.get_projects(provider.project).json()
        if projects["success"] and isinstance(projects["result"], list):
            names = [name["name"] for name in projects["result"]]
            name = Prompt.ask("Enter project name", choices=names)
        elif not projects["success"]:
            self.console.print("There was an error fetching your Cloudflare project", style="bold red")
            log.debug(projects)
            exit(1)
        else:
            name = provider.project

        current_version = cf.current_version(name)
        if current_version != self.version:
            log.debug(f"Current Hugo version in Cloudflare: v{current_version}")
        else:
            self.console.print(":heavy_check_mark: Hugo version is already up to date")
            return

        response = cf.update_api(name).json()
        if not response["success"]:
            self.console.print("There was an error updating your Cloudflare environment")
            log.debug(response)
            exit(1)
        self.console.print(
            f":heavy_check_mark: Cloudflare updated with Hugo v{self.version} :tada:", style="green bold"
        )
