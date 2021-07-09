import os
from typing import Text

import requests

from uhugo.post_install.providers import ProviderBase


class Cloudflare(ProviderBase):
    """
    Cloudflare provider
    """

    def __init__(self, api_key: Text = None, email_address: Text = None, account_id: Text = None):
        """

        :param api_key: Authentication key for Cloudflare
        :param email_address: Registered email address
        :param account_id: Cloudflare worker account ID
        :raises ValueError: If ``email_address`` and ``account_id`` is not provided
        """
        super().__init__(api_key, None)

        self.account_id = account_id

        if not email_address:
            email_address = os.environ.get("CLOUDFLARE_EMAIL", None)

        if not self.account_id:
            self.account_id = os.environ.get("CLOUDFLARE_WORKER_ACCOUNT_ID", None)

        if not email_address and not self.account_id:
            raise ValueError("email_address and account_id not provided")

        self.headers = {
            "X-Auth-Email": email_address,
            "X-Auth-Key": self.api_key
        }

    def update_api(self, project_name: Text = None):
        """
        Updates Cloudflare Pages environment variable of ``HUGO_VERSION``.

        :param project_name: Name of the project to update
        :return:
        """

        if not project_name:
            projects = self._get_projects()
            print(projects)

        print(self._get_project(project_name))

    def _get_projects(self):

        response = requests.get(f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/pages/projects",
                                headers=self.headers)
        return response.content

    def _get_project(self, project_name: Text):
        response = requests.get(f"https://api.cloudflare.com/client/v4/accounts/{self.account_id}/pages/projects/{project_name}",
                                headers=self.headers)
        return response.content
