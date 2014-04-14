"""Setup for twenty_fourty_eight XBlock."""

import os
from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='twenty_fourty_eight-xblock',
    version='0.1',
    description='twenty_fourty_eight XBlock',   # TODO: write a better description.
    packages=[
        'twenty_fourty_eight',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'twenty_fourty_eight = twenty_fourty_eight:TwentyFourtyEightXBlock',
        ]
    },
    package_data=package_data("twenty_fourty_eight", "static"),
)