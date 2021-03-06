import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CLTviz",
    version="0.0.1",
    author="Herumb Shandilya",
    author_email="herumbshandilya123@gmail.com",
    description="Central Limit Theorem Playground",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krypticmouse/CLTviz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
