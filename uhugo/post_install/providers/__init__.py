import os
from typing import Text


class ProviderBase:
    """
    This is a base class for all the providers
    """

    def __init__(self, api_key: Text = None, config_path: Text = None):
        """

        :param api_key: Authentication key for providers
        :param config_path: Path for configuration file of the provider
        """
        self.api_key = api_key
        self.path = config_path

        if not self.api_key:
            self.api_key = os.environ.get("UHUGO_KEY", None)

        if not self.path:
            self.path = os.environ.get("UHUGO_CONFIG_PATH", None)

        if not self.api_key and not self.path:
            raise ValueError("key or path not set")

    def update_api(self, project_name: Text = None):
        """
        Updates an API
        :return:
        """
        pass

    def update_file(self):
        """
        Updates a configuration file

        :return:
        """
        pass
