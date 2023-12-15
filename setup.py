from setuptools import setup

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
   name = "python_artnet",
   author= "sciencegey",
   version= "1.0.0",
   license= "MIT",
   description= "Easy-to-use and simple python receiver for Art-Net (that also implements device polling).",
   long_description=long_description,
   long_description_content_type= "text/markdown",
   url= "https://github.com/sciencegey/python_artnet",
   
)