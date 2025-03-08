from setuptools import setup

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding='UTF-8') as fh:
    requirements = fh.read().split("\n")

setup(
    name="bingcnsearch-python",
    version="1.0.0",
    author="Tian",
    author_email="tianxuan911@aliyun.com",
    description="A Python library for scraping the cn.bing.com search engine.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tianxuan911/bingcnsearch",
    packages=["bingcnsearch"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[requirements],
    include_package_data=True,
)
