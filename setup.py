import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scvf",
    version="0.0.39",
    author="Spikes#2212",
    author_email="spikesno2212@gmail.com",
    description="a framework that wraps opencv for our needs in FRC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Spikes-2212-Programming-Guild/SpikesCVFramework",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
