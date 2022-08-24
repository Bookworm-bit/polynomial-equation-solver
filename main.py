from Term import Term

# import math
import re
# import colorama


def combine_like_terms(polynomial):
    for (t1, idx) in enumerate(polynomial):
        if isinstance(t1, Term):
            for (t2, jdx) in enumerate(polynomial):
                if isinstance(t2, Term):
                    if t2.exp == t1.exp:
                        polynomial[idx] = t1 + t2
                        polynomial.pop(jdx)
                        continue
    return polynomial


def get_factors(number):
    factors = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(-1 * i)
            factors.append(number // i)
            factors.append(-1 * (number // i))
    return factors


def get_possible_roots(leading_coeff_factors, constant_term_factors):
    return [t3 / t4 for (t3, t4) in zip(constant_term_factors, leading_coeff_factors)]


def test_possible_roots(possible_roots, polynomial):
    working_roots = []
    for r in possible_roots:
        term_values = 0
        for t in polynomial.pop():
            term_values += t.plugin(r)
        if term_values + polynomial[-1] == 0:
            working_roots.append(r)
    return working_roots


def main():
    print("Welcome to Polynomial Equation Solver by:")
    print("""
    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    ██░▄▄▀█▀▄▄▀█▀▄▄▀█░█▀█░███░█▀▄▄▀█░▄▄▀█░▄▀▄░████░▄▄▀██▄██▄░▄██
    ██░▄▄▀█░██░█░██░█░▄▀█▄▀░▀▄█░██░█░▀▀▄█░█▄█░█▄▄█░▄▄▀██░███░███
    ██░▀▀░██▄▄███▄▄██▄█▄██▄█▄███▄▄██▄█▄▄█▄███▄████▄▄▄██▄▄▄██▄███
    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    """)

    while True:
        print("Type 'exit' to exit.")
        polynomial = input("Enter a polynomial: ").strip().split(" ")

        if polynomial == ['exit']:
            print("Goodbye!")
            break
        if re.match(r'^-[0-9]+', polynomial[0]):
            print("You entered a number")
            print("This program will not work with single numbers")
            print("Please enter a polynomial with a degree greater than 0.")
            continue

        for (t, idx) in enumerate(polynomial):
            EXP = 0
            COEFF = 0

            if 'x' in str(t):
                if '^' not in str(t):
                    polynomial[idx] = str(t) + '^1'
                    COEFF = int(t.removesuffix('x'))
                    EXP = 1
                else:
                    COEFF = int(t.removesuffix('x'))
                    EXP = int(t.removeprefix('^'))

                polynomial[idx] = Term(COEFF, EXP)
            else:
                polynomial[idx] = int(t)

        if 'x' in polynomial[-1]:
            polynomial.append(0)

        polynomial = combine_like_terms(polynomial)
        leading_coeff = polynomial[0].coeff
        constant_term = polynomial[-1]

        leading_coeff_factors = get_factors(leading_coeff)
        constant_term_factors = get_factors(constant_term)

        possible_roots = get_possible_roots(leading_coeff_factors, constant_term_factors)

        roots = test_possible_roots(possible_roots, polynomial)

        print(roots)



if __name__ == '__main__':
    main()
