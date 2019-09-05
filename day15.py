Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> thislist=["apple","banana","cherry"]
>>> print(len(thislist))
3
>>> thislist.append("orange")
>>> print(thislist)
['apple', 'banana', 'cherry', 'orange']
>>> thislist.insert(1,"orange")
>>> print(thislist)
['apple', 'orange', 'banana', 'cherry', 'orange']
>>> thislist.remove("banana")
>>> print(thislist)
['apple', 'orange', 'cherry', 'orange']
>>> thislist=["apple","banana","cherry"]'
  File "<stdin>", line 1
    thislist=["apple","banana","cherry"]'
                                        ^
SyntaxError: EOL while scanning string literal
>>> thislist=["apple","banana","cherry"]
>>> thislist.remove("banana")
>>> print(thislist)
['apple', 'cherry']
>>> thislist=["apple","banana","cherry"]
>>> thislist.pop()
'cherry'
>>> print(thislist)
['apple', 'banana']
>>> thislist=["apple","banana","cherry"]
>>> thislist.pop[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> thislist.pop(1)
'banana'
>>> print(thislist)
['apple', 'cherry']
>>> thislist=["apple","banana","cherry"]
>>> thislist.clear()
>>> print(thislist)
[]
>>> thislist=["apple","banana","cherry"]
>>> mylist=thislist.copy()
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> thislist=["apple","banana","cherry"]
>>> mylist=thislist.copy()
>>> thislist.pop(0)
'apple'
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> print(thislist)
['banana', 'cherry']
>>> thislist=["Amal","Ebtihaj","Munirah"]
>>> mylist=thislist
>>> thislist.pop(0)
'Amal'
>>> print(mylist)
['Ebtihaj', 'Munirah']
>>> print(thislist)
['Ebtihaj', 'Munirah']
>>> thislist=["apple","banana","cherry"]
>>> mylist=list(thislist)
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> thislist=list(("apple","banana","cherry"))
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> thislist=["apple","banana","cherry"]
>>> thistlist.append("orange")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'thistlist' is not defined
>>> thislist=["apple","banana","cherry"]
>>> thislist.append("orange")
>>> print(thislist)
['apple', 'banana', 'cherry', 'orange']
>>> s=thislist.copy()
>>> print(s)
['apple', 'banana', 'cherry', 'orange']
>>> thislist.clear()
>>> print(thislist)
[]
>>> thislist.reverse()
>>> print(thislist)
[]
>>> thislist=["apple","banana","cherry"]
>>> thislist.reverse()
>>> print(thislist)
['cherry', 'banana', 'apple']
>>> thislist.sort()
>>> print(thislist)
['apple', 'banana', 'cherry']
