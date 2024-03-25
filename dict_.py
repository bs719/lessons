'=====================словари==================='
# dict - изменяемый, итерируемый, неупорядочный (псевдопорядок)тип данных, для хранения данных в парах{ключь:значение}

#user = {'name':'Anonym', 'age':30, 'last_name':'Makers'}
#print(user['name']) #Anonym
#print(user['age']) #30
#print(user['last_name']) #Makers

# ключами в словаре могут быть не изменяемые типы данных
# ключи в словарях должны быть уникальным

'=========================создание словарей========================'
#dict_ = {'a':1, 'b':1}
#dict_ = dict({('a',1),('b',2)})
#print(dict_)
#dict_ = dict(['a1', 'b2', 'c3'])
#print(dict_) 

#dict_ = {}
#dict_['name'] = 'makers'
#dict_['age'] = 50  
#dict_['last_name'] = 'bootcamp'
#print(dict_)     


'===================================Методы словаря========================='


'get - метод который получает значения по ключу если указанного ключа нет выходит None-по по умолчанию можем его поменять'

#user = {'name':'Anonym', 
 #   'age':15, 
  #  'last_name':'Makers'}
#print(user.get('nam'))
#print(user.get('id', 'Такого ключа нету'))

#pop - удаляет пару по ключу и возвращает значение

# dict_ = {'a':1, 'b':2, 'c':3}
# popped = dict_.pop('b')
# print(dict_)
# print(popped)               

# #{'a': 1, 'c': 3}
#2


'popiten - удаляет последнюю пару и возвращает ee'
# dict_ = {'a':1, 'b':2, 'c':3}
# popped = dict_.popitem()
# print(dict_)                 # {'a':1, 'b':2}

'update - расшираяет словарь парами из второго словаря'

#dict_1 = {1:'a', 2:'a'}
#dict_2 = {2:'b', 3:'b'}
#dict_1.update(dict_2)
#print(dict_1) #{1: 'a', 2: 'b', 3: 'b'}

'clear - очищает словарь'
#dict_ = {'a':1, 'b':2, 'c':3}
#dict_.clear()
#print(dict_)#{}

'fromkeays - метод для создания нового словаря ипользуя список новых'
#dict_ = dict.fromkeys('hi')
#print(dict_)
#dict_2 = dict.fromkeys(['hi', 123, True], 0)
#print(dict_2) #{'hi': 0, 123: 0, True: 0}

'keys, valus, items'
#keys - метод который возвращает все ключи
#valus - метод который возвращает все значения
#items - метод который возвращает пары ключа и значение в виде tuple

#user = {
   # 'name':'Anonym',
    #'age':15,
    #'last_name':'Makers'
#}

#print(user.keys()) #dict_keys(['name', 'age', 'last_name'])
#print(user.values()) #dict_values(['Anonym', 15, 'Makers'])
#print(user.items()) #dict_items([('name', 'Anonym'), ('age', 15), ('last_name', 'Makers')])

'===============================итерирование словарей======================'
# user = {
    # 'name':'Anonym',
    # 'age':15,
    # 'last_name':'Makers'
# }
# 
# for i in user:
    # print(i) # приходит ключ
# 
# for valuse in user.values():
    # print(valuse) #приходит значения
# 
# for item in user.items():
    # print(item) #приходит tuple с ключем и значениям
# 
# '------------------------------------------------------'
# dict_1 = {1:'a', 2:'b'}
# dict_2 = {}
# for a, b in dict_1.items():
    # dict_2[b] = a
    # print(dict_2)

'poitem - удаляет последнюю пару и возвращает ее'

# dict_ = {'a':1, 'b':2, 'c':3}
# popped = dict_.popitem()
# print(dict_, popped)

'update - расширяет словарь парами из второго словаря'

# dict_1 = {1:'a', 2:'a'}
# dict_2 = {2:'b', 3:'b'}
# dict_1.update(dict_2)
# print(dict_1)    #{1:'a', 2:'b', 3:'b'}

'clear - очищает словарь'
# dict_ = {'a':1, 'b':2, 'c':3}
# dict_.clear()
# print(dict_)     #{}

'fromkeys - метод для создания нового словаря, используя список ключей'

# dict_ = dict.fromkeys('hi')
# print(dict_)       #{'h': None, 'i': None}

# dict_2 = dict.fromkeys(['hi', 123, True], 0)
# print(dict_2)      #{'hi': 0, 123: 0, True: 0}

'keys, values, items'
# keys - метод, который возвращает все ключи
# values - метод, который возыращает все значения
# items - метод, который возвращает пары ключ и значение в виде tuple

# user = {
    # 'name':'Anonym',
    # 'age':15,
    # 'last_name':'Makers'
# }
# print(user.keys())     #dict_keys(['name', 'age', 'last_name'])
# print(user.values())   #dict_values(['Anonym', 15, 'Makers'])
# print(user.items())    #dict_items([('name', 'Anonym'), ('age', 15), ('last_name', 'Makers')])


'============================Итерирование словарей=============================='

# user = {'name': 'Anonym',
        # 'age': 15,
        # 'last_name': 'Makers'
# }
#  
# for key in user:
    # print(key)
#при итерации словаря будут приходить ключи



# for value in user.values():
    # print(value)
#при итерации словаря с методом values(), приходят значения

# for item in user.items():
    # print(item)
#при итерации словаря с методом items(), приходят tuple с ключем и значением


# dict_1 = {1:'a', 2:'b'}
# dict_2 = {}
# 
# for k, v in dict_1.items():
    # dict_2[v] = k
# 
# print(dict_2)


# a1 = dict(a = 1, b = 2)
# a2 = {'a':1, 'b':1}
# a3 = dict.fromkeys('hi')
# print(a1)
# print(a2)
# print(a3)


