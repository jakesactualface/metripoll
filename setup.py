from setuptools import setup, find_packages

setup(
    name="metripoll",
    description="A Python program for polling JSON metrics",
    author="Jake Everhart",
    url="https://github.com/jakesactualface/metripoll",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["requests", "argparse"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'metripoll=metripoll.__main__:main',
        ],
    }
)
