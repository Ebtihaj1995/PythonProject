Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> x=5
>>> y="Ebtihaj"
>>> print(x)
5
>>> print(y)
Ebtihaj
>>> x=4 #x is of type int
>>> x="Salary" # x is now of type str
>>> print(x)
Salary
>>> x="Ebtihaj"
>>> # is the same as
... x='Ebtihaj'
>>> print(x)
Ebtihaj
>>> x="Ebtihaj"
>>> #double quotes are the same as single quotes:
... x= 'Ebtihaj'
>>> print(x)
Ebtihaj
>>> x,y,z="Orange", "Banana", "Cherry"
>>> print(x)
Orange
>>> print(y)
Banana
>>> print(z)
Cherry
>>> x=y=z="Orange"
>>> print(x,y,z)
Orange Orange Orange
>>> x="awesome"
>>> print("Python is "+ x)
Python is awesome
>>> x="awesome"
>>> y="Python is ""
  File "<stdin>", line 1
    y="Python is ""
                  ^
SyntaxError: EOL while scanning string literal
>>> y="Python is "
>>> z= y+x
>>> print(z)
Python is awesome
>>> x=5
>>> y=10
>>> print(x+y)
15
>>> x=5
>>> y="John"
>>> print(x+y)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
