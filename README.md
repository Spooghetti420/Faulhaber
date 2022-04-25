# Faulhaber formula calculator
This program uses an implementation of Faulhaber's formula to calculate the formula for the below sum: [sum from 1 to n of k^p](https://wikimedia.org/api/rest_v1/media/math/render/svg/cdfa28bc350e73f808fc51da16d427df1a45fd28)

Formulas are given as a fractional factor multiplying a polynomial with integer coefficients, e.g. 1/6(2n^3 + 3n^2 + n).

(Sadly, this means we don't get to see the more fascinating incarnation of this formula, 1/6(n)(n+1)(2n+1), however...)

## Usage
Run the program:
`python calculator.py`

It will prompt for the desired p-value, the variable name to use (n by default), and whether to output fractions in the "normal" fashion — e.g. `1/6` — or to use the LaTeX-based `\frac` expression.  