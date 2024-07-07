from setuptools import setup, find_packages

setup(
    name='bubble_citations',
    version='1.0.0',
    author='Stefan Faaland',
    author_email='stefan.faaland@gmail.com',
    description='yeehaw',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)