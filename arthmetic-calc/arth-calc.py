# Arithmetic calculator 
a = ["32 - 698", "3801 - 2", "45 + 43", "123 + 49"]



eq = []
values = []
operators = []
operand = []


if len(a) > 5: 
    print('Error: Too many problems.')

for i in a:
    eq += i.split()

for p in eq: 
    try:
        if int(p):
            if len(p) <=4:
                values.append(int(p))
            else:
                print("Error: Numbers cannot be more than four digits.")
                break
    except:
        if p == '-' or p == '+':
            operators.append(p)
        else:
            if len(p) > 1:
                print("Error: Numbers must only contain digits.")
                break
            else:    
                print("Error: Operator must be '+' or '-'.")
                break


print(operators , values)






#arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])