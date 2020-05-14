try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Ilja Moisejevs',
    'url': 'URL to get it at',
    'download_url': 'Where to download it.',
    'author_email': 'iljamoisejevs@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47 exercise'
}

setup(**config)
