'''сделать пример функции
без return c pass or ...
сделать 5 различных функций на свое усмотрение.'''

def send_text():
    print("Здравствуйте уважаемый пользователь!")
    pass


send_text()

def send_text_2():
    text = input("Введите Ваше имя: ")
    print(f'Здравствуйте, {text}! Очень рады Вас видеть.')


send_text_2()


def find_square(x):
    y = x**2
    return y


x = int(input('Введите число: '))
print(f'квадрат числа {x} = {find_square(x)}')


a, b, c = input('введите длину (см) сторон треугольника: ').split()
a, b, c = float(a), float(b), float(c)


def square_triangle(a, b, c):
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    return round(s, 2)


def perimeter_triangle(a, b, c):
    p = a+b+c
    return p


print(f'Периметр треугольника = {perimeter_triangle(a, b, c)} см, его площадь = {square_triangle(a, b, c)} см2')

