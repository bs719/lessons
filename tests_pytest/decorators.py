'==============================Декораторы=================='
# функция высшего порядка - функция, которая принимает в аргументы другую функцию, создает внтури себя функцию, вызывает внутри функцию и возвращает функцию

# def func1():
# ...

#def func2(a): #функция высшего порядка, так как принимает другую функцию в аргументы
#       a()

#func@(func1)

# декораторы - функция высшего порядка, которая нужна чтобы расширить функционал другой функции не изменяя ее (функция обертка)

# def glushitel(func):
    # def wrapper(*args, **kwargs):
        # text = func(*args, **kwargs)
        # return text + 'тихо'
    # return wrapper
# 
# def gun():
    # return 'Стреляет '
#  
# wrapper = glushitel(gun)
# result = wrapper()
# print(result)

# def glushitel(func):
    # def wrapper(*args, **kwargs):
        # text = func(*args, **kwargs)
        # return text + 'тихо'
    # return wrapper
# 
# @glushitel
# def gun():
    # return 'Стреляет '
# 
# result = gun()
# print(result)


# from datetime import datetime
# 
# def func_start_time(func):
    # def wrapper():
        # time_ = datetime.now().strftime('%d.%m.%Y %H:%M')
        # print(f'Наша функция запутилась {time_}')    
        # func()
    # return wrapper
# 
# @func_start_time
# def func():
    # print('hi')
# 
# @func_start_time    
# def func1():
    # print('hello')
    # 
# func()
# func1()


def decorator(num):
    def inner_decorator(func):
        def wrapper():
            for i in range(1,num+1):
               func()
            return wrapper
        return inner_decorator

@decorator(3)
def hello():
    print('helo world')

hello()