from setuptools import setup, find_packages

setup(
    name="number-guessing",
    version="0.1.0",
    description="A CLI Number Guessing Game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="NguyenDong",
    author_email="doannguyendong1808@gmail.com",
    url="https://github.com/ndongdoan/Number-Guessing",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "tabulate",
    ],
    entry_points={
        "console_scripts": [
            "game=number_guessing_game.game:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.6"
)