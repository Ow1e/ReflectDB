# ReflectDB   
## NOTE: DONT USE THIS, USE [SAILDB](https://github.com/Ow1e/SailDB) INSTEAD
![PyPI - Downloads](https://img.shields.io/pypi/dw/reflectdb?style=flat-square) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/reflectdb?style=flat-square) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/reflectdb?style=flat-square) [![GitHub license](https://img.shields.io/github/license/Ow1e/ReflectDB?style=flat-square)](https://github.com/Ow1e/ReflectDB/blob/master/LICENSE) [![GitHub issues](https://img.shields.io/github/issues/Ow1e/ReflectDB?style=flat-square)](https://github.com/Ow1e/ReflectDB/issues)  
A fast storage based database solution 

## Benchmarks
### Experimental Mode Benchmarks
 - 9975 items a second on 2017 MacBook Flash Storage (Random Num (1, 100000), Date (Datetime.now), name (String128 CONSTANT), email(String128 CONSTANT))
### Seperate Mode
- 2769 items a second on 2017 MacBook Flash Storage (Random Num (1, 100000), Date (Datetime.now), name (String128 CONSTANT), email(String128 CONSTANT))
### Bundled Mode 
- 358 items a second on 2017 MacBook Flash Storage (Random Num (1, 100000), Date (Datetime.now), name (String128 CONSTANT), email(String128 CONSTANT))

# Install
## Using Pip
```
pip install reflectdb
```
## Install via setup
```
git clone https://github.com/Ow1e/ReflectDB
cd ReflectDB
python3 setup.py install
```
## Upload to PyPi
(For contributers only)
```
python3 setup.py bdist_wheel 
twine upload dist/* 
```
