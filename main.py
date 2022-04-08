import math
import cmath

operator = ['+', '-'] # accepted operators
diction = {} # dictionary of the elements of the equation

def listMake(listy): # turn the elements of the equation into a dictionary
    for item in listy:
        if item[0] == 'x':
            diction[str(listy.index(item)) + 'coefficient'] = "1"
        if item[0] != 'x' and item not in operator:
            partit = item.partition("x")
            diction[str(listy.index(item)) + 'coefficient'] = str(partit[0])
        if "x" not in item and item not in operator:
            diction[str(listy.index(item)) + 'coefficient'] = f'C: {item}'
        if item in operator:
            diction[str(listy.index(item)) + 'operator'] = item
        if item not in operator:
            if diction[str(listy.index(item)) + 'coefficient'] != "1":
                if "^" in item:
                    diction[str(listy.index(item)) + 'power'] = item.removeprefix(str(diction[str(listy.index(item)) + 'coefficient']) + 'x^')
            if diction[str(listy.index(item)) + 'coefficient'] == "1":
                if "^" in item:
                    diction[str(listy.index(item)) + 'power'] = item.removeprefix('x^')
            if "x" in item and "^" not in item:
                diction[str(listy.index(item)) + 'power'] = "1"
            if "x" not in item and "^" not in item:
                diction[str(listy.index(item)) + 'power'] = "0"
    return diction

og = input("Enter your polynomial equation: ")
listy = og.split(' ')

def factorFind(diction):
    constantFac = 0
    leadcoeffFac = 0
    coeff = []
    for i in range(len(listy) - listy.count("+") - listy.count("-") + 1):
        if i % 2 == 0:
            coeff.append(diction[str(i) + 'coefficient'])
    for value in diction.values():
        if 'C:' in value:
            for x in range(0 - int(value.removeprefix("C: ")), (int(value.removeprefix("C: "))) + 1):
                if int(value.removeprefix("C: ")) % x == 0:
                    constantFac = x
    for i in range(0 - int(diction.get('0coefficent')), int(diction.get('0coefficient') + 1)):
        print("hate you dad")
        

print("Welcome to Polynomial Equation Solver by:")
print("""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▀█▀▄▄▀█▀▄▄▀█░█▀█░███░█▀▄▄▀█░▄▄▀█░▄▀▄░████░▄▄▀██▄██▄░▄██
██░▄▄▀█░██░█░██░█░▄▀█▄▀░▀▄█░██░█░▀▀▄█░█▄█░█▄▄█░▄▄▀██░▄██░███
██░▀▀░██▄▄███▄▄██▄█▄██▄█▄███▄▄██▄█▄▄█▄███▄████▄▄▄▄█▄▄▄██▄███
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")
print(listMake(listy))
print(factorFind(diction))
