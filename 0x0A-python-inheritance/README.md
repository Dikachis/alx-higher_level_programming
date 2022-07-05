# 0x0A. Python - Inheritance
To know more about class, object or instance, and isinstance
## Introduction/Objectives
* To know what a superclass, baseclass or parentclass is
* To know what subclass is
* To know how to list all attributes and methods of a class or instance
* To know when an instance can have new attributes
* To know how to inherit class from another
* To know how to define a class with multiple base classes
* To know what the default class that every class inherit from is
* To know how to override a method or attribute inherited from the base class
* To know which attributes or methods are available by heritage to subclasses
* To know the purpose of inheritance
* To know what are, when and how to use ``isinstance``, ``issubclass``, ``type`` and ``super`` built-in functions

### Resources
* [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance) || [Multiple Inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance) || [Inheritance in python](https://www.packt.com/inheritance-python/) || [Inheritance Magic Methods ](https://www.youtube.com/watch?v=d8kCdLCi6Lk) etc.

## General Requirements
**Python Script:**
* Allowed editors: **vi**, **vim**, **emacs**
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files ends with a new line
* Python Scripts: The first line of all your files should be exactly **#!/usr/bin/python3**
* There is a **README.md** file, at the root of the folder of the project
* All files are executable
* All coded used the pycodestyle (version 2.8.*)*

**Python Test Cases:**
* Allowed editors: **vi**, **vim**, **emacs**
* All files ends with a new line
* All test files are inside a folder tests
* All test files are text files with extension: ``.txt``)
* All tests are executed using the command: ``python3 -m doctest ./tests/*``
* All the modules have a documentation ``(python3 -c 'print(__import__("my_module").__doc__)')``
* All functions have a documentation (``python3 -c 'print(__import__("my_module").my_function.__doc__)'`` and <br> ``python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'``)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!


## List of files and description:
| S/N   |       Files          |        Description  |
|:-----:|:--------------------:|:-------------------|
|1. | [0-lookup.py](https://github.com/Dikachis/alx-higher_level_programming/blob/master/0x0A-python-inheritance/0-lookup.py) | A function that returns the list of available attributes and methods of an object: |
|2. | [1-my_list.py](https://github.com/Dikachis/alx-higher_level_programming/blob/master/0x0A-python-inheritance/1-my_list.py) <br> [tests/1-my_list.txt](https://github.com/Dikachis/alx-higher_level_programming/tree/master/0x0A-python-inheritance/tests)| To write a class ``MyList`` that inherits from ``list``:|
|3. | [2-is_same_class.py](https://github.com/Dikachis/alx-higher_level_programming/blob/master/0x0A-python-inheritance/2-is_same_class.py) | A function that returns ``True`` if the object is exactly an instance of the specified class ; otherwise ``False``. |
|4. | [3-is_kind_of_class.py](https://github.com/Dikachis/alx-higher_level_programming/blob/master/0x0A-python-inheritance/3-is_kind_of_class.py) | A function that returns ``True`` if the object is an instance of, or <br> if the object is an instance of a class that inherited from, the specified class ; otherwise ``False``. |
|5. | [4-inherits_from.py](https://github.com/Dikachis/alx-higher_level_programming/blob/master/0x0A-python-inheritance/4-inherits_from.py) | A function that returns ``True`` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise ``False``. |
|6. | [6-base_geometry.py](https://github.com/Dikachis/alx-higher_level_programming/blob/master/0x0A-python-inheritance/6-base_geometry.py) | A class BaseGeometry (based on 5-base_geometry.py).: |
|7. | [7-base_geometry.py](https://github.com/Dikachis/alx-higher_level_programming/blob/master/0x0A-python-inheritance/7-base_geometry.py) | A class ``BaseGeometry`` (based on ``6-base_geometry.py``). |
