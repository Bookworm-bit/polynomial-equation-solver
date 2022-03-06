import math
import cmath

coeff = []
operator = ['+', '-']
operList = []
powers = []

def listMake(listy):
    for item in listy:
        if item[0] == 'x':
            coeff.append(1)
        if item[0] != 'x' and item not in operator:
            partit = item.partition("x")
            coeff.append(partit[0])
        if "x" not in item and item not in operator:
            coeff.append(f'C: {item}')
        if item in operator:
            operList.append(item)
        if coeff[listy.index(item)] != 1:
            if "^" in item:
                powers.append(int(item.removeprefix(str(coeff[listy.index(item)]) + 'x^')))
        if coeff[listy.index(item)] == 1:
            if "^" in item:
                powers.append(item.removeprefix('x^'))
        if "x" in item and "^" not in item:
            powers.append(1)
        if "x" not in item and "^" not in item:
            powers.append(0)
    return(coeff, powers, operList)

print("Welcome to Polynomial Equation Solver by:")
print("""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▀█▀▄▄▀█▀▄▄▀█░█▀█░███░█▀▄▄▀█░▄▄▀█░▄▀▄░████░▄▄▀██▄██▄░▄██
██░▄▄▀█░██░█░██░█░▄▀█▄▀░▀▄█░██░█░▀▀▄█░█▄█░█▄▄█░▄▄▀██░▄██░███
██░▀▀░██▄▄███▄▄██▄█▄██▄█▄███▄▄██▄█▄▄█▄███▄████▄▄▄▄█▄▄▄██▄███
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")

og = input("Enter your polynomial equation:")
listy = og.split(' ')

print(listMake(listy))

