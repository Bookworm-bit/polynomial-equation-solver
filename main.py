import math
import cmath

operator_list = ['+', '-']
polynomial_coefficients = []
polynomial_constant_factors = []
leading_coefficient_factors = []
polynomial_operators = []
polynomial_exponents = []
possible_roots_reciprocal = []
unflipped_possible_roots = []
possible_polynomial_roots = []
POLYNOMIAL_CONSTANT = 0
PLUG_IN_LIST = []
roots = []
zeroes = []


def parse(list_input):
    for item in list_input:
        if item[0] == 'x':
            polynomial_coefficients.append(1)

        if item[0] != 'x' and item not in operator_list:
            partit = item.partition("x")
            polynomial_coefficients.append(int(partit[0]))

        if "x" not in item and item not in operator_list:
            global POLYNOMIAL_CONSTANT
            POLYNOMIAL_CONSTANT += int(item)

        if item in operator_list:
            polynomial_operators.append(item)

        if item not in operator_list:
            if "^" in item and "x" in item:
                polynomial_exponents.append(int(item.partition("x^")[len(item) - 1]))
            if "x" in item and "^" not in item:
                polynomial_exponents.append(1)

            if "x" not in item and "^" not in item:
                polynomial_exponents.append(0)
        
        if len(polynomial_coefficients) - len(polynomial_operators) == 2:
            polynomial_operators.insert(0, '+')

    return polynomial_coefficients, polynomial_operators, polynomial_exponents, POLYNOMIAL_CONSTANT

og = input("Enter your polynomial equation: ")
list_input = og.split(' ')


def factoring(polynomial_coefficients, polynomial_constant_factors, leading_coefficient_factors):
    for i in range(len(list_input) - list_input.count("+") - list_input.count("-") + 1):
        if i % 2 == 0:
            polynomial_coefficients.append(i)

    for x in range(0 - POLYNOMIAL_CONSTANT, POLYNOMIAL_CONSTANT + 1):
        if x != 0:
            if int(POLYNOMIAL_CONSTANT) % x == 0:
                polynomial_constant_factors.append(x)

    for i in range(0 - polynomial_coefficients[0], polynomial_coefficients[0] + 1):
        leading_coefficient_factors.append(i)

    try:
        leading_coefficient_factors.remove(None)
        polynomial_constant_factors.remove(None)
    except ValueError:
        pass

    # try:
    #     if int(diction['0coefficient']) > 0:
    #         for item in leading_coefficient_factors:
    #             if int(item) < 0:
    #                 leading_coefficient_factors.remove(item)

    #     for item in diction.keys():
    #         if int(item) < 0 and 'C:' in item:
    #             for item in polynomial_constant_factors:
    #                 if int(item) > 0:
    #                     polynomial_constant_factors.remove(item)
    # except ValueError:
    #     pass

    return leading_coefficient_factors, polynomial_constant_factors


def unflipped_roots(leading_coefficient_factors, polynomial_constant_factors, unflipped_possible_roots):
    unflipped_possible_roots = [f'{x}/{y}' for x in leading_coefficient_factors for y in polynomial_constant_factors]
    for item in unflipped_possible_roots:
        if '/0' in item:
            unflipped_possible_roots.remove(item)

    return unflipped_possible_roots


def reciprocal_roots(leading_coefficient_factors, polynomial_constant_factors, possible_roots_reciprocal):
    possible_roots_reciprocal = [f'{y}/{x}' for y in polynomial_constant_factors for x in leading_coefficient_factors]
    for item in possible_roots_reciprocal:
        if '/0' in item:
            possible_roots_reciprocal.remove(item)

    return possible_roots_reciprocal


def plug_in_setup(list_input, PLUG_IN_LIST):
    for item in list_input:
        if '^' in item and 'x' in item:
            if item[0] == 'x':
                PLUG_IN_LIST.append(item.replace('x^', '1 * (x) ** '))
            if item[0] != 'x':
                PLUG_IN_LIST.append(item.replace('x', '* (x) ** '))
        
        if 'x' not in item and '^' not in item:
            PLUG_IN_LIST.append(item)
    
    return(PLUG_IN_LIST)
    

def plug_in(possible_polynomial_roots, zeroes, PLUG_IN_LIST): 
    for item in possible_polynomial_roots:
        if eval(''.join(PLUG_IN_LIST).replace('x', item)) == 0:
            zeroes.append(eval(item))

    return(zeroes)


def zero_cleaner(zeroes, roots):
    for item in zeroes:
        if item not in roots:
            roots.append(item)


# def synthetic_division():


print("Welcome to Polynomial Equation Solver by:")
print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▀█▀▄▄▀█▀▄▄▀█░█▀█░███░█▀▄▄▀█░▄▄▀█░▄▀▄░████░▄▄▀██▄██▄░▄██
██░▄▄▀█░██░█░██░█░▄▀█▄▀░▀▄█░██░█░▀▀▄█░█▄█░█▄▄█░▄▄▀██░▄██░███
██░▀▀░██▄▄███▄▄██▄█▄██▄█▄███▄▄██▄█▄▄█▄███▄████▄▄▄▄█▄▄▄██▄███
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")

print(parse(list_input))

print(factoring(polynomial_coefficients, polynomial_constant_factors, leading_coefficient_factors))

print(plug_in_setup(list_input, PLUG_IN_LIST))

possible_polynomial_roots = unflipped_roots(
    leading_coefficient_factors,
    unflipped_possible_roots, 
    polynomial_constant_factors) + reciprocal_roots(
    leading_coefficient_factors, 
    possible_roots_reciprocal,
    polynomial_constant_factors)

print(possible_polynomial_roots)

plug_in(possible_polynomial_roots, zeroes, PLUG_IN_LIST)

zero_cleaner(zeroes, roots)

print(roots)