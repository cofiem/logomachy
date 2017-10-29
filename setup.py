"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open

import os
import re


here = os.path.abspath(os.path.dirname(__file__))


# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def get_version():
    version = None
    version_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), '_version.py')
    fp = open(version_file)
    with fp:
        for line in fp:
            match = re.match("__version__ = '([^']+)'", line)
            if match:
                version = match.group(1)
    if version is None:
        raise ValueError('no version available')
    return version


setup(
    name='logomachy-text',
    version=get_version(),
    description='A Django application for indexing, analysing, and comparing text, '
                'particularly EULA, ToS, privacy statements, and other documents.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/cofiem/logomachy',
    author='Mark Cottman-Fields',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Operating System :: Unix',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
    ],
    keywords='text django web natural-language-analysis',

    packages=find_packages(exclude=['docs', 'tests']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'django', 'docutils', 'pytz',
        'numpy', 'nltk', 'spacy'],

    python_requires='>=3.5.*, <4',

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['bumpversion', 'mypy', 'typed-ast', 'check-manifest'],
        'test': ['coverage', 'lxml'],
    },

    include_package_data=True,
    zip_safe=False
)
