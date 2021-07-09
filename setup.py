# Jack C. Cook
# August 2, 2020

from setuptools import setup
from setuptools.extension import Extension
import numpy as np
from Cython.Distutils import build_ext

# Cython extensions
extensions = [
    Extension(
        name='Package.helloworld',  # this will become <name>.so
        sources=['Package/helloworld.pyx'],  # a list of the cython and cpp files
        include_dirs=[np.get_include()],
    )
]

setup(name='Package',
      version='0.0.1',
      packages=['Package'],
      install_requires=['coolprop',
                        'numpy',
                        'Cython'],
      include_package_data=True,
      ext_modules=extensions,
      cmdclass={'build_ext': build_ext},
      author='Jack C. Cook',
      author_email='jack.cook@okstate.edu',
      description='an example python package')
