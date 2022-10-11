import math

x_coordinate_A = float(input('Введите координату точки А по оси Х: '))
y_coordinate_A = float(input('Введите координату точки А по оси Y: '))
z_coordinate_A = float(input('Введите координату точки А по оси Z: '))
x_coordinate_B = float(input('Введите координату точки B по оси Х: '))
y_coordinate_B = float(input('Введите координату точки B по оси Y: '))
z_coordinate_B = float(input('Введите координату точки B по оси Z: '))

distance = round(math.sqrt((x_coordinate_B - x_coordinate_A)**2 + (y_coordinate_B - y_coordinate_A)+ (z_coordinate_B - z_coordinate_A)**2), 2)
print(distance)

