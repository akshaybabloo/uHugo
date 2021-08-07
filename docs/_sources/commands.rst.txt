Commands
========

uHugo is a CLI that comes with two commands

Install
-------

`uhugo install` command can be used to install or force install a latest Hugo binary. If a binary already exists and you wish to reinstall then you can use
``--force`` flag.

Install Help
~~~~~~~~~~~~

.. code-block:: sh

    > uhugo install --help
    Usage: uhugo install [OPTIONS]
    
      Install latest Hugo binary files
    
    Options:
      -v, --version TEXT  Hugo version to download
      --force             Reinstall Hugo
      --help              Show this message and exit.    

Update
------

``uhugo update`` can be used to update an existing binary. This command can also be used to downgrade Hugo version using the ``--to <version number>`` flag.

Update Help
~~~~~~~~~~~

.. code-block:: sh

    > uhugo update --help
    Usage: uhugo update [OPTIONS]

      Updates Hugo binary files and any associated configurations

    Options:
      --to TEXT     Updates to a specified version
      --only-hugo   Updates only Hugo binary while ignoring providers
      --only-cloud  Updates only cloud providers while ignoring Hugo
      --help        Show this message and exit.

--to Flag
~~~~~~~~~

.. versionadded:: 0.0.8

``--to <version number>`` can be used to install a specific version of Hugo binary

--only-hugo Flag
~~~~~~~~~~~~~~~~

``--only-hugo`` is a binary flag. It can be used when you only want to update Hugo binary and ignore updating cloud provider

--only-cloud Flag
~~~~~~~~~~~~~~~~~

.. versionadded:: 0.0.8

``only-cloud`` is a binary flag. It can be used when you only want to update cloud provider and ignore updating Hugo binary
