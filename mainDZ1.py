
#1 задание

# просим пользователя ввести количество секунд
# time_volume_in_sek = input('Введите количество секунд')
# day = (int(time_volume_in_sek) // 86400)
# hour = ((int(time_volume_in_sek) // 3600 )% 24)
# minute = ((int(time_volume_in_sek) // 60)% 60)
# secund = (int(time_volume_in_sek) % 60)
# print(str(day ) + (" дней ") + str(hour ) + (" часов ") + str(minute ) + (" минут ") + str(secund ) + (" секунд ") )


#2 задание



# my_cube_list = []
# for number in range(1, 1001, 2):
#     my_cube_list.append(number ** 3)
#
# for my_cube in my_cube_list:
#     print(my_cube)
#     final_sum_cube = 0
#     sum_single_int = 0
#
#     for single_int in str(my_cube):
#         # print(single_int)
#         sum_single_int = sum_single_int + int(single_int)
#
#     if int(sum_single_int) % 7 != 0:
#         print(str(sum_single_int) + " на 7 нацело не делится fail")
#
#     else:
#         print(str(sum_single_int) + "  делится нацело на 7 bingo!")
#     final_sum_cube = final_sum_cube + my_cube
# print("-------------------")
# print("Сумма кубов чисел, сумма цифр которых делится нацело на 7 = " + str(final_sum_cube))
# print("-------------------")

#Вариант 2
# my_cube_list2 = [x + 17 for x in my_cube_list]
# for my_cube in my_cube_list2:
#     print(my_cube)
#     final_sum_cube = 0
#     sum_single_int = 0
#
#     for single_int in str(my_cube):
#         # print(single_int)
#         sum_single_int = sum_single_int + int(single_int)
#
#     if int(sum_single_int) % 7 != 0:
#         print(str(sum_single_int) + " на 7 нацело не делится fail")
#
#     else:
#         print(str(sum_single_int) + "  делится нацело на 7 bingo!")
#     final_sum_cube = final_sum_cube + my_cube
# print("-------------------")
# print("Сумма кубов чисел, сумма цифр которых делится нацело на 7 = " + str(final_sum_cube))
# print("-------------------")



# #3 задание

# for i in range(1, 101):
#     if i % 10 == 1 and i != 11:
#         print(str(i) + " процент")
#     elif i % 10 in (2, 3, 4) and i not in (12, 13, 14):
#         print(str(i) + " процента")
#     else:
#         print(str(i) + " процентов")






