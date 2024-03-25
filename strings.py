'=========================Strings==================='
#строки - неизменяемый тип данных, который предназначен для хранения текста, заключенного в одинарные либо двойные кавычки

# string1 = 'строка с одинарными кавычками'
# string2 = "строка с двойными кавычками"
# string3 = "Don't" #внутри двойных кавычек все одинарные кавычки - просто часть текста
# string4 = 'Название магазина "Азбука"'
# string5 = ''' 
# Многострочный текст
# в одинарных кавычках
# Тут можно использовать и одинарные и двойные кавычки
# '''
# string6 = """ 
# Многострочный текст
# в двойных кавычках
# Тут можно использовать и одинарные и двойные кавычки
# """
# string7 = 'hello' + ' ' 'world'     #helloworld
# print(string7)

# string8 = 'A' * 20      #AAAAAAAAAAAAAAAAAAAAA
# print(string8)

'====================================Экранизация строк====================================='
# '\n' #перенос на новую строку
# print('hello world') #hello world
# '---------------------------------------'
# print('hello\nworld') #hello
#                       #world
# '---------------------------------------'
# print('he\nllo world') #he
#                        #llo world
# '---------------------------------------'

# '\t' #табуляция (несколько пробелов)
# print('hello\tworld') #hello   world
# print('he\tllo world') #he   llo world

# '\v' #перенос на новую строку со смещением вправо на длину предыдущей строки
# print('hello\vworld\vmakers') #hello
#                                #    world
#                                #         makers
                               
# '\r' #перенос каретки в самое начало строки
# print('Hello world\rMa') #Mallo world

# '\' #отображение '
# "\" #отображение "

# print('Don\'t')
# print('Home"\\"Makers')

# '\\' #отображение \
# print('команда \\n - переносит строку')

# '==============================Форматирование строк=========================='
# title = 'Iphone 15'
# price = 1000
# shop = 'Makers'
# #print('Я купил title за price $')

# '1. f-строка'
# print (f'Я купил {title} за {price}$, в магазине {shop}')

# '2. %s'
# print('Я купил %s за %s $, в магазине %s' % (title, price, shop))

# '3.str.format'
# print('Я купил {} за {}$, в магазине {}'.format(title, price, shop))


'==========================Методы строк(str)================================='
#методы - это функции, которые относятся к определенному типу данных (классу), к ним мы обращаемся через точку

# print(dir(str))

# string = 'Hi'

# print(string.upper())  #HELLO WORLD
# print(string.lower())  #hello world
# print(string.swapcase()) #hELLO wORLD

# print(string.title()) #Hello World
# print(string.capitalize()) #Hello world

# print(string.islower()) #True  - да
# print(string.isupper()) #False - нет

# print(string.center(12, '*')) #'*****Hi*****'

# string = 'hello world'
# print(string.count('l'))  #3
# print(string.count('el')) #1 
# print(string.count('o w')) #1
# print(string.count('hello')) #1

# print(string.startswith('h')) #True
# print(string.startswith('H')) #False
# print(string.startswith('hallo')) #False
# print(string.endswith('ld'))  #True

# string = 'makers'
# print(string.isalpha()) #True, проверяет на буквы
# print(string.isdigit()) #False, проверяет на числа
# print(string.isalnum()) #True, проверяет является ли строка числом или буквой или и числом и буквой, если есть символ то вернет False
# 
# string = 'hello'
# print(string.split('o')) #['hello', 'world', 'makers', 'bootcamp']
# ['hell', '.w', 'rld.makers.b', '', 'tcamp']
# 
# print(string.replace('','$'))
# string = '$$$$$$12 h e l l o $$$$'
# print(string.strip('$'))
#''.join(list) #list -> это переменная, которая хранит тип данных list []

'========================Индексы======================='
#индекс - это порядковый номер элемента в последовательности (индекс начинается с 0)

#-11-10-9-8-7-6-5-4-3-2-1
# 'h e l l o  w o r l d'
#  0 1 2 3 4 5 6 7 8 9 10

# string = 'hello world'
# print(string[0]) #h
# print(string[-1]) #d
# print(string[-6]) #' '
# 
# срез [start:end(не включительно):step]
# string[6:10] #worl
# string[0:5] #hello
# print(string[::2]) #hlowrd
# print(string[::-1]) #dlrow olleh
# print(string[::-2]) #drwolh











x = 6
y = 4
z = 2

if x == y and y == z and x == z:
    print('3')
elif x == y or y ==z or x == z:
    print('2')
else :
    print('0')