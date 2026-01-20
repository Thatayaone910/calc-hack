def calculator():
    history = []

    while True:
        user_input = input("Enter equation: ")

        if user_input == "exit":
            break
       
        try:
            result = eval(user_input)
            print(result)
        except:
            print("Inavild Operator")
    return
calculator()