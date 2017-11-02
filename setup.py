import os
import sys

from setuptools import setup, find_packages

# pylint: disable=invalid-name
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, *('doc', 'DESCRIPTION.rst'))) as f:
    DESCRIPTION = f.read()
with open(os.path.join(here, 'CHANGELOG')) as f:
    CHANGELOG = f.read()

requires = [
    'bleach',
    'Flask',
    'MarkupSafe'
]

if sys.version_info[0] < 3:  # python 2.7
    requires.extend([
        'typing',
    ])

development_requires = [
    'colorlog',
    'flake8',
    'pylint',
]

testing_requires = [
    'colorlog',
    'pytest',
    'pytest-cov',
]

production_requires = [
]

setup(
    name='lutece',
    version='0.1',
    description='LUpine sofTwarE website to introduCE about our product and'
                'ourselves',
    long_description=DESCRIPTION + '\n\n' + CHANGELOG,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Flask",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Lupine Software LLC',
    author_email='feedback@lupine-software.com',
    url='https://lupine-software.com',
    keywords='web wsgi flask',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'development': development_requires,
        'testing': testing_requires,
        'production': production_requires,
    },
    install_requires=requires,
)
