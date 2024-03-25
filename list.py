'===========================List========================='
#списки - изменяемый, индексируемый, упорядодченный, итерируемый тип данных, предназначенный для хранения любых данных в определенном порядке

list_1 = [1, 2, 14, 'hello', True, [0,0,0], None]
         #0  1  2      3      4       5       6
list_1 [3]       # 'hello'
list_1[-1]       #None
list_1[-2] [-1]  #0
list_1[3] [-2]   #l
list_1[5]        #[0,0,0]

'range(start, end(не включительно), step) - это функция генератор, которая генерирует/создает диапазон от start до end(не включительно)'

#list('hello') -> ['h', 'e', 'l', 'l', 'o']
# list_2 = list(range(0, 101))  #[0,1,2...100]
# print(list_2)

# print(list(range(11, 4, -1)))
# [1,2,3,4,5,6,7,8,9,10] шаг 1
# [0,2,4,6,8,10]         шаг 2
# [0,3,6,9]              шаг 3
# [11, 10,8,6,5]         шаг -1

'===========================Методы списков======================='

'append - добавление элемента в конец списка'

# list_ = []
# list_.append(1)
# list_.append('hello world')
# list_.append(True)
# print(list_) #[1, 'hello world', True]

'pop - удаление элемента из списка по индексу, возвращает удаленный элемент. Если не указать индекс, то удалит с конца'

# list_ = [90, True, None, 'Hi']
# popped = list_.pop ()
# print(list_) #[90, True, None]
# print(popped) #True

'remove - удаление элемента из списка по значению'

# list_ = [1, 2, 3, 5, 99, 1, 'hi', -11]
# list_.remove(5)
# print(list_)  #[1, 2, 3, 99, 0, 1, 'hi', -11]

'count - считает кол-во принятого элемента в списке'

# list_ = [1, 23, 1, 'hi',4, 5, 6, 'hi', 1, 7, 1, 7, 8, 1]
# print(list_.count(7))     #2
# print(list_.count('hi'))  #2

'index - возвращает индекс первого вхождения принятого элемента'

# list_ = ['hi', 1, 341, 2, 0, 2, 1, 'makers', 99, 10]
# print(list_.index(0))    #4

'extend - расширяет список при помощи другого списка'

# list_1 = [1,2,3]
# list_2 = [0,0,0]
# list_1.append(list_2)   #[1,2,3,[0,0,0]]
# print(list_1)
# list_1.extend(list_2)   #[1,2,3,[0,0,0],0,0,0]
# print(list_1)

'reverse - изменяет список, расставляя его элементы в обратном порядке'

# list_ = ['hi', 1, 2, 3, True]
# list_.reverse()
# print(list_)  #[True, 3, 2, 1, 'hi']

'sort - сортирует список, состоящий из элементов одно типа данных'
# list_ = [12, 4, 1, 0, 7]
# list_.sort(reverse=True)
# print(list_)    #[12,7,4,1,0]
# 
# list_ = ['c', 'b', 'v', 'w', 'A', 'M']
# list_.sort()
# print(list_)    #['A', 'M', 'b', 'c', 'v', 'w']

'clear - очищает список'

# list_ = [12, 42, 1, 'hi', 0, False, None]
# list_.clear()
# print(list_)  #[]
# 
# len([12, 4, 5, [1,2,3]])    #4
# 
# a = 10
# b = 5
# c = 2
# 
# a, b, c = 10, 5, 2
# print(a)

# list_ = [23, 'hi', 4, 0, 'makers']
# for i in list_:
    # print(i) 

# meshok = ['картошка', 'лук', 'лук', 'картошка', 'лук']    
    # 
# paket1 = []
# paket2 = []
# 
# for ruka in meshok:
    # if ruka == 'картошка':
        # paket1.append(ruka)
    # elif ruka == 'лук':
        # paket2.append(ruka)
        # 
# print(paket1)
# print(paket2)










# x = int(input(675))
# y = int(input(23))
# if x % y == 0: 
    # print('x делится на y') 
    # d = x//y
    # print(f'Частное: {d}') 
# else : 
    # print('x не делится на y') 
    # a = x // y 
    # print(f'Частное: {a}') 
    # b = x % y 
    # print(f'Остаток: {b}')
    
    
    
    
# num = int(input(57))
# if chr(num) :
    # print(f'Это не буква, а "символ" {num}')
# else :
    # print(f'Это буква "буква" {num}')
    
    
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 - y1 == x2 - y2:
    # print('YES')
# else:
    # print('NO')
    
    
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 and not y1 == y2:
    print('YES')
elif y1 == y2 and not x1 == x2:
        print('YES')
else:
    print('NO')