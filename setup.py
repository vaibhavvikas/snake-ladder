#!/usr/bin/env python

"""The setup script."""

from pathlib import Path
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

project_dir = Path(__file__).parent

setup(
    author="Vaibhav Vikas",
    author_email='vbhvvikas@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    description="A python snake and ladder game for machine coding practice",
    install_requires=project_dir.joinpath('requirements.txt').read_text().split("\n"),
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='snake_ladder',
    name='snake_ladder',
    packages=find_packages(include=['snake_ladder', 'snake_ladder.*']),
    project_dir={"":"'snake_ladder'"},
    test_suite='tests',
    tests_require=project_dir.joinpath('requirements.txt').read_text().split("\n"),
    url='https://github.com/vaibhavvikas/snake_ladder',
    version='0.1.0',
    zip_safe=False,
)
