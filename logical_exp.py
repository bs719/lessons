'========================Логические и условные операторы======================='
#boolean - тип данных, который имеет 2 значения
#True (да, истина) и False (нет, ложь)

# print (bool (0)) #False
# print(bool(-10)) #True
# print(bool(' ')) #True
# print(bool('')) #False
# print(bool(None)) #False

#Логические операторы - выражения, которые возвращают True, если выражение верное, False - если не верное

# 'равенство'
# 5 == 5 #True
# 5 == 7 #False
# 
# 'не равенство'
# 5 != 10 #TRue
# 
# 'больше'
# 5 > 1 #True
# 0 > 10 #False
# 
# 'меньше'
# 10 < 100 #True
# 0 < -10 #False
# 5 < 5 #False
# 
# 'больше или равно'
# 5 >=10 #False
# 10 >= 3 #True
# 3 >= 3 #True
# 
# 'меньше или равно'
# 10 <= 5 #False
# 5 <= 10 #True
# 5 <= 5  #True
# 
# '5' == 5 #False
# 'hello' == 'hello' #True
# 'hello' == 'Hello' #False



'==========================And Or Not=========================='
#and - и
#or - или
#not - не

'AND - возвращает True, если все выражения вернули True'

# a = 5
# b = 6
# 
# a == 5 and b == 6
# 
# True   и    True
#a == 5 and b == 6 #True

# False  и    True
#a == 6 and b == 6 #False

# True   и   False
#a == 5 and b == 2 #False

# False  и   False
# a == 1 and b == 1 #False
# 

'OR - возвращает True, если хотя бы одно из выражений вернул True, либо когда все выражения вернули True'

# c = 5
# d = 6

#True или True
# c == 5 or d == 6 #True

#False или True
# c == 1 or d == 6 #True

#True или False
# c == 5 or d < 1 #True

#False или False
# c <= 1 or d > 1000 #False
# 
'NOT - это частица "не", которая меняет значение на противоположное'

# a = 1
# b = 5
# 
# not False # True
# not True # False

#not False или False  и  True
# not a == b or b > 10 and 10 == a #True
# 
# 
# not not not not not 5 == 5 #False
# 
# not 5 != 5 #True
# 
# bool(None) #False
# bool('None') #True
# bool([]) #False


'===================Условные операторы====================='
#Условные операторы - конструкция, которая используется для того, чтобы при разных входных данных код работал по разному (в зависимости от условия)
 
# pogoda = 'дождь'
# if pogoda == 'дождь':
    # print('взял зонт')
# elif pogoda == 'снег':
    # print('взял шапку и шарф')
# elif pogoda == 'солнце':
    # print('взял очки')
# else:
    # print('сижу дома')
    
    
# fact = 'распиздяй'
# if fact == 'распиздяй':
    # print('безработный')
# elif fact == 'много времени':
    # print('Нураалы')
    
#в одной конструкции мы можем использовать один if
#в одной конструкции мы можем использовать неограниченное кол-во elif или не использовать вообще
#в одной конструкции мы можем использовать только один else или не использовать вообще

#Принять от пользователя число, и узнать какое это число, отрицательное, положительное или 0

# num = int(input('Введите число:'))
# if num > 0:
    # print ('число положительное')
# elif num < 0:
    # print('число отрицательное')
# else:
    # print('число 0')

'=====================Тернарный оператор================'
#тернарный оператор - условия в одну строку

#тело1 if условие1 else тело2

# num = 0
# if num > 0:
    # message = 'Положительное число'
# else:
    # message = 'Отрицательное число или 0'
# print(message)

# num = 0
# message = 'Положительное число' if num > 0 else 'Отрицательное число или 0'
# print(message)

 

 
# string = input('Here, there, and everywhere') 
# if len('string') > 5: 
    # print(True) 
# elif('string') < 5:
    # print(False)
    # print(len(string) > 5)
    

string = str(input('ldkvdvn'))
if len(string) < 5: 
    print('True') 
elif len (string) > 5:
    print('False')
else:
    print('False')