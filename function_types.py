import numpy as np


def parse_number(message):
    ini_x = input(message)
    if 'pi' in ini_x:
        ini_x = ini_x.replace('pi', str(np.pi))
    if 'π' in ini_x:
        ini_x = ini_x.replace('π', str(np.pi))
    if 'e' in ini_x:
        ini_x = ini_x.replace('e', str(np.e))
    x = float(ini_x)
    return x


class Function:

    @staticmethod
    def get_general_form():
        return 'y = NaN'

    def eval_at_x(self, x):
        return np.nan


class Polynomial(Function):

    def __init__(self, coefficients, degree):
        """

        :type degree: int
        :type coefficients: list
        """
        Function.__init__(self)
        self.coefficients = coefficients
        self.degree = degree

    def __str__(self):
        val = 'y = '
        for num in range(self.degree + 1):
            val += str(self.coefficients[num]) + ' * x ^ ' + str(self.degree - num)
            if num != self.degree:
                val += ' + '
        return val

    @staticmethod
    def get_general_form():
        return 'y = a_1 * x^n + a_2 * x^(n-1) + a_3 * x^(n-2) + ... + a_(n-2) * x^2 + a_(n-1) * x + a_n'

    @staticmethod
    def ask_for(name='Polynomial'):
        degree = int(input('What is the degree of your ' + str(name) + ' '))
        coefficients = []
        for x in range(degree + 1):
            coefficients.append(parse_number('What is the coefficient of the ' + str(degree - x) + ' degree term in '
                                                                                                   'your function '))
        function = Polynomial(coefficients, degree)
        return function

    def eval_at_x(self, x):
        y = 0
        for num in range(self.degree):
            y += self.coefficients[num] * x ** (self.degree - num)
        return y


class Rational(Function):

    def __init__(self, numerator, denominator):
        """

        :type numerator: Polynomial
        :type denominator: Polynomial
        """
        Function.__init__(self)
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        val = 'y = ' + self.numerator.__str__() + ' / ' + self.denominator.__str__()
        return val

    @staticmethod
    def ask_for():
        numerator = Polynomial.ask_for('Numerator')
        denominator = Polynomial.ask_for("Denominator")
        function = Rational(numerator, denominator)
        return function

    @staticmethod
    def get_general_form():
        return 'y = (a_1 * x^b + a_2 * x^(b-1) + a_3 * x^(b-2) + ... + a_(b-2) * x^2 + a_(b-1) * x + a_b) / ' \
               '(c_1 * x^d + c_2 * x^(d-1) + c_3 * x^(d-2) + ... + c_(d-2) * x^2 + c_(d-1) * x + c_d)'

    def eval_at_x(self, x):
        y = self.numerator.eval_at_x(x) / self.denominator.eval_at_x(x)
        return y


class Exponential(Function):

    def __init__(self, a, b):
        Function.__init__(self)
        self.a = a
        self.b = b

    def __str__(self):
        val = 'y = ' + self.a + ' * ' + self.b + ' ^ x'
        return val

    @staticmethod
    def ask_for():
        a = parse_number('What is a: ')
        b = parse_number('What is b: ')
        function = Exponential(a, b)
        return function

    @staticmethod
    def get_general_form():
        return 'y = a * b^x'

    def eval_at_x(self, x):
        y = self.a * self.b ** x
        return y


class Logarithmic(Function):

    def __init__(self, base):
        Function.__init__(self)
        self.base = base

    def __str__(self):
        val = 'y = log_' + self.base + '(x)'
        return val

    @staticmethod
    def ask_for():
        base = parse_number('What is the base: ')
        function = Logarithmic(base)
        return function

    @staticmethod
    def get_general_form():
        return 'y = log_base(x)'

    def eval_at_x(self, x):
        y = np.log(x) / np.log(self.base)
        return y


class Sine(Function):

    def __init__(self, a, b, c, d):
        Function.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        val = 'y = ' + self.a + ' * sin(' + self.b + ' * x - ' + self.c + ') + ' + self.d
        return val

    @staticmethod
    def ask_for():
        a = parse_number('What is a: ')
        b = parse_number('What is b: ')
        c = parse_number('What is c: ')
        d = parse_number('What is d: ')
        function = Sine(a, b, c, d)
        return function

    @staticmethod
    def get_general_form():
        return 'y = a * sin(b * x - c) + d'

    def eval_at_x(self, x):
        y = self.a * np.sin(self.b * x - self.c) + self.d
        return y


class Cosine(Function):

    def __init__(self, a, b, c, d):
        Function.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        val = 'y = ' + self.a + ' * cos(' + self.b + ' * x - ' + self.c + ') + ' + self.d
        return val

    @staticmethod
    def ask_for():
        a = parse_number('What is a: ')
        b = parse_number('What is b: ')
        c = parse_number('What is c: ')
        d = parse_number('What is d: ')
        function = Cosine(a, b, c, d)
        return function

    @staticmethod
    def get_general_form():
        return 'y = a * cos(b * x - c) + d'

    def eval_at_x(self, x):
        y = self.a * np.cos(self.b * x - self.c) + self.d
        return y


class Tangent(Function):

    def __init__(self, a, b, c, d):
        Function.__init__(self)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        val = 'y = ' + self.a + ' * tan(' + self.b + ' * x - ' + self.c + ') + ' + self.d
        return val

    @staticmethod
    def ask_for():
        a = parse_number('What is a: ')
        b = parse_number('What is b: ')
        c = parse_number('What is c: ')
        d = parse_number('What is d: ')
        function = Tangent(a, b, c, d)
        return function

    @staticmethod
    def get_general_form():
        return 'y = a * tan(b * x - c) + d'

    def eval_at_x(self, x):
        y = self.a * np.tan(self.b * x - self.c) + self.d
        return y
