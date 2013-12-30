try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A PDS Image library based on the GDAL implementation.',
    'author': 'Austin Godber',
    'url': 'https://github.com/godber/gdal_pds',
    'download_url': 'https://github.com/godber/gdal_pds',
    'author_email': 'godber@uberhip.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['gdal_pds'],
    'scripts': [],
    'name': 'gdal_pds'
}

setup(**config)
