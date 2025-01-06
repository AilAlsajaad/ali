from setuptools import setup, find_packages

setup(
    name="mysbus",
    version="0.1.0",
    description="SBUS decoding library for Raspberry Pi / Linux",
    author="You & ChatGPT",
    packages=find_packages(),
    install_requires=[
        "pyserial",
        "pigpio"
    ],
    python_requires='>=3.6',
)
