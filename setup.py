"""
Setup script for the AutoPicLabel project.
"""
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="autopiclabel",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "ollama",
        "argparse"
    ],
    entry_points={
        'console_scripts': [
            'autopiclabel=autopiclabel:main',
        ],
    },
    author="Cyril Moron",
    author_email="cyril.moron@gmail.com",
    description="A module to analyze images, generate descriptive names, and rename image files.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/cmoron/autopiclabel",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
