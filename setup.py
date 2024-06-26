from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Keywords
keywords = [
    "file",
    "hash",
    "hashing",
    "checksum",
    "algorithm",
    "md5",
    "sha1",
    "sha256",
    "sha512",
]


setup(
    name="HashGenerator",
    version="1.0.0",
    description="A simple file hash calculator supporting multiple algorithms",
    author="LpCodes",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/LpCodes/HashGenerator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    keywords=keywords,
    install_requires=[
        "hashlib",
        "pytest",
    ],
)
