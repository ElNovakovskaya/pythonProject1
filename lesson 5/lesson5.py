
sum = 0

while True:
   text = input("Введите число: ")
   if text == "sum":
      print("Сумма чисел=", sum)
      break
   try:
      sum = sum + int(text)
   except Exception:
      print("Неправильный фориат числа, попробуйте снова")
