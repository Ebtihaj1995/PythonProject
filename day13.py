Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> s=[]
>>> print(s)
[]
>>> numbers=[1,2,3,4,5]
>>> print(numbers)
[1, 2, 3, 4, 5]
>>> thislist=["apple","banana","cherry"]
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> thislist="apple","banana","cherry",1,2,3]
>>> thislist=["apple","banana","cherry",1,2,3]
>>> print(thislist)
['apple', 'banana', 'cherry', 1, 2, 3]
>>> floatlist=[2.3,5.7,9.0,7.1]
>>> print(floatlist)
[2.3, 5.7, 9.0, 7.1]
>>> print(thislist[1])
banana
>>> thislist=["apple","banana","cherry"]
>>> for x in thislist :{
... print(x)}
...
apple
{None}
banana
{None}
cherry
{None}
>>> for x in floatlist : {
... print (x)}
...
2.3
{None}
5.7
{None}
9.0
{None}
7.1
{None}
>>> thislist=["apple","banana","cherry"]
>>> thislist[1]="blackcurrant"
>>> print(thislist)
['apple', 'blackcurrant', 'cherry']
>>> thislist=["apple","banana","cherry"]
>>> del thislist[0]
>>> print(thislist)
['banana', 'cherry']
>>> thislist=["apple","banana","cherry"]
>>> del thislist
>>> print(thislist)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'thislist' is not defined
>>> thislist=["A","B","C","D","E"]
>>> print(thislist)
['A', 'B', 'C', 'D', 'E']
>>> del thislist[0]
>>> del thislist[1]
>>> print(thislist)
['B', 'D', 'E']
>>>
