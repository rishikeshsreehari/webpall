from setuptools import setup, find_packages
from pathlib import Path

# Read the README file for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='webpall',
    version='0.1.2',
    description='Convert JPG and PNG images in a folder to WebP format with selective options.',
    long_description=long_description,  
    long_description_content_type="text/markdown",  
    author='Rishikesh Sreehari',
    author_email='contact@rishikeshs.com',
    packages=find_packages(),
    install_requires=['Pillow'],
    entry_points={
        'console_scripts': [
            'webpall=webpall.converter:main',  
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
