'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# n=0
#
# for i in range(1,6):
#      a = 0
#      n += 1
#      for b in range(1,5):
#          a = str(a)+'0'
#      print(str(n),a)

# Задача 2
# Пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5.

# n=0
# for i in range(1, 11):
#      x=int(input('Input number: '))
#      if x == 5:
#          n +=1
# print('How many numbers 5 inputted: ', n)

'''
# Задача 3
# Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
# '''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

# Задача 4
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.

# mult = 1
#
# for i in range(1,11):
#     mult*=i
#     print(mult)
#
# '''
#
# '''
# Задача 5
# Вывести цифры числа на каждой строчке.
# '''
#
# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10
# '''
# '''
# Задача 6
# Найти сумму цифр числа.
# '''
#
# x=int(input('Input number'))
# sum=0
# while x>0:
#     sum += x%10
#     x//=10
# print(sum)
#
#
# # '''
# Задача 7
# Найти произведение цифр числа.
# '''
#
# x=int(input('Input number'))
# mult=1
# while x>0:
#     mult *= x%10
#     x//=10
# print(mult)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 213413
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''

# x=int(input('Введите число '))
# max=x%10
# x //=10
# while x>0:
#     if x%10>max:
#         max=x%10
#     x //=10
# print(max)
# '''
#
# '''
# '''
# Задача 10
# Найти количество цифр 5 в числе
# '''
#
# x=int(input('Введите число '))
#
# i = 0
#
# while x>0:
#     if x%10 == 5:
#         i+=1
#     x//=10
#
# print(i)
