Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> thistuple=("apple","banana","cherry")
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> thistuple=()
>>> print(thistuple)
()
>>> thistuple=(3,)
>>> print(thistuple)
(3,)
>>> thistuple=(3,1.3,4.1,7)
>>> print(thistuple)
(3, 1.3, 4.1, 7)
>>> thistuple=("Ahmad",1.1,4,"Python")
>>> print(thistuple)
('Ahmad', 1.1, 4, 'Python')
>>> thistuple=("apple","banana","cherry")
>>> print(thistuple[1])
banana
>>> thistuple=("apple","banana","cherry")
>>> for x in thistuple: {
... print(x) }
...
apple
{None}
banana
{None}
cherry
{None}
>>> thistuple[3]="orange"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> thistuple=("apple","banana","cherry")
>>> del thistuple
>>> print(thistuple)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'thistuple' is not defined
>>> thistuple=("apple","banana","cherry")
>>> print(thistuple[0:3])
('apple', 'banana', 'cherry')
>>>
