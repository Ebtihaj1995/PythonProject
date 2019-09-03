Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> age = 36
>>> txt="My name is Ebtihaj, I am " + age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> print(txt)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'txt' is not defined
>>> age=36
>>> txt="My name is Ebtihaj, I am {}"
>>> print(txt.format(age))
My name is Ebtihaj, I am 36
>>> quantity=3
>>> itemon=567
>>> price=49.95
>>> myorder="I want {} pieces of item {} for {} dollars."
>>> print(myorder.format(quantity, itemon, price))
I want 3 pieces of item 567 for 49.95 dollars.
>>> myorder="I want {2} pieces of item {0} for {1} dollars."
>>> print(myorder.format(quantity, itemon, price))
I want 49.95 pieces of item 3 for 567 dollars.
>>>
