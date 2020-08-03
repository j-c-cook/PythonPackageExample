# PythonPackageExample
A simple example of a python package

# Usage
## Build in Place
During development, you may want to build the project in place.
Building in place is necessary for `Cython` and any uncompiled `C++`
associated files.  
```
python setup.py build_ext --inplace
```

## Pip Install
In `Python`, you regularly make use of packages. Common packages you may have
used are `numpy`, `scipy`, `coolprop`, etc. These pacakges are installed to a 
pip located in a specific virtual environment. You can make your package
available to be installed without the source code by posting your package 
on  <a href="https://pypi.org/">PyPi</a>. Or if you have the parent directory 
zipped up, you can install by the following. 
```
pip install <path/to/package.zip>
``` 
