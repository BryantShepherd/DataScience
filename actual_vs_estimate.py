from matplotlib import pyplot as plt
from functools import partial
from intro_hypothesis_testing import normal_cdf
def sum_of_squares(v):
    return sum(v_i ** 2 for v_i in v)

def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def square(x):
    return x * x;

def derivative(x):
    return 2 * x;
derivative_estimate = partial(difference_quotient, square, h=0.00001);

x = range(-10, 10)
plt.title("Actual derivatives vs Estimates")
plt.plot(x, map(derivative, x), 'rx', label='Actual')
plt.plot(x, map(derivative_estimate, x), 'b+', label='Estimate')
plt.legend(loc=9)
plt.show()