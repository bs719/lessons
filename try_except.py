'=======Exceptions====='
'Исключения - это обьекты которые прерывают работу кода если не были обработаны '

#SyntaxError
'исключение, которое выходит,когда в коде допущена синтаксическая ошибка'

'''
a = 
SynaxError
'''

NameError
# выходит когда обращаешься к несуществующей переменной

'''
num1 = 15
print(num5)
NameError
'''

IndexError
# выходит когда обращаешься к несуществующему индексу

'''
list1 = [1,2,3,4]
print(list1[7])
IndexError
'''

KeyError
# исключение, которое выходит, когда мы обращаемся по несуществующему ключу

"""
dict_ = {'a':1}
dict_['c']
KeyError
"""

'''
dict_ {'a':1}
dict_.get('c')
ошибки не будет!!! Так как get не вызыввает ошибку, а вернет None, если такого ключа нет
'''

ValueError
# когда мы передаем в функцию не корректный для нее тип данных
# когда мы распаковываем итериуемый объект на несколько переменных и кол-во переменных не совпадает с кол-вом элементов

'''
int('10dkn')
ValueError
'''

'''
a, b, c = 1, 2
ValueError
'''

TypeError
# исключение выходит, когда мы пытаемся использовать методы не свойственные какому-то типу данных
# когда мы пытаемся передать функции больше или меньше аргументов, чем принимает функция

'''
for i in 1234:
   ...
TypeError
'''

'''
"5" + 5
TypeError
'''


'''
{[1,2,3]:'hi'}
'''


'''
input('Введите число', 123)
TypeError
'''


'''
[].append()
'''


ZeroDivisionError
'''
45 / 0
ZeroDivisionError
'''

'''
45 // 0
ZeroDivisionError
'''


'''
45 % 0
ZeroDivisionError
'''

AttributeError
# выходит, когда мы обращаемся к несуществующему аттрибуту или методу объекта (типа данных)


'''
[1,23,1,56].replace('a', '')
AttributeError
'''

'''
'makers'.pop(0)
AttributeError
'''


IndentationError
# выходит, когда мы неправильно используем оступы

'''
    a = 5
IndentationError
'''

'''
for i in range(11):
pirnt(i)
IndentationError
'''


Exception
# исключение, которое создали, чтобы его вызывать

'===============================Вызов исключений================================'

# raise NameError ('Просто вызываю NameError')
# raise IndexError
# raise KeyError


'==============================Обработка исключений============================='

# чтобы код не прекращал свою работу, мы можем использовать конструкцию try-except, и обрабатывать вызванное исключение

# try:
    # код, который может вызвать ошибку/исключение
    # num = int(input('Введите число:'))
# except ValueError:       # Ожидаемое исключение
    # Обработку на исключение которое поймали
    # print('Вы ввели не число')
# else:           
    # код, который отработает, если исключения не вышло
    # print(f'Вы ввели число {num}')
# finally:        
    # работает всегда
    # print('До свидания')
    

# try:
    # ...
# except ZeroDivisionError:
    # ...
    # 
# 
# try:
    # num = (input('ВВедите число:'))
    # res = 10 / num
# except (ValueError, ZeroDivisionError):
    # print('Что-то пошло не так')
    
    
# try:
    # num = int(input('введите число'))
    # res = 10 / num
# except ValueError:
    # print('что-то пошло не так')
# except ZeroDivisionError:
    # print('вы ввели 0')

# except Exception - обрабатывает все исключения которые могут выйти

# try:
    # num = int(input('введите число'))
    # res = 10 / num
# except ValueError as e:
    # print('что-то пошло не так')
    
# мы можем указать в except несколько исключений при помощи скобок и запятой except (ValueError, TypeError, ZeroDivisionError)


# try:
    # raise NameError
# except NameError:
    # print(1)
    
    
    
# try:
    # num = int(input('Введите число: '))
    # if num == 0:
        # raise ZeroDivisionError
    # elif num > 0:
        # raise ValueError
    # elif num < 0:
        # raise TypeError
# except ValueError:
    # print('Положительное')
# except TypeError:
    # print('Отрицательно')
# except ZeroDivisionError:
    # print('0')
   