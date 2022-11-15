import re
from setuptools import setup

version = '1.0.0'


requirements = ['requests', 'beautifulsoup4']
    


readme = 'Simple youtube search.'
with open('README.md', encoding="utf8") as f:
    readme = f.read()

setup(
    name='YouTubeSearch',
    author='xenmods',
    author_email='ilumomin04@gmail.com',
    version=version,
    long_description=readme,
    url='https://github.com/xenmods/YouTubeSearch',
    packages=['YouTubeSearch'],
    license='GNU General Public License v3.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Build Tools",

    ],
    description='YouTube Search in python.',
    include_package_data=True,
    keywords=['youtube', 'search', 'python', 'videos', 'scraping',
              'bs4'],
    install_requires=requirements
)