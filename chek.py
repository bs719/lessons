"""
1) Мурат с друзьями на выходных решил собраться и пойти в ночной клуб.
Но в ночной клуб пропускают только тех, кому 17+.
Мурату - 24 года, Эржану - 21 год, Карине - 24 года, Алтынай - 17 лет, Айбеку - 16 лет.
Напишите программу, которая определяет кого пустить в ночной клуб, а кого нет. (работа со словарем)
"""
# dict_ = {
    # 'murat':24,
    # 'erjan':21,
    # 'karina':24,
    # 'altinay':17,
    # 'aybek':16,
# }
# dict_ = {k:v for k,v in dict_.items()if v > 18}
# print(dict_)



# 2) Дан словарь а, значениями которого являются словари,
# измените словарь 'а' таким образом, чтобы значения внутреннего словаря стали 
# внешними значениями

# a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# dict_ = {k:y for k,v in a.items() for x,y in v.items()}
# print(dict_)

# Вывод:
# {'a': 32, 'b': 36, 'c': 37, 'd': 21}
"""
"""
# 3) Создайте словарь, где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным.
# """
# писать код здесь
# """
# 4) Создайте словарь, где значениями будут являться числа. 
# Найдите сумму этих значений.

dict_ = {
    
}


# """

# dict_ = {
    # 'apple':30,
    # 'melon':35,
# }
# dict2_ = {k:v for k,v in dict_.items() if v % 2 != 0} 
# print(dict2_)
# писать код здесь
# """
# 5) Создайте словарь из чисел от 1 до 10, где ключами будут сами числа, а значениями их квадраты.
# """
# писать код здесь
# """
# 6) Дан словарь, значениями в котором являются другие словари. Замените внутренние словари их значениями. Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}} -> {'first': 1, 'second': 2}
# """
# писать код здесь
# """
# 7) Дан словарь dict_. Отсортируйте словарь по значениям в порядке уменьшения.
# Новые элементы занесите в словарь sorted_dict




# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {}
# 
# Вывод:
# {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
# """
# писать код здесь
# """
# 8) Запросите у пользователя сумму, которая у него сейчас есть в бумажнике. Если он введёт сумму, меньшую чем 0, то запринтите исключение с текстом "Сумма не может быть отрицательной!"
# """
# писать код здесь
# 
# 
# """
# 9) Создайте список list_ из чётных целых чисел в промежутке от 1 до 25. 
# Нужно использовать comprehension.
# """


"""
10) Создайте список используя

list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

и запишите в новый список int_list

числа, которые меньше нуля, замените на 1. Нужно использовать comprehension.
"""