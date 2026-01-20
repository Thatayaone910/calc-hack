history = []


while True:
    user_input = input("Enter equation: ")

    if user_input == "exit":
        break

    parts = user_input.split()

    if len(parts) != 3:
        print("Format must be: Number Space Operator Space Number")
        continue

    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    
    
    if operator == "+":
        print(num1 + num2)
    
    elif operator == "-":
        print(num1 - num2)
    
    elif operator == "*":
        print(num1 * num2)

    elif operator == "/":
        print(num1 / num2)
    else:
        print("Inavild Operator")