# comprehension - это генератор с помощью которого можно создать последовательность используя цилк for в одну строку

# range()
# []
# {}
# {:}

# результат for элемент in последовательность
# gen = ('hi' for x in range())
# prin(gen)     #<generator object <genexpr> at 0x7f52ad640510>

# list_1 = [x + 2 for x in [23, 0, 5, 10]]
# print(list_1)       #[25, 3, 7, 12]

# list_ = []
# for i in range(1,11):
    # if i % 2 == 0:
        # list_.append('четные')    #i
    # else:
        # list_.append('нечетные')  #i*2
# print(list_)

# list_2 = [i if i % 2 == 0 else i*2 for i in range(1,11)]

'В coprehension можно добавлять условия, там их бывает 2 вида'
'1 - тернарный оператор, пишется перед циклом, так как используем и if, и else'
'2 - фильтр пишется после цикла, так как используется только if'


# list_1 = [12, True, None, 'hi', 0, False, 'makers', 'world']
# list_2 = [i for i in list_1 if type(i) == str]
# print(list_2)

'========================Виды comprehension======================'
'1 - list comprehension'
'2 - dict ocmprehension'
'3 - set comprehension'

'Dict comprehension'

# dict_1 = {i:i**2 for i in range(1, 11)}   #
# print(dict_1)

# dict_1 = {'a':1, 'b':2, 'c':3} 
# dict_2 = {value:key for key,value in dict_1.items()}
# print(dict_2)

# dict_1 = {
    # 'a':[1,2,3],
    # 'b':[12,0,1],
    # 'c':[32,0,0,10]
# }
# dict_2 = {k:sum(v) for k,v in dict_1.items()}
# print(dict_2)

'Set comprehension'

# set_1 = {i for i in range(1, 11)}
# print(set_1)                       #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# set_1 = {12,3,4,13,1}
# set_2 = {i ** i for i in set_1}
# print(set_2)                         #{256, 1, 8916100448256, 27, 302875106592253}

# set_1 = {12,4,34,5,6}
# set_2 = {str(i) for i in set_1}
# print(set_2)                           #{'5', '12', '4', '34', '6'}


# set_1 = {1,12,'hi',34,True, 'makers'}
# set_2 = {i for i in set_1 if type(i) == str}
# print(set_2)                          #{'hi', 'makers'}


# set_1 = {12,True,'hi',23,'10','makers', False,'1'}
# set_2 = {int(i) if i.isdigit() else i for i in set_1 if type(i) == str}
# print(set_2)                            #{1, 10, 'makers', 'hi'}


# dict_1 = {i: [i for i in range(1,i+1)] for i in range(1,6)}
# print(dict_1)                              #{1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}