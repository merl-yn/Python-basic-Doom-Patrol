def user_input():
    first_num = int(input("Enter first num: "))
    operation = input("Enter operation: ")
    second_num = int(input("Enter second num: "))
    result = f'{first_num} {operation} {second_num}'
    file = open('result.txt', 'w')
    file.write(result + " = " + str(eval(result)))
    file.close()


def print_result():
    with open('result.txt', 'r') as file:
        text_in_file = file.read()
        print(text_in_file)


while True:
    user_input()
    print_result()
