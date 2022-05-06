import math
import cmath

operator_list = ['+', '-']
polynomial_coefficients = []
polynomial_constant_factors = []
leading_coefficient_factors = []
polynomial_operators = []
polynomial_exponents = []
possible_roots_reciprocal = []
unfllipped_possible_roots = []
POLYNOMIAL_CONSTANT = 0


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


def factoring(polynomial_coefficients):
    global polynomial_constant_factors
    global leading_coefficient_factors
    polynomial_constant_factors = []
    leading_coefficient_factors = []

    for i in range(len(list_input) - list_input.count("+") - list_input.count("-") + 1):
        if i % 2 == 0:
            polynomial_coefficients.append(i)

        for x in range(0 - polynomial_coefficients[-1], polynomial_coefficients[-1] + 1):
            if x != 0:
                if polynomial_coefficients[-1] % x == 0:
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


def unfllipped_roots(leading_coefficient_factors, polynomial_constant_factors):
    global unfllipped_possible_roots
    unfllipped_possible_roots = [f'{x}/{y}' for x in leading_coefficient_factors for y in polynomial_constant_factors]
    return unfllipped_possible_roots


def reciprocal_roots(leading_coefficient_factors, polynomial_constant_factors):
    global possible_roots_reciprocal
    possible_roots_reciprocal = [f'{y}/{x}' for y in polynomial_constant_factors for x in leading_coefficient_factors]
    return possible_roots_reciprocal


# def plugin(possible_polynomial_roots):


# def syntheticdivision():


print("Welcome to Polynomial Equation Solver by:")
print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▀█▀▄▄▀█▀▄▄▀█░█▀█░███░█▀▄▄▀█░▄▄▀█░▄▀▄░████░▄▄▀██▄██▄░▄██
██░▄▄▀█░██░█░██░█░▄▀█▄▀░▀▄█░██░█░▀▀▄█░█▄█░█▄▄█░▄▄▀██░▄██░███
██░▀▀░██▄▄███▄▄██▄█▄██▄█▄███▄▄██▄█▄▄█▄███▄████▄▄▄▄█▄▄▄██▄███
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")

print(parse(list_input))
print(factoring(polynomial_coefficients))
possible_polynomial_roots = unfllipped_roots(leading_coefficient_factors, polynomial_constant_factors) + reciprocal_roots(leading_coefficient_factors, polynomial_constant_factors)