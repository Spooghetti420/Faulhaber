import fractions


def kronecker_delta(i, j):
    return int(i == j)

def factorial(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    
    return product

def binomial(n, r):
    return (factorial(n)//(factorial(r)*factorial(n-r)))

def bernoulli(n) -> fractions.Fraction:
    """
    Return B- ("B minus" — Bernoulli numbers with B(1) = -1/2 rather than +1/2)
    """
    # Partially derived from: https://rosettacode.org/wiki/Bernoulli_numbers#Python
    if n == 1:
        return fractions.Fraction(-1,2)
    b = [0 for _ in range(n + 1)]
    for m in range(n + 1):
        b[m] = fractions.Fraction(1, (m+1))
        for j in range(m, 0, -1):
            b[j-1] = j*(b[j-1]-b[j])
    return b[0]

def lowest_common_denominator(*fractions: fractions.Fraction):
    highest = {}
    for fraction in fractions:
        factors = prime_factorisation(fraction.denominator)
        for factor, order in factors.items():
            if factor not in highest:
                highest[factor] = order
            elif order > highest[factor]:
                highest[factor] = order

    product = 1
    for factor, order in highest.items():
        product *= factor ** order

    return product

def prime_factorisation(n):
    powers = {}
    i = 2
    while n > 1:
        if n % i == 0:
            n //= i
            try:
                powers[i] += 1
            except KeyError:
                powers[i] = 1
        elif i == 2:
            i = 3
        else:
            i += 2
            while not is_prime(i):
                i += 2 
    return powers

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False

    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def faulhaber(p, variable="n", fraction_mode = "standard") -> str:
    """
    Returns a string that represents the formula for the sum of k^p from 1 to `variable`,
    a value of the user's choice (such as n). The `fraction_mode` value can either be
    `standard` or `latex`: the former produces e.g. `1/6`, whereas the latter `\frac{1}{6}`.
    """
    if fraction_mode not in ("standard", "latex"):
        raise ValueError(f"Fraction mode must be one of 'standard' or 'latex', not {fraction_mode}.")
    
    if len(variable) > 1:
        variable = f"({variable})"

    coefficients = [[i, (-1)**(kronecker_delta(i, p)) * binomial(p + 1, i) * bernoulli(p+1-i)] for i in range(p + 1, 0, -1)]
    coefficients = [c for c in coefficients if c[1] != 0]
    lcd = lowest_common_denominator(*[c[1] for c in coefficients])
    for c in coefficients:
        c[1] *= lcd

    output = f"{fractions.Fraction(1, (p+1)*lcd)}(" if fraction_mode == "standard" else f"\\frac{{1}}{{{(p+1)*lcd}}}("
    for i, c in enumerate(coefficients):
        if c[0] == 0:
            continue
        
        power = len(coefficients) - i
        output += f"{abs(c[1]) if c[1] != 1 else ''}{variable}{f'^{power}' if power != 1 else ''}" if c[1] != 0 else ""
        if i != len(coefficients) - 1:
            if coefficients[i+1][1] == 0:
                continue
            output += " + " if coefficients[i+1][1] > 0 else " - "
    output += ")"

    return output

def main():
    p = None
    while p is None:
        try:
            p = int(input("Please input a power to get the partial sum for: "))
        except ValueError:
            pass
    
    var = input("Please enter a variable (n by default): ")
    var = "n" if var == "" else var

    fraction_format = input("Please enter what fraction format you would like ('standard'/'latex', standard by default): ")
    if fraction_format not in ("standard", "latex"):
        fraction_format = "standard"

    print(faulhaber(p, var, fraction_format))

if __name__ == "__main__":
    main()