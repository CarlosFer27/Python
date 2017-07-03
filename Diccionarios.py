Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> mi_diccionario = {'clave_1':'Fer', 'clave_2':'te amo'}
>>> print(mi_diccionario['clave_1'])
Fer
>>> mi_diccionario['clave_2'] = 'HezGaleana'
>>> print(mi_diccionario)
{'clave_1': 'Fer', 'clave_2': 'HezGaleana'}
>>> del(mi_diccionario['clave_2']) # eliminando claves
>>> print (mi_diccionario)
{'clave_1': 'Fer'}
>>> mi_diccionario.values
<built-in method values of dict object at 0x0328E630>
>>> 
