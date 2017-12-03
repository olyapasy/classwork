import random
import string
# # Создайте список на 50 элементов из всех нечётных чисел от 1 до 99 и передайте его в функцию, которая перемешает его элементы в случайном порядке
# # (например, 99 11 43 19 … 7 91 3 1).
# # Примечание: использовать метод random.shuffle не допускается.
# # Создайте список из 11 случайных целых чисел из отрезка [-1;1].
# # Передайте его в функцию, которая определит какой элемент встречается в списке чаще всего и вернет этот элемент.
# #  Если два каких-то элемента встречаются одинаковое количество раз, то вернуть None.
# #
# # Напишите функцию, которая преобразует переданный ей текст подобным описанным выше образом. В качестве алгоритма перемешивания букв в слове используйте следующий:
# #
# # Для каждого слова в тексте:
# #   1. Фиксируем первый и последний символы слова.
# #   2. Из оставшихся берём первые три символа, произвольно перемешиваем.
# #   3. Полученную тройку фиксируем, т.е. она уже не будет участвовать в дальнейшем перемешивании.
# #   4. Повторяем пункт 2, пока незафиксированные символы не кончатся.
# #
# # Создать программу, которая запрашивает у пользователя произвольную строку символов. Далее программа ее шифрует и выводит на экран в зашифрованном виде.
# # Шифрование происходит путем замены каждого символа символом, который находится на 5 позиций правее в предопределенной таблице шифрования.
# # Таблица шифрования задается программистом в виде одномерного списка символов латинского алфавита от a до z.
# #  Если при выборе символа для шифровки таблица шифрования заканчивается, то циклически переходить к ее началу.
# #   Таблица шифрования (a,b,c,d,...,x,y,z,1,2,3,4,5,6,7,8,9,0)
# #   Например: Исходная строка, которую ввел пользователь: 'secret'
# #   Зашифрованная строка, которую выдала программа: 'xjhwjy'
# #   Примечание: т.н. таблица шифрования может быть представлена как строка или список.
# #
# # def encode(str_to_encode): # returns enсoded string
# #       pass
# # Создать генератор паролей, который будет генерировать случайные неповторяющиеся пароли по следующим правилам:
# # Пароль состоит из 8 символов
# # В пароле допускаются только латинские большие и маленькие буквы, цифры и символ подчеркивания
# # Пароль обязательно должен содержать Большие и маленькие буквы и цифры
# print("Task 1.25")
# lst = []
# for i in range(100):
#     if i % 2 != 0:
#         lst.insert(i, i)
# print(lst)
# def shuffle_list(list_to_shuffle): # no return (shuffles list in place)
#     empty_list = []
#     while len(list_to_shuffle) != 0:
#         elem_of_list = random.choice(list_to_shuffle)
#         empty_list.append(elem_of_list)
#         list_to_shuffle.remove(elem_of_list)
#     print(empty_list)
# shuffle_list(lst)
# print("Task 1.26")
# lst1 = []
# for i in range(11):
#     i = random.randint(-1, 1)
#     lst1.insert(i, i)
# print(lst1)
# def calc_frequency(lst):  # returns the most frequent number or None
#     first_group = []
#     second_group = []
#     third_group = []
#     for elem in lst:
#         if elem == -1:
#             first_group.insert(elem, elem)
#         elif elem == 0:
#             second_group.insert(elem, elem)
#         else:
#             third_group.insert(elem, elem)
#     a = len(first_group)
#     b = len(second_group)
#     c = len(third_group)
#     if a > b > c:
#         return a
#     elif b > a > c:
#         return b
#     elif c > a > b:
#         return c
#     else:
#         return None
# print(calc_frequency(lst1))
# print("Task 1.27")
# text ='Some text for task in which I should shuffle letters in words'
#
#
# def shuffle_letters(text):
#     new_word = []
#     new_text = []
#     words_list = text.split(" ")
#     print(words_list)
#     for words in words_list:
#         print(words)
#         if len(words) > 3:
#             for letters in range(1, len(words)-1):
#                 letters = random.shuffle(words[letters])
#                 print(words[letters])
#
#
#             # if letters == 0:
#             #     new_word.insert(letters)
#             # elif letters != 0 and letters != len(words):
#             #     new_word.insert(letters)
#             # else:
#             #     new_word.insert(letters)
#     print(new_word)
# print(shuffle_letters(text))
#



def gen_password(): # returns string
    password = ''
    while len(password) != 8:
      for i in range(1):
          i =''.join(random.choice(string.ascii_uppercase) for x in range(1))
          password = password + i
          i = ''.join(random.choice(string.ascii_lowercase) for x in range(1))
          password = password + i
          i = ''.join(random.choice(string.digits) for x in range(1))
          password = password + i
    return password

password1 = gen_password()
print(password1)
