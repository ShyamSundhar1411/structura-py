from setuptools import find_packages, setup

setup(
    name="structura-py",
    version="0.1.0",
    description="A CLI for automated folder structure generation and dependency management for Python projects.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Shyam Sundhar",
    author_email="clashwithchiefrpjyt@gmail.com",
    url="https://github.com/ShyamSundhar1411/structura-py",
    packages=find_packages(where="src"),
    package_dir={"": "structura_py"},
    install_requires=[
        "typer",
        "pyyaml",
        "rich",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "structura=structura_py.cli:structura",
        ]
    },
)
