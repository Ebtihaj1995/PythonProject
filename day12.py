Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> s=" Please, I want {} sandwishes and {} donutes "
>>> print(s.replace("I","We"))
 Please, We want {} sandwishes and {} donutes
>>> x=5
>>> y=7
>>> print(s.format(x,y))
 Please, I want 5 sandwishes and 7 donutes
>>> print(s.replace("a","A"))
 PleAse, I wAnt {} sAndwishes And {} donutes
>>>
