import codecs
import os
from distutils.core import setup

from uhugo import __version__

HERE = os.path.abspath(os.path.dirname(__file__)) + os.sep


def get_requirements(*parts):
    return codecs.open(os.path.join(HERE, *parts), 'r').read().splitlines()


setup(
    name='uhugo',
    version=__version__,
    packages=get_requirements('requirements.txt'),
    url='https://github.com/akshaybabloo/uHugo',
    license='MIT',
    author='Akshay Raj Gollahalli',
    author_email='akshay@gollahalli.com',
    description='Hugo publisher is a CLI utility helper for Hugo static site builder',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=['hugo', 'hugo cli helper'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
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
