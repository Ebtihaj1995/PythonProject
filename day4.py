Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> x=1
>>> y=2.8
>>> z=lj
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'lj' is not defined
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'float'>
>>> print(typr(z))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'typr' is not defined
>>> z=1j
>>> print(type(z))
<class 'complex'>
>>> x=1
>>> y=35656222554887711
>>> z=-3255522
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'int'>
>>> print(type(z))
<class 'int'>
>>> x=1.10
>>> y=1.0
>>> z=-35.59
>>> print(type(x)
... print(type(x))
  File "<stdin>", line 2
    print(type(x))
        ^
SyntaxError: invalid syntax
>>> print(type(x))
<class 'float'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'float'>
>>> x=35e3
>>> y=12E4
>>> z=-87.7e100
>>> print(type(x))
<class 'float'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'float'>
>>> x=3+5j
>>> y=5j
>>> z=-5j
>>> print(type(x))
<class 'complex'>
>>> print(type(y))
<class 'complex'>
>>> print(type(z))
<class 'complex'>
>>> x=1
>>> y=2.8
>>> z=1j
>>> a=float(x)
>>> b=int(y)
>>> c=complex(x)
>>> print(a,b,c)
1.0 2 (1+0j)
>>> print(type(a,b,c))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: type.__new__() argument 1 must be str, not float
>>> print(type(a))
<class 'float'>
>>> print(type(b))
<class 'int'>
>>> print(type(c))
<class 'complex'>
>>> import random
>>> print(random.randrange(1,10))
2
>>> print(random.randrange(1,10))
2
>>> import random
>>> print(random.randrange(1,10))
1
>>> import random
>>> print(random.randrange(1,10))
2
>>> import random
>>> print(random.randrange(1,10))
8
>>>
