history = []

while True:
    user_input = input("select an operator or an action...(+ - * /  history exit): ")
    if user_input == "exit":
        print("Goodbye!")
        break

    elif user_input == "history":
        if not history:
            print("No history yet")
    
        else:
            for item in history:
                print(item)
    
    elif user_input in ["+", "-", "*", "/"]:
        num1 = float(input("type your first number here: "))
        num2 = float(input("type your second number here: "))

        if user_input == "+" :
            result = (num1 + num2)

        elif user_input == "-":
            result = (num1 - num2)
    
        elif user_input == "*":
            result = (num1 * num2)

        elif user_input == "/":
            result = (num1 / num2)
            
        print(result)
        history.append(f"{num1} {user_input} {num2} = {result}")
    
    else:
        print("Invalid entry,please try again")
    


    


    
    



