import random

# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# for i in range(len(lst)):
#     print(i, lst[i])
#
#
# for i, elem in enumerate(lst):
#     print(i, elem)
#     lst[i]*= 2
#     print(i, elem)
#
#
# for elem in lst:
#     elem *= 2
#     print(elem)
#
#
# for i in range(len(lst)):
#     lst[i] *= 2
#     print(lst)


# cпособы подсчета списка
# print(lst)
# for i in range(len(lst)):
#     lst[i] = lst[i]**2
# print(lst)
#
# print("//////////////////////////////////////////////////")
#
# lst = [10, 20, 30, 40, 50, 60,70,80,90]
#
# print(lst)
# for i, elem in enumerate(lst):
#     lst[i] = lst[i] ** 2
# print(lst)
#
#
# print("//////////////////////////////////////////////////")
#
# lst = [0] * 20
# print(lst)

lst = [0] * 20


def fill_list(lst, lower_bound, upper_bound):
    for i in range(len(lst)):
        lst[i] = random.randint(lower_bound, upper_bound)
    return lst


print(id(lst), fill_list(lst, 0, 100))


def multiple_list(lst,coeff):
    for i in range(len(lst)):
        lst[i] *= coeff
    return lst


print(id(lst), multiple_list(lst,10))


def nullify_list(lst):
    for i in range(len(lst)):
        lst[i] = 0
    return lst

print(id(lst), nullify_list(lst))
