'===============================Встроенные функции=========================='
# map, filter, reduice, zip, enumerate

'ZIP'
# соединяет несколько последовательностей (получаем генератор, в котором элементы - tuple)


# list1 = [1,2,3,4]
# list2 = ['a','b','c','d']
# list3 = [10.5, 20.6, 35.8, 0.5]
# 
# zipped = zip(list1, list2)
# print(list(zipped))       list[tuple, tuple, tuple]
# [(1, 'a', 10.5), (2, 'b', 20.6), (3, 'c', 35.8), (4, 'd', 0.5)]

# print(dict(zipped))       dict{k:v, k:v, k:v}
# {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

'ENUMERATE'
# нумерует последовательность (по дефолту с 0) (тоже возвращает генератор)

# enumerated = enumerate('hello')              #<enumerate object at 0x76e150cde700>
# print(list(enumerate))                       #[(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]       
# emumerated = enumerate('hello', 100)         #[(100, 'h'), (101, 'e'), (102, 'l'), (103, 'l'), (104, 'o')]

# enumerated = enumerate('hello')
# for i in enumerated:
    # print(i)         
# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')

# enum = enumerate([12,8,'hi',True,'Hello',None], 15)    # [(15, 12), (16, 8), (17, 'hi'), (18, True), (19, 'Hello'), (20, None)]
# print(list(enum))
# for n,v in enum:
    # print(f'Номер: {n},Значение: {v}')
    # Номер: 15,Значение: 12
# Номер: 16,Значение: 8
# Номер: 17,Значение: hi
# Номер: 18,Значение: True
# Номер: 19,Значение: Hello
# Номер: 20,Значение: None


'MAP'
# принимает другую функцию и последовательность. МЭП применяет функцию, которую мы передали на каждый элемент из последовательности. 
#Возвращает МЭП объект.

# list_ = [1,2,3,4]      #['1','2','3','4']
# def func(a):
    # return str(a)
# 
# mapped = map(func, list_)
# print(mapped)          #<map object at 0x7a72f835b700>
# print(list(mapped))    #['1', '2', '3', '4']


# list_1 = [1,2,3,4]
# def func(a):
    # return a ** 2
# mapped = map(func, list_1)
# print(list(mapped))      #[1,4,9,16]


'lambda - это одноразовая, анонимная функция'

# def func(num):
    # return num ** 3
# 
# func(2)  #8

# result = lambda num: num ** 3
# print(result(2))                   #8

# print((lambda num: num ** 3)(2))   #8


# def func(a):
#   return a ** 2
# 
# mapped = map(func, list_1)
# print(list(mapped))      


# list_1 = [1,2,3,4]
# mapped = map(lambda a: a **2, list_1)
# print(list(mapped))                    #[1, 4, 9, 16]

'FILTER'
# принимает другую функцию и последовательность, применяет функцию, которую мы передали на каждый элемент последовательности 
# и оставляет только те элементы, которые прошли проверку.

# list1 = [-10,0,39,-12,2,0]
# 
# def func(a):
    # return a >= 0
# 
# filtered = filter(func, list1)
# print(list(filtered))                        #[0, 39, 2, 0]
# 
# filtered = filter(lambda a: a >= 0, list1)
# print(list(filtered))                        #[0, 39, 2, 0]

# list1 = [1,2,3,4,5,6,7,8]
# 
# filtered = filter(lambda a: a % 2 == 0, list1)
# print(list(filtered))                               #[2,4,6,8]
# 
# print(list(filter(lambda a: a % 2 == 0, list1)))    #[2,4,6,8]

'REDUCE'
# принимает функцию и  последовательность, возвращает 1 результат (передаваемая функция, должна принимать 2 аргумента)

# from functools import reduce
# 
# list1 = [12,3,8,5]
# print(reduce(lambda a,b: a+b, list1))      #28

# list1 = ['hi', 'a', 'world', 'name']
# list2 = sorted(list1, key=len)
# print(list2)