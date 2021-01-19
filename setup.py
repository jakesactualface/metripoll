from setuptools import setup

setup(
    name='metripoll',
    version='0.0.1',
    description='A Python program for polling JSON metrics',
    url='https://github.com/jakesactualface/metripoll',
    author='Jake Everhart',
    author_email='jake.a.everhart@gmail.com',
    packages=['metripoll', 'metripoll.library'],
    python_requires='>=3.6, <4',
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'metripoll=metripoll:runnable',
        ],
    },
)