Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> mi_lista = ['FER1', 27, 07, 2013,'FER5']
SyntaxError: invalid token
>>> mi_lista = ['FER1', 27, 7, 2013,'FER5']
>>> print (mi_lista[0:-1])
['FER1', 27, 7, 2013]
>>> mi_lista[1] = 'FER2'
>>> print (mi_lista[2])
7
>>> print (mi_lista[1])
FER2
>>> mi_lista.
SyntaxError: invalid syntax
>>> mi_lista.append('nueva Fer') # agregando un nuevo item a la lista
>>> print (mi_lista)
['FER1', 'FER2', 7, 2013, 'FER5', 'nueva Fer']
>>> l
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> len(mi_lista)
6
>>> len(mi_lista) # numero de elementos que tiene mi lista
6
>>> 
