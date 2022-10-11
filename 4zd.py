a = int(input('Введите номер четверти: '))
if a < 1 or a > 4:
     print('Пожалуйста,введите правильное число(от 1 до 4)')
elif a == 1:
     print('x > 0 and y > 0')
elif a == 2:
     print('x < 0 and y > 0')
elif a == 3:
     print('x < 0 and y < 0')
elif a == 4:
     print('x > 0 and y < 0') 
