"""
SRU PIP
Special Reconnaissance Unit
-----------
python SRU
Link
`````
* Source
  https://github.com/abusaidm/
"""
from setuptools import setup

version = "0.1.3"

setup(
    name="sru_pip",
    version=version,
    author="Mohamed Abusaid",
    author_email="m.abusaid<at>yahoo<dot>com",
    packages=[
        "sru_pip",
        ],
    include_package_data=True,
    url="http://github.com/abusaidm/sru_pip/packages/{}/".format(version),

    # license="LICENSE.txt",
    description="sri_pip",
    # long_description=open("README.txt").read() or just """ lots of text here too""",
    # Dependent packages (distributions)
    dependency_links=[
        "https://github.com/abusaidm/pip_shim/tarball/master#egg=pip_shim-0.1.1"
    ],
    install_requires=[
        "pip_shim==0.1.1"
    ],
)