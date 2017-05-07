import os
from setuptools import setup

# Set external files
README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='vape',
    version='0.1.0',
    packages=['vape'],
    install_requires=required,
    include_package_data=True,
    license='MIT License',
    description='Command line aesthetic generator.',
    long_description=README,
    url='https://github.com/Miserlou/Vape',
    author='Rich Jones',
    author_email='rich@openwatch.net',
    entry_points={
        'console_scripts': [
            'vape= vape.__init__:command_line_runner',
        ]
    },
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
