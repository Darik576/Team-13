from setuptools import setup, find_packages

setup(
    name="assistant-bot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'assistant-bot = assignment1.main:main',
        ],
    },
)