import functools

# 1
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

# 2
lst_d.append(4)
lst_d.append(5)

# 3
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

# 4
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

# 5
print(("Anna has {} apples and {} peaches.".format(1, 2)))

# 6
print(("Anna has {0} apples and {1} peaches.".format(1, 2)))

# 7
print(("Anna has {one} apples and {two} peaches.".format(two=2, one=1)))

# 8
print("Anna has {0: >5} apples and {1: >3} peaches.".format("one", "two"))

# 9
apple = 1
peach = 2
print(f"Anna has {apple} apples and {peach} peaches.")

# 10
print("Anna has %s apples and %s peaches." % (apple, peach))

# 11
dictNum = {"apple": 1, "peach": 2}
print("Anna has {apple} apples and {peach} peaches.".format(**dictNum))

# 12
'''lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)'''
lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)

# 13
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
list_comprehension = []
for num2 in range(10):
    if num2 % 2 == 0:
        lst.append(num2 // 2)
    else:
        lst.append(num2 * 10)

# 14
"""d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)"""
dict1 = {num ** 2 for num in range(1, 11) if (num % 2 == 1)}
print(dict1)

# 15
"""d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)"""
dict2 = {num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict2)

# 16
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
dict_comprehension1 = {}
for t in range(10):
    if t ** 3 % 4 == 0:
        dict_comprehension1[t] = t ** 3

# 17
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
dict_comprehension2 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension1[x] = x ** 3
    else:
        dict_comprehension1[x] = x

# 18

"""def foo(x, y):
    if x < y:
        return x
    else:
        return y"""
foo1 = lambda a, b: a if a < b and b > a else b


# 19
# foo = lambda x, y, z: z if y < x and x > z else y
def foo2(c, d, e):
    if d < c:
        return e
    elif c > e:
        return d
    else:
        pass


lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20
print(sorted(lst_to_sort))

# 21
print(sorted(lst_to_sort, reverse=True))

# 22
new_list = list(map(lambda i: i * 2, lst_to_sort))
print(new_list)

# 23
list_A = [2, 3, 4]
list_B = [5, 6, 7]
listC = list(map(lambda j, k: j ** k, list_A, list_B))


def getAdd(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


functools.reduce(getAdd, lst_to_sort)

# 25
listD = list(filter(lambda g: (g % 2 == 1), lst_to_sort))
print(listD)

# 26
lst_neg = list(filter(lambda b: b < 0, range(-10, 10)))
print(lst_neg)

# 27
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]

list_3 = list(filter(lambda p: p in list_1, list_2))
print(list_3)
