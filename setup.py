"""Package setup file"""
from typing import List

from setuptools import find_packages
from setuptools import setup

from biodatasets import ROOT_DIRECTORY
from biodatasets.version import VERSION

README = (ROOT_DIRECTORY / "README.md").read_text()


def read_requirements() -> List:
    with open("requirements.txt", "r+") as file:
        req = file.readlines()
    requirements = [pkg.replace("\n", "") for pkg in req]

    return requirements


DESCRIPTION = "Open-source collection of biology datasets and pre-trained embeddings."


def make_install():
    """main install function"""

    setup_fn = setup(
        name="bio-datasets",
        license="Apache-2.0",
        version=VERSION,
        description=DESCRIPTION,
        author="InstaDeep",
        long_description=README,
        long_description_content_type="text/markdown",
        url="https://github.com/DeepChainBio/datasets",
        author_email="a.delfosse@instadeep.com",
        packages=find_packages(exclude=["test"]),
        classifiers=[
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.7",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Scientific/Engineering :: Bio-Informatics",
            "Topic :: Software Development",
        ],
        install_requires=read_requirements(),
        include_package_data=True,
        zip_safe=False,
        python_requires=">=3.7",
    )

    return setup_fn


if __name__ == "__main__":
    make_install()
