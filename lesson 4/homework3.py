

user_input_1 = {
    "hello",
    "привіт",
    "доброго дня"
}
user_input_2 = {
    "як справи?",
    "що робиш?",
    "чим займаєшся?"
}
user_input_3 = {
    "бувай",
    "гудбай",
    "до зустрічі"
}

bot_answer_1 = 'Доброго вечора, я бот з України!'
bot_answer_2 = 'Вчусь програмувати на Python!'
bot_answer_3 = 'Побачимось у мережі, I\'ll be back'
bot_answer_error = 'Дуже цікаво, але, нажаль, нічого не зрозуміло'

while True:
    user_input = input("""
    >>""")
    if user_input.lower() in user_input_1:
        print(bot_answer_1)
    elif user_input.lower() in user_input_2:
        print(bot_answer_2)
    elif user_input.lower() in user_input_3:
        print(bot_answer_3)
        break
    else:
        print(bot_answer_error)



