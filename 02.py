# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input("Введите число: "))

def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)

list = []
for e in range(1, number + 1):
    list.append(mult(e))

print(list)