from setuptools import setup
from freecad.ipython_integration import __version__
# name: this is the name pip is using.
# Packages using the same name here cannot be installed together

setup(name='freecad-ipython',
      version=str(__version__),
      packages=['freecad',
                'freecad.ipython_integration'],
      maintainer="looooo",
      maintainer_email="sppedflyer@gmail.com",
      url="https://github.com/looooo/freecad-spyder",
      description="integrating qt-console of ipython into freecad",
      install_requires=[],
include_package_data=True)