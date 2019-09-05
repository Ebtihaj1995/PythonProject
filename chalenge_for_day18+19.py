Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> list=["Nada","Asma","Amal","Ebtihaj","Munirah",1,2,3,4,5]
>>> print(list.append("Abdullah"))
None
>>> print(list)
['Nada', 'Asma', 'Amal', 'Ebtihaj', 'Munirah', 1, 2, 3, 4, 5, 'Abdullah']
>>> list_2=list.copy()
>>> print(list_2)
['Nada', 'Asma', 'Amal', 'Ebtihaj', 'Munirah', 1, 2, 3, 4, 5, 'Abdullah']
>>> list.clear()
>>> print(list)
[]
>>> list_2.reverse()
>>> print(list_2)
['Abdullah', 5, 4, 3, 2, 1, 'Munirah', 'Ebtihaj', 'Amal', 'Asma', 'Nada']
>>> list_2.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'int' and 'str'
>>> print(list_2)
['Abdullah', 5, 4, 3, 2, 1, 'Munirah', 'Ebtihaj', 'Amal', 'Asma', 'Nada']
>>> list_2.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'int' and 'str'
>>> list_2.pop(0)
'Abdullah'
>>> list_2.insert(2,5)
>>> print(list_2)
[5, 4, 5, 3, 2, 1, 'Munirah', 'Ebtihaj', 'Amal', 'Asma', 'Nada']
>>> tuple=("java","python","swift")
>>> if "python" in tuple :{
... print("Yes , 'python' is in the lan tuple")}
...
Yes , 'python' is in the lan tuple
{None}
>>>
