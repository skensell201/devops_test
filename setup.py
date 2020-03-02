import pathlib
import re
import sys
from datetime import datetime
from setuptools import setup


if not sys.version_info >= (3, 8):
    raise RuntimeError("doesn't support Python earlier than 3.8")


HERE = pathlib.Path(__file__).parent
PACKAGE_NAME = "package"
BUILD = datetime.now().strftime('%y%m%d%H%M')


try:
    version = re.findall(
        r'^__version__ = "([^"]+)"\n?$',
        (HERE / PACKAGE_NAME / "__init__.py").read_text("utf8"),
        re.M
    )[0]
except IndexError:
    raise RuntimeError("Unable to determine version")


install_requires = [
    req.strip().strip("\r")
    for req in (HERE / "requirements" / "production.txt").read_text("utf8").split("\n")
]

f = open(f"{PACKAGE_NAME}/build_info", "w")
try:
            f.write(BUILD)
finally:
            f.close()

setup(
    name=PACKAGE_NAME,
    version=f"{version}.{BUILD}",
    classifiers=[
          "Programming Language :: Python :: 3.8",
          "Framework :: AsyncIO",
    ],
    python_requires=">=3.8",
    packages=[PACKAGE_NAME],
    install_requires=install_requires,
    include_package_data=True
)
