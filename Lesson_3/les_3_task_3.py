# 3. В массиве случайных целых чисел поменять
# местами минимальный и максимальный элементы.


import random
a = [random.randint(20, 80) for _ in range(20)]
a.sort()
print(a)

min = 0
max = 0
for i in range(len(a)):
    if a[i] < a[min]:
        min = i
    elif a[i] > a[max]:
       max = i
print('a[%d]=%d a[%d]=%d' % (min+1, a[min], max+1, a[max]))
b = a[min]
a[min] = a[max]
a[max] = b

for i in range(len(a)):
    print(a[i], end='')
print(a)
