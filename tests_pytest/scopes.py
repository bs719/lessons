'==============================Области видимости=============================='
# LEGB - local enclosed global build-in

'Build-in(Встроенное пространство)'
# Это пространство, которое находится в python (print, input, int, str, sum)

'Global(Глобальное пространство)'
# это пространство, которое находится у вас в файле 
# Globals() - показывает все глобальные переменные


#a = 5 
#b = 'hello'
#print(globals())


'Enclosed(Замкнутая)'
# Это пространство, которое находится во вложенных функциях

# var = 'global'

# def func():
    # локальное пространство для глобального пространства
    # замкнутое пространство(потому что есть более локальное пространство)
    # var = 'enclosed'
    # def func2():
        # локальное пространство для пространства func
        # var = 'local'
        # print(var)
    # print(var)
    # func2()
# 
# print(var)
# func()


'Local(Локальное пространство)'
# Это пространство, которое находится внутри функции 
# locals() - выводит переменные локального пространства 

# a = 10
# def func(a,b):
#    print(a,b)
#    print('Глобальное', globals())
#    print('Локальное', locals())
   
   




# var = 'global'
# def func():
    # global var
    # var = 10
#    
# print(var)
# func()
# print(var)

'global - это оператор, который позволяет менять переменную с глобального пространства'

# def func():
    # var = 'enclosed'
    # def func2():
        # nonlocal var
        # var = 'local'
    # print(var)       #enclosed
    # func2()
    # print(var)       #local
    
# func()

'nonlocal - это оператор, который позволяет менять переменную с локального пространства'

# count = 0
# def incr():
    # global count
    # count = count + 1

# incr() #1
# incr() #2
# incr() #3
# incr() #4
# incr() #5
# print(count)       #5