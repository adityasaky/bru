import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="bru",
    version="0.0.1",
    author="Aditya Saky",
    author_email="aditya@saky.in",
    description="A package for all things Bru!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adityasaky/bru",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
