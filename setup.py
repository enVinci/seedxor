#!/usr/bin/env python
import setuptools

with open("README.md", "rt") as fh:
    long_description = fh.read()

setuptools.setup(
    name="seedxor",
    version="0.1.0",
    author="Adam P. Goucher",
    description="Implementation of Bitcoin BIP 85",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/apgoucher/hamming-backups",
    packages=setuptools.find_packages(),
    keywords=['SeedXOR', 'hamming', 'bitcoin'],
    install_requires=["mnemonic", "argparse"],
    python_requires=">=3.8.1",
    entry_points = {
        "console_scripts": ["seedxor=seedxor.cli:main"],
    },
)
