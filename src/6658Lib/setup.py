from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'FRC team 6658 codebase'
LONG_DESCRIPTION = 'A package containing code used for FRC team 6658'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="6658Lib", 
        version=VERSION,
        author="entityJY",
        author_email="<jomathya07@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'frc'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)