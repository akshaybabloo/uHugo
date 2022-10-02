import codecs
import os
import pathlib
from distutils.core import setup

from setuptools import find_packages

from uhugo import __version__

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')


def get_requirements(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read().splitlines()


setup(
    name='uhugo',
    version=__version__,
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages(),
    url='https://github.com/akshaybabloo/uHugo',
    license='MIT',
    author='Akshay Raj Gollahalli',
    author_email='akshay@gollahalli.com',
    description='Hugo publisher is a CLI utility helper for Hugo static site builder',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['hugo', 'hugo cli helper'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities'
    ],
    entry_points={
        'console_scripts': [
            'uhugo = uhugo.cmd:main'
        ]
    }
)
