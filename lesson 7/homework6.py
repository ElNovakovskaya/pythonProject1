
A = []

while True:
    user_input = input("""
    >>""")
    A.append(user_input)

    print(sorted(A, key = len))


