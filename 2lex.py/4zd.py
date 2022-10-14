# Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях(не индексах).
from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-10,10))
print(numbers)

def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('Number of elements: ', get_numbers(numbers))

a = int(input('Введите место первого элемента: '))
b = int(input('Введите место второго элемента: '))

for i in range(len(numbers)):
    mult = numbers[a-1]*numbers[b - 1]
print(f'Множество элементов: {numbers[a -1]} * {numbers[b -1]} =', mult)