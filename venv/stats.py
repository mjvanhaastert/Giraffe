numb1 = float(input("enter first number: "))
op = input("enter operator: ")
numb2 = float(input("enter second number: "))

if op == "+":
    print(numb1 + numb2)
elif op == "-":
    print(numb1 - numb2)
elif op == "/":
    print(numb1 / numb2)
elif op == "*":
    print(numb1 * numb2)
else:
    print("Invalid operator!")