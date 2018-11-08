from setuptools import setup
import os

version_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 
                            "freecad", "ipython", "version.py")
with open(version_path) as fp:
    exec(fp.read())


setup(name='freecad.ipython',
      version=str(__version__),
      packages=['freecad',
                'freecad.ipython'],
      maintainer="looooo",
      maintainer_email="sppedflyer@gmail.com",
      url="https://github.com/looooo/freecad-spyder",
      description="integrating qt-console of ipython into freecad",
      install_requires=[],
include_package_data=True)