import numpy as np  # Copyright (c) 2005-2019, NumPy Developers.
                    # All rights reserved.
import matplotlib.pyplot as plt  # Copyright (c) 2012- Matplotlib Development Team;
                                 # All Rights Reserved
import function_types as ft

function_types = [('Polynomial', ft.Polynomial.get_general_form()),
                  ('Rational', ft.Rational.get_general_form()),
                  ('Exponential', ft.Exponential.get_general_form()),
                  ('Logarithmic', ft.Logarithmic.get_general_form()),
                  ('Sine', ft.Sine.get_general_form()),
                  ('Cosine', ft.Cosine.get_general_form()),
                  ('Tangent', ft.Tangent.get_general_form())]  # List of the names of different functions and their
                                                              # general forms



def plot():
    """
    Asks the user to input a function and plots the given function
    :return: null
    """
    func_asked = input('Select a general form for your function or see the list of function types by typing `Types` ')
    if func_asked == 'Types':
        for type in function_types:
            print(type[0] + '\t' + type[1])
    elif func_asked == 'Polynomial':
        function = ft.Polynomial.ask_for()
    elif func_asked == 'Rational':
        function = ft.Rational.ask_for()
    elif func_asked == 'Exponential':
        function = ft.Exponential.ask_for()
    elif func_asked == 'Logarithmic':
        function = ft.Logarithmic.ask_for()
    elif func_asked == 'Sine':
        function = ft.Sine.ask_for()
    elif func_asked == 'Cosine':
        function = ft.Cosine.ask_for()
    elif func_asked == 'Tangent':
        function = ft.Tangent.ask_for()
    else:
        print('Unrecognized function type')
        exit()

    x_min = ft.parse_number('What is the minimum x value to plot: ')
    x_max = ft.parse_number('What is the maximum x value to plot: ')

    x = np.linspace(int(x_min), int(x_max), int(20 * (x_max - x_min)))
    y = []

    print('x\ty')
    for i in x:
        y.append(function.eval_at_x(i))
        print(str(round(i, 2)) + '\t' + str(round(y[len(y) - 1], 2)))

    plt.plot(x, y)
    plt.title(function)
    plt.grid()
    plt.show()


plot()
