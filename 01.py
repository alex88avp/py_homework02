# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

    
# def InputNumbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = float(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("Это не число!")
#     return number

number = input("Введите число: ")

def sumNums(number):
    sum = 0
    for i in str(number):
        if i != ".":
            sum += int(i)
    return sum

print(f"Сумма цифр = {sumNums(number)}")   