import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='maka',
    version='0.0.1',
    author='SLAPaper',
    author_email='slapaper.pku@gmail.com',
    description='Python port of Microsoft Academic Knowledge API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/PKU-Dragon-Team/maka',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
)
