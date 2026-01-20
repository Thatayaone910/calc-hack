history = []


while True:
    user_input = input("Enter equation: ")

    if user_input == "exit":
        break

    parts = user_input.split()

    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])