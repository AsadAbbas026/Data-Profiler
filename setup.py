# setup.py

from setuptools import setup, find_packages

setup(
    name='data_profiler',
    version='0.1.0',
    author='Your Name',
    author_email='your_email@example.com',
    description='A package for data profiling and anomaly detection',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0',
        'scipy>=1.5'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
)
