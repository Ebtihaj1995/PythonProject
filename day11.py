Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> x=5
>>> print(x>3 or x<4)
True
>>> x=["apple","banana"]
>>> y=["apple","banana"]
>>> z=x
>>> print(x is not z)
False
>>> #return false because z is the same object as x
...
>>> print(x is not y)
True
>>> #return true because x is not the same object as y
... #even if they have the same content
...
>>> print (x!=y)
False
>>> #to demostrate the difference between "is not" and "!=":
... #this comparison returns false because x is equal to y
...
>>> x == y
True
>>> x==y and x==z
True
>>> x=["apple","banana"]
>>> print("banana" in x)
True
>>>
