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

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[('my_data', ['data/mockResponse.json'])],  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        'console_scripts': [
            'metripoll=metripoll:runnable',
        ],
    },
)