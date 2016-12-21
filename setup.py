# -*- coding: utf-8 -*-

import codecs
from distutils.core import setup

version = __import__('osmapi').__version__

try:
    import pypandoc
    from unidecode import unidecode
    description = codecs.open('README.md', encoding='utf-8').read()
    description = unidecode(description)
    description = pypandoc.convert(description, 'rst', format='md')
except (IOError, OSError, ImportError):
    description = 'Python wrapper for the OSM API'

setup(
    name='osmapi',
    packages=['osmapi'],
    version=version,
    install_requires=['requests'],
    description='Python wrapper for the OSM API',
    long_description=description,
    author='Etienne Chové',
    author_email='chove@crans.org',
    maintainer='Stefan Oderbolz',
    maintainer_email='odi@metaodi.ch',
    url='https://github.com/metaodi/osmapi',
    download_url='https://github.com/metaodi/osmapi/archive/v%s.zip' % version,
    keywords=['openstreetmap', 'osm', 'api'],
    license='GPLv3',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
