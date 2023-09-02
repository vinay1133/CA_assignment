from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bytenba/__init__.py
from bytenba import __version__ as version

setup(
	name="bytenba",
	version=version,
	description="ERP for Clg",
	author="byte_team",
	author_email="ishaanmapte@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
