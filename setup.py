"""Python setup.py for tacl2025_ood_eval_self_rationalization package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("tacl2025_ood_eval_self_rationalization", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="tacl2025_ood_eval_self_rationalization",
    url="https://github.com/jingyng/tacl2025-ood-eval-self-rationalization/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="author_name",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["tacl2025_ood_eval_self_rationalization = tacl2025_ood_eval_self_rationalization.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-dev.txt")},
)
