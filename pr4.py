import random
from random import randint

#
# print("Угадай число!\n"
#        "Случайное число находится между 1 и 9\n"
#        "У вас есть 3 попытки!\n"
#        "Игра начинается...\n")
#
# num = random.randint(1, 9)
# ch = False
# for chance in range(3):
#      a = int(input("Введите число : "))
#
#      if a == num:
#          ch = True
#          break
#      elif a != num:
#          print(f"Вы не угадали! У вас еще {2 - chance} попытки")
# if ch:
#      print("Вы угадали!")
# else:
#     print("Попытки закончились. Загаданное число : ", a)


# 2 task
# print("Камень - ножницы - бумага!\n"
#        "Вы будете играть с компом сулифа\n"
#        "Комп уже выбрал!\n"
#        "Теперь твоя очередь...\n"
#         "1--- камень"
#         "2--- ножницы"
#         "3--- бумага")
#
# num = random.randint(1, 3)
#
# player_choice = int(input("Введите число : "))
# computer_choice = random.choice(["камень", "ножницы", "бумага"])
#
# print(f"Выбор бота:{num}")
#
# if player_choice == num:
#     print("Ничья")
# elif player_choice == 1:
#     if num == 2:
#         print("Вы победили!")
#     else:
#         print("Компьютер победил!")
# elif player_choice == 2:
#     if num == 3:
#         print("Вы победили")
#     else:
#         print("Вы проиграли")
# elif player_choice == 3:
#     if num == 1:
#         print("Вы победили")
#     else:
#         print("Вы проиграли")


# print("Введи номер в числовом формате")
# oper_num = input("Введите номер : ")
#
# if oper_num in ("727"):
#     print("You're using Activ")
# elif oper_num in ("700","708"):
#     print("You're using Altel 4G")
# elif oper_num in ("705", "771", "776", "777"):
#     print("You're using Beeline")
# elif oper_num in ("701", "702", "775", "778"):
#     print("You're using Kcell")
# elif oper_num in ("707", "747"):
#     print("You're using Tele2")


num1 = int(input("1st num :"))
num2 = int(input("2nd num : "))
op = input("operator : ")
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "//":
    print(num1 // num2)
elif op == "**":
    print(num1 ** num2)
elif op == "%":
    print(num1 % num2)

else:
    print("Error")