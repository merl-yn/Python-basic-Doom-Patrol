def func_calc():
    first_num = int(input("Enter first num: "))
    operation = input("Enter operation: ")
    second_num = int(input("Enter second num: "))
    result = 0

    if operation == '+':
        result += first_num + second_num
    elif operation == '-':
        result += first_num - second_num
    elif operation == '*':
        result += first_num * second_num
    elif operation == '/':
        if second_num == 0:
            print("Ділення на 0!")
            result = None
        else:
            result += first_num / second_num
    elif operation == '//':
        result += first_num // second_num
    elif operation == '%':
        result += first_num % second_num
    elif operation == '**':
        result += first_num ** second_num
    else:
        print("Такої операції немає!")

    result_str = f'{first_num} {operation} {second_num}'

    file = open('result.txt', 'w')
    file.write(f'{result_str} = {result}')
    file.close()


def print_result():
    with open('result.txt', 'r') as file:
        text_in_file = file.read()
        print(text_in_file)


while True:
    func_calc()
    print_result()
