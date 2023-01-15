
sum = 0

while True:
   text = input("Введите число: ")
   if text == "sum":
      print("Сумма чисел=", sum)
      break
   try:
      sum = sum + float(text)
   except Exception:
      print("Введіть число або sum будь-ласка!")
