Providers
=========

.. versionadded:: 0.0.3

Providers are basically cloud providers that host your static website. uHugo comes with three providers. 
These providers can be set in Hugo's ``config.yaml`` or ``config.toml``, using the following configurations

.. tabs::

    .. code-tab:: toml config.toml

        [uhugo]
        name = "<name of the provider>"
        project = "<project name or ID>"
        email_address = "<email address of the user authenticated>" # part of cloudflare
        account_id = "<Cloudflare workers account ID>" # part of cloudflare
        api_key = "<authentication key>"
        file_name = "<name of the configuration file>"

    .. code-tab:: yaml config.yaml

        uhugo:
            name: <name of the provider>
            project = <project name or ID>
            email_address: <email address of the user authenticated>
            account_id: <Cloudflare workers account ID>
            api_key: <authentication key>
            file_name: <name of the configuration file>

.. note:: A configuration with ``env`` values tells uHugo to search in environment value. Internally ``api_key = "env"``, will search for ``os.environ["api_key"]``

Definitions
-----------

Certain properties in the above configuration are optional, this depends on the cloud providers.

Name Property
~~~~~~~~~~~~~

``name`` property describes the type of cloud providers to choose. Currently, uHugo supports the following cloud providers:

.. toctree::
    :maxdepth: 2
 
    cloudflare

.. _api-key-property:

API Key Property
~~~~~~~~~~~~~~~~

``api_key`` is the authentication token provided by the cloud provider. This property is required when using :doc:`cloudflare`.

File Name Property
~~~~~~~~~~~~~~~~~~

``file_name`` property is the name of the configuration file. This property is required for Netlify and Vercel (can be left blank if :ref:`api-key-property` is provided). 
