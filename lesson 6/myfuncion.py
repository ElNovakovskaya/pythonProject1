def perim(a: float, b: float, c: float):
    if a + b > c and b + c > a and a + c > b:

        pp = (a + b + c)
        p = (a + b + c) / 2
        s = pow(p * (p - a) * (p - b) * (p - c), 1 / 2)

        print(f"Площадь треугольника со сторонами {a}, {b}, {c} составляет: {s}, периметр составляет:{pp}")
    else:
        print(f'Треугольник со сторонами {a}, {b}, {c} существовать не может. И площади у него тоже нет :)')


def get_int_from_user(comment: str, lower_bound: int = float('1'), upper_bound: int = float('inf')) -> float:
    """
    Считывает int у пользователя, входящий в заданные рамки от lower_bound до upper_bound
    Считывает до тех пор, пока верное значение не было получено
    :param comment: обращение к пользователю
    :param lower_bound: нижнее допустимое значение
    :param upper_bound: верхнее допустимое значение
    :return: полученное верное integer значение
    """
    while True:
        # пытаемся
        try:
            x = input(f'{comment} ')
            x = float(x)
            if x < lower_bound or x > upper_bound:
                # вызов исключений самостоятельно
                raise ValueError
            # команда return возвращает результат работы функции
            return x
        # исключаем и обрабатываем ошибку (указываем какая ошибка. В данном случае - все ошибки)
        except Exception:
            print(f'Введите корректное значение от {lower_bound} до {upper_bound}')


print(f'My file name is {__name__}')
