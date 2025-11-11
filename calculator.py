try:

    a = int(input("enter first number"))
    b = int(input("enter second number"))
    print("whihc operation")
    op = input("enter operation")
    match op:
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            print(a / b)
        case _:
            print("invalid operation")

except Exception as e:
    print("enter vslid  and b")