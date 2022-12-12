
# ПАЛИНДРОМ

name = input("Назовите Ваше имя")
print(f"Здравствуйте!", name)
s = input("""Напишите фразу,которую хотите проверить на палиндром
>>""")

print(s)

s = s.replace(" ", "").replace(".", "").replace("!", "").replace(",", "").replace(";", "").replace(":", "").replace("?", "")
print(s)
s = s.lower()
print(s.lower())
print(s[::-1])
s_test = s[::-1]
if s == s_test:
    print("Is a palindrome")
else:
    print("Is NOT a palindrome")
