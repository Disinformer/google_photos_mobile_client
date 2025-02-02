from setuptools import find_packages, setup

setup(
    name="gpmc",
    version="0.5.1",
    python_requires=">=3.10",
    description="Reverse engineered Google Photos mobile API client",
    author="Disinformer",
    url="https://github.com/Disinformer/gphotos_mobile_client",
    packages=find_packages(),
    install_requires=[
        "bbpb",
        "rich",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "gp-upload = gpmc.cli:main",
            "gpmc = gpmc.cli:main",
        ]
    },
)
