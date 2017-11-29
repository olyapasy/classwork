import random

# x = 10
# while x > 0:
#     print('Hello world', x)
#     x -= 1

# # x = 10
# # while x <100:
# #     print('Hello world', x)
# #     x += 5
# #
# # x = 10
# # while x <100:
# #     print('Hello world', x)
# #     x += random.randint(0, 5)
# #
# # print("######################################################################################################################")
#
# def fill_truck(volume_capacity, lower_bound, upper_bound):
#     current_capacity = 0
#
#     while current_capacity < volume_capacity:
#         random_box = random.randint(lower_bound, upper_bound)
#         if random_box <= (volume_capacity - current_capacity):
#             current_capacity += random_box
#             print('Current capacity = %d, last box = %d' % (current_capacity, random_box))
#         else:
#             print('Skipped box %d' % random_box)
# fill_truck(1000, 1, 50)
# print("######################################################################################################################")
#
print("Привет, Богатырь!")
print("1: Налево пойдешь - коня потеряешь")
print("2: Направо пойдешь - полцарства найдешь")
print("3: Прямо пойдешь - мешок денег найдешь")

while True:
    user_choice = input("Сделай свой выбор [1-3], используй Q для выхода: ")
    if user_choice == "q":
        print("Заходи еще")
        break

    valid_input = True
    if not user_choice.isnumeric():
        valid_input = False

    # elif not int(user_choice) >= 1 and int(user_choice) <= 3:
    elif not 1 <= int(user_choice) <=3:
        valid_input = False

    if not valid_input:
        print("Сделай правильный выбор!!Сделай свой выбор [1-3], используй Q для выхода ")
        continue

    user_choice = int(user_choice)
    if user_choice == 1:
        print("Лошадку жалко ")

    elif user_choice == 2:
         print("Молодец")

    elif user_choice == 3:
         print("10% за подсказку!")
    else:
         print("Сделай правильный выбор!!Сделай свой выбор [1-3], используй Q для выхода ")
else:
        print("Сделай правильный выбор!!Сделай свой выбор [1-3], используй Q для выхода ")
