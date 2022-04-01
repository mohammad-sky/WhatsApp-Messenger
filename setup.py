from os import path
from setuptools import setup

# read the contents of your description file

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="WhatsApp-Messenger",
    version="1",
    description="Send files to a large number of WhatsApp users",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sepehrmizani/WhatsApp-Messenger",
    author="sepehr",
    author_email="m.sepehr.mizani@gmail.com",
    license="MIT",
    packages=["WhatsApp-Messenger"],
    keywords=[
        "WhatsApp-Messenger",
        "python-whatsapp",
        "WhatsApp",
        "Messenger",
    ],
    install_requires=[
        "selenium",
        "webdriver-manager",
        "alright",
    ],
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
