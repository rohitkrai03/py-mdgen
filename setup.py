try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
    'description': 'This is a simple project for generating MarkDwon Syntax from simple text files.',
    'author': 'Rohit Rai',
    'url': 'url',
    'download_url': 'download_url',
    'author_email': 'rohitkrai03@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['mdgen'],
    'scripts': [],
    'name': 'MarkDown Generator'
}

setup(**config)
