from setuptools import find_packages, setup

setup(
    name="py3cw-aio",
    version="0.0.1",

    description="Asynchronous 3Commas Python wrapper",

    url="https://github.com/cyberjunky/py3cw-aio",

    author="Ron Klinkien",
    author_email="ron@cyberjunky.nl",

    license="MIT",

    classifiers=[
        "Development Status :: 5 - Production/Stable"
    ],

    keywords="api 3Commas trading crypto bitcoin altcoin dca bots",

    packages=find_packages(exclude=["tests"]),

    install_requires=[
        "aiohttp >= 3.6",
    ],
)
