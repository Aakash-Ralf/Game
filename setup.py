from setuptools import setup, find_packages

setup(
    name="python-clicker-game",
    version="1.0.0",
    description="A simple clicker game with a Flask backend",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "pygame",
        "flask",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "run-game=game:main",
            "run-server=server:main"
        ]
    }
)

