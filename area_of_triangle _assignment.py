'''
This programme is too calculate the area of a triangle.
'''
base = float(input('Enter the base of the triangle\n'))
height = float(input('Enter the height of the the triangle\n'))
area = 1/2 * (base * height)
print('area', '=', area)

'''
This programme is too calculate the area of a square.
'''
length = float(input('Enter the length of the square\n'))
area = length**2
print('area', '=', area)

'''
This programme is too calculate the area of a cylinder.
'''
radius = float(input('Enter the radius of cylinder: '))
pi = 3.142
height = float(input('Enter the heigth of cylinder: '))
area = (2 * pi * radius**2) + (2 * pi * radius * height)
print('Enter the area', (round(area,2)))

'''
This programme is too calculate the area of a trapezoid.
'''
a = float(input('Enter base 1 of trapezoid: '))
b = float(input('Enter base 2 of trapezoid: '))
height = float(input('Enter the height of trapezoid: '))
area = 1/2 * (a + b) * height
print('area', '=', area)
