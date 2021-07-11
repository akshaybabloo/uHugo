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
    --to TEXT            Updates to a specified version
    --help               Show this message and exit.