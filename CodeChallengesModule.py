from decimal import Decimal, getcontext
import math


def isDigit(s):
    return s.isdigit()


def u_n_x(n, x):
    total = 0
    for i in range(1, n + 1):
        total += i * (x ** i)
    return total


class SeriesSolver:
    MAX_N = 1000  # Increase the maximum value of n

    @staticmethod
    def __series_sum(m, x):
        getcontext().prec = 100  # Set the precision for the decimal calculations
        total = Decimal(0)
        for n in range(1, SeriesSolver.MAX_N):
            if abs(x) < Decimal('1e-100'):  # Check if x is too small
                return total - Decimal(m)
            total += Decimal(n) * Decimal(x) ** Decimal(n)
        return total - Decimal(m)

    @staticmethod
    def __series_derivative(x):
        getcontext().prec = 100  # Set the precision for the decimal calculations
        total = Decimal(0)
        for n in range(1, SeriesSolver.MAX_N):
            if abs(x) < Decimal('1e-100'):  # Check if x is too small
                return total
            total += Decimal(n) * Decimal(x) ** Decimal(n - 1)
        return total

    @staticmethod
    def solve(m):
        # Use the Newton-Raphson method to find the root of the series_sum
        x = Decimal(0.5)  # Adjust the initial guess
        for _ in range(SeriesSolver.MAX_N):
            x_prev = x
            derivative = SeriesSolver.__series_derivative(x)
            if derivative != Decimal(0):  # Check if the derivative is not zero
                x = x - SeriesSolver.__series_sum(m, x) / derivative
            else:
                return None  # Return None if the derivative is zero
            if abs(x - x_prev) < Decimal(1e-6):  # Improve the convergence criterion
                break

        # Check whether the series converges to m
        if abs(SeriesSolver.__series_sum(m, x)) > Decimal(1e-12):
            return None

        return float(x)  # Convert the result back to a float


def f(x, m, n):
    x = Decimal(x)
    return x * (1 - x ** n) / (1 - x + Decimal('1e-12')) - Decimal(m)


def df(x, n):
    x = Decimal(x)
    return (n * x ** (n - 1) - n * x ** n - 1) / (1 - x + Decimal('1e-12')) ** 2


def solve(m):
    n = 1000  # define n as a constant within the function
    x = Decimal(0.7)  # initial guess
    getcontext().prec = 50  # set precision
    while abs(f(x, m, n)) > 1e-12:
        x = x - f(x, m, n) * (x - f(x, m, n) / f(x + f(x, m, n) - x, m, n))
    return float(x)


class Gps:
    @staticmethod
    def max_avg_speed(s, x):
        if len(x) <= 1:
            return 0

        speeds = []
        for i in range(1, len(x)):
            delta_distance = x[i] - x[i - 1]
            avg_speed = (3600 * delta_distance) / s
            speeds.append(avg_speed)

        return math.floor(max(speeds))
