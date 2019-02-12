"""A setuptools based setup module for conda_demo."""


from os import path
# Always prefer setuptools over distutils
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))
NAME = 'conda_demo'

# Load the version
with open(path.join(HERE, NAME, 'version.py')) as version_file:
    exec(version_file.read())

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

REQUIREMENTS = [
    # Package requirements go here:
    'pyyaml',
]

TEST_REQUIREMENTS = [
    'pytest',
]

SETUP_REQUIREMENTS = [
    'pytest-runner',
]

setup(
    name=NAME,
    version=__version__,
    description='Demo of a tool written in Python and packaged by conda',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Baylor College of Medicine Human Genome Sequencing Center',
    author_email='questions@hgsc.bcm.edu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    setup_requires=SETUP_REQUIREMENTS,
    entry_points={
        'console_scripts': [
            'cdemo=conda_demo.cli:main',
        ],
    },
)
