import imp
from os import path

from setuptools import find_packages, setup


VERSION = imp.load_source('version', path.join('.', 'trellominer', 'version.py'))
VERSION = VERSION.__version__

REQUIRES = [
    'requests==2.12.5',
    'openpyxl==2.4.5',
    'ruamel.yaml==0.13.10'
]

setup(
    name='trellominer',
    version=VERSION,
    description='Pull data from Trello and write into Excel',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment ::',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Officer/Business :: Financial :: Spreadsheet',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='reporting excel trello http api',
    author='Paul Stevens',
    author_email='ps@xnode.co.za',
    url='https://xnoder.co.za/',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIRES,
    setup_requires=[],
    entry_points={
        'console_scripts': [
            'trellominer = trellominer.cmd.trellominer:main',
        ]
    }
)
