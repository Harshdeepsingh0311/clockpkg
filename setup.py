from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.20.21'

# Setting up
setup(
    name="clockpkg",
    version=VERSION,
    author="Harshdeep Singh",
    author_email="harshdeepsinghbakshi2005@gmail.com",
    description='Simple package to make an analog clock.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['clock', 'python', 'clockmaker', 'myclock'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
