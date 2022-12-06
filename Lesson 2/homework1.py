
Nalog_1 = 3
Nalog_2 = 5

# user_choise = ("Назовите Ваше имя")
name = input("Назовите Ваше имя")
print(f"Здравствуйте!", name)

# input(f"Здравствуйте!", name)
# print("Здравствуйте!", name)

user_choise = input("""Укажите сумму дохода за отчетный период?
>>""")
user_choise = int(user_choise)
print(type(user_choise))
user_nalog = input("""Выбрать одно:
1.Ставка налога 3%
2.Ставка налога 5%
>>""")
user_nalog = str(user_nalog)
print(type(user_nalog))
if  (user_nalog == "1"):
    summ = round(user_choise /100* Nalog_1, 2)
    print(f"Вы должны заплатить налог в сумме {summ} грн")
if  (user_nalog == "2"):
    summ  = round(user_choise /100* Nalog_2, 2)
    print(f"Вы должны заплатить налог в сумме {summ} грн")
dohod = round(user_choise - summ, 2)
print(f"Вы должны задекларировать Чистый доход в сумме {dohod} грн")
print("Спасибо!")