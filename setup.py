from setuptools import setup, find_packages

setup(
    name='webpall',  
    version='0.1.1',  
    description='Convert JPG and PNG images in a folder to WebP format with selective options.',
    author='Rishikesh Sreehari',
    author_email='contact@rishikeshs.com',  
    packages=find_packages(),
    install_requires=['Pillow'],
    entry_points={
        'console_scripts': [
            'webpall=webpall.converter:main',  # Entry point for the command-line tool
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
