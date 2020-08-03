# PythonPackageExample
A minimal package including various aspects: 
- Installing to pip ([setup.py](setup.py))
- Including Non-Python files ([MANIFEST.in](MANIFEST.in))
- Building with Cython ([pyproject.toml](pyproject.toml))
- Requirements for the project ([requirements.txt](requirements.txt))

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
## Post Installation
If you do `pip install` this package, then you can list off all the packages you
now have in your `pip`.
```
pip list
```
provides me with the following after installing:
```
Package              Version
-------------------- -------
CoolProp             6.3.0  
pip                  19.2.3 
Package              0.0.1  
setuptools           41.2.0
``` 

# Comments
Given that this is completely public, enforcing citation is near impossible.
However, open source software is making the world a better place for all people, so 
I post this here and leave it up to your moral compass as what in this work 
you will decide to cite. Additionally, most of what is here is neither new nor 
ground breaking. This example repository does provide a more in depth 
example of the features available for Python packaging in a more simple 
presentation than I have ever seen. Dissecting numpy may provide some 
insight, but it is also a fairly complex example. 
