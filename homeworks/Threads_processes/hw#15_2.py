from multiprocessing import Process


def sqrt_equation(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d > 0:
        first_result = (-b - (d ** 2)) / (2 * a)
        second_result = (-b + (d ** 2)) / (2 * a)
        print(f'Result = {int(first_result)} and {int(second_result)}')
    elif d == 0:
        result = -b / (2 * a)
        print(f'Result = {int(result)}')
    else:
        print("None!")


first = Process(target=sqrt_equation(6, 11, -35))
second = Process(target=sqrt_equation(5, - 2, -9))

first.start()
second.start()

first.join()
second.join()
