'=========================Циклы========================'
#цикл - это оператор/конструкция, который повторяет код несколько раз.

#есть 2 вида цикла:
'1. for - цикл, который работает с итерируемым объектом. Цикл заканчивает работу, когда доходит до последнего элемента итерируемого объекта'

'2 - while - цикл, который работает до тех пор пока условие верное (True)'

'Итерируемый объект - это какая-то последовательность, например: [1,23,"hi"], "makers", (123, True, 1,5), dict, set'

'Итерация - процесс перебора итерируемого объекта (когда мы по очереди вытаскиваем элементы в последовательности)'

'FOR'

#list_ = [12, 'hi', True, None, [0,0,0]]
# print(list_[0])
# print(list_[1])
# print(list_[2])
# print(list_[3])

#or i in list_: 
#    print(i)


#for letter in 'hello world':
#    print(letter)

#for number in [12, 3, 4, 0, -1, 20]:
#    print(number * 2)
    
#list_ = [2, 12, 5, 3]
#for i in list_:
#    print(i ** 2)
    
# text = 'makers'
# for letter in text:
#    print(letter)

#list_ = [2, 5, 20, 10, 9, -1]
#for i in list_:
#    if i % 2 == 0:
#        print(i)
##   else :
##        print('УЧИ!')
    
'WHILE'

#n = 1
#while n < 10:
#    print(n)
#    n = n + 1

# n = 0
# while n:
    # print('hi')
    # n += 1

#Останавливает ваш код в терминале
# ctrl + c
# ctrl + z

'==============================Ключевые слова в циклах==========================='
#break - принудительная остановка цикла
#continue - пропускает итерацию, продолжает со следующей итерации

#range()  #генератор
# for i in range(1, 11):
    # if i == 3:
        # continue
    # print(i)


# for i in range(11):
    # if i == 2:
        # break
    # print(i)

# n = 1
# while n < 10:
    # n = n + 1 
    # if n == 2:
        # continue
    # print(n)
    
# n = 0
# while n < 10:
    # print(n)
    # if n < 100:
        # break
    # n += 1   #n = n + 1
# 