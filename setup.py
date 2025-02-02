#!/usr/bin/env python
from pathlib import Path

from setuptools import find_packages, setup

extras_require = {
    "test": [
        "cryptography",
        "pytest-cov",
        "pytest-django",
        "pytest-xdist",
        "pytest",
        "tox",
    ],
    "lint": [
        "flake8",
        "pep8",
        "isort",
    ],
    "doc": [
        "Sphinx>=1.6.5,<2",
        "sphinx_rtd_theme>=0.1.9",
    ],
    "dev": [
        "pytest-watch",
        "wheel",
        "twine",
        "ipython",
    ],
    "python-jose": [
        "python-jose==3.3.0",
    ],
    "crypto": [
        "cryptography>=3.3.1",
    ],
}

extras_require["dev"] = (
    extras_require["dev"]
    + extras_require["test"]
    + extras_require["lint"]
    + extras_require["doc"]
    + extras_require["python-jose"]
)


setup(
    name="djrestframework_simplejwt",
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
    url="https://github.com/mowarlee/djangorestframework-simplejwt",
    license="MIT",
    description="A minimal JSON Web Token authentication plugin for Django REST Framework",
    long_description=Path("README.rst").read_text(encoding="utf-8"),
    author="Mewar Lee",
    author_email="leemowar@gmail.com",
    install_requires=[
        "django>=4.0",
        "djrestframework>=5.12",
        "pyjwt>=1.7.1,<3",
    ],
    python_requires=">=3.7",
    extras_require=extras_require,
    packages=find_packages(exclude=["tests", "tests.*", "licenses", "requirements"]),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
