import math
import cmath

operator = ['+', '-'] # accepted operators
coefficients = []
operators = []
powers = []
const = 0

def listMake(listy):
    for item in listy:
        if item[0] == 'x':
            coefficients.append(1)
        if item[0] != 'x' and item not in operator:
            partit = item.partition("x")
            coefficients.append(int(partit[0]))
        if "x" not in item and item not in operator:
            const += int(item)
        if item in operator:
            operators.append(int(item))
        if item not in operator:
            powers.append(int(item.partition("x^")[1]))
            if "x" in item and "^" not in item:
                powers.append(1)
            if "x" not in item and "^" not in item:
                powers.append(0)
    return coefficients, operators, powers, const

og = input("Enter your polynomial equation: ")
listy = og.split(' ')

def factorFind(coefficients, powers):
    global constantFac
    global leadcoeffFac
    constantFac = []
    leadcoeffFac = []
    coeff = []
    for i in range(len(listy) - listy.count("+") - listy.count("-") + 1):
        if i % 2 == 0:
            coeff.append(i)
        for x in range(0 - coefficients[-1], coefficients[-1] + 1):
            if x != 0:
                if coefficients[-1] % x == 0:
                    constantFac.append(x)
    for i in range(0 - coefficients[0], coefficients[0] + 1):
        leadcoeffFac.append(i)
    try:
        leadcoeffFac.remove(None)
        constantFac.remove(None)
    except ValueError:
        pass
    # try:
    #     if int(diction['0coefficient']) > 0:
    #         for item in leadcoeffFac:
    #             if int(item) < 0:
    #                 leadcoeffFac.remove(item)
    #     for item in diction.keys():
    #         if int(item) < 0 and 'C:' in item:
    #             for item in constantFac:
    #                 if int(item) > 0:
    #                     constantFac.remove(item)
    # except ValueError:
    #     pass
    return leadcoeffFac, constantFac

def combine(leadcoeffFac, constantFac):
    global comb
    comb = [f'{x}/{y}' for x in leadcoeffFac for y in constantFac]
    return comb

def recip(leadcoeffFac, constantFac):
    global recip
    recip = [f'{y}/{x}' for y in constantFac for x in leadcoeffFac]
    return recip

poss = comb + recip

#def test(poss):


# def synthetic()



print("Welcome to Polynomial Equation Solver by:")
print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▀█▀▄▄▀█▀▄▄▀█░█▀█░███░█▀▄▄▀█░▄▄▀█░▄▀▄░████░▄▄▀██▄██▄░▄██
██░▄▄▀█░██░█░██░█░▄▀█▄▀░▀▄█░██░█░▀▀▄█░█▄█░█▄▄█░▄▄▀██░▄██░███
██░▀▀░██▄▄███▄▄██▄█▄██▄█▄███▄▄██▄█▄▄█▄███▄████▄▄▄▄█▄▄▄██▄███
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")
print(listMake(listy))
print(factorFind(coefficients))
print(combine(leadcoeffFac, constantFac))
print(recip(leadcoeffFac, constantFac))