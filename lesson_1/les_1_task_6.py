# 6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.



a = int(input("Введите a = "))
b = int(input("Введите b = "))
c = int(input("Введите c = "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
elif a != b and a != c and b != c:
    print("Треугольник существует. Разносторонний")
elif a == b == c:
    print("Треугольник существует. Равносторонний")
else:
    print("Треугольник существует. Равнобедренный")