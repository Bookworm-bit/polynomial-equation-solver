import math
import cmath

operator = ['+', '-']
diction = {}

def listMake(listy):
    for item in listy:
        if item[0] == 'x':
            diction[str(listy.index(item)) + 'coefficient'] = "1"
        if item[0] != 'x' and item not in operator:
            partit = [item.partition("x")]
            diction[str(listy.index(item)) + 'coefficient'] = str(partit[0])
        if "x" not in item and item not in operator:
            diction[str(listy.index(item)) + 'coefficient'] = f'C: {item}'
        if item in operator:
            diction[str(listy.index(item)) + 'power'] = item
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
    

print("Welcome to Polynomial Equation Solver by:")
print("""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▀█▀▄▄▀█▀▄▄▀█░█▀█░███░█▀▄▄▀█░▄▄▀█░▄▀▄░████░▄▄▀██▄██▄░▄██
██░▄▄▀█░██░█░██░█░▄▀█▄▀░▀▄█░██░█░▀▀▄█░█▄█░█▄▄█░▄▄▀██░▄██░███
██░▀▀░██▄▄███▄▄██▄█▄██▄█▄███▄▄██▄█▄▄█▄███▄████▄▄▄▄█▄▄▄██▄███
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")

og = input("Enter your polynomial equation: ")
listy = og.split(' ')

print(listMake(listy))