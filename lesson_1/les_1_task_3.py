#3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.


import random
a = int(input('Введите нижнюю границу диапазона целых чисел: '))
b = int(input('Введите верхнюю границу диапазона целых чисел: '))
c = random.randint(a, b)
print(c)

a_1= float(input('Введите нижнюю границу диапазона вещественных чисел: '))
b_1 = float(input('Введите верхнюю границу диапазона вещественных чисел: '))
c_1 = random.random()*(b_1 - a_1) + a_1
print(c_1)

a_2= int(input('Введите нижнюю границу диапазона символа от 0 до 26: '))
b_2 = int(input('Введите верхнюю границу диапазона символа от 0 до 26: '))
c_2 = chr(random.randrange(97 + a_2, 97 + b_2))
print(c_2)