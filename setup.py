from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in knk_hr_esic_pf_challan_report/__init__.py
from knk_hr_esic_pf_challan_report import __version__ as version

setup(
	name="knk_hr_esic_pf_challan_report",
	version=version,
	description="A frappe custom addon to add option to generate ESIC report and PF Challan Report from ErpNext.",
	author="Kanak Infosystems LLP.",
	author_email="sales@kanakinfosystems.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
