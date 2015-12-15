print("Valid operations: +, -, *, /, ^, rt")
def ansDef(baseA, oper, baseB):
    numBRT = int(1) / int(baseB)
    if oper == "+":
        baseAns = int(baseA) + int(baseB)
    elif oper == "-":
        baseAns = int(baseA) - int(baseB)
    elif oper == "*":
        baseAns = int(baseA) * int(baseB)
    elif oper == "/":
        baseAns = int(baseA) / int(baseB)
    elif oper == "^":
        baseAns = int(baseA) ** int(baseB)
    elif oper == "rt":
        baseAns = int(baseA) ** int(numBRT)
    else:
        print("ERROR: INVALID OPERATION")
    ans = hex(baseAns).lstrip("0x") or "0"
    print(ans)
    return

inputA = input("Enter first number: ")
operation = input("Enter operation: ")
inputB = input("Enter second number: ")
intA = int(inputA, 16)
intB = int(inputB, 16)
ansDef(baseA=intA, oper=operation, baseB=intB)
