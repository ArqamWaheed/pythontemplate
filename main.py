# bad_example.py


def MyFunc(x, y):  # bad: function name should be snake_case, weird spaces
    print("Sum is", x + y)  # bad: print usage flagged by T201
    return x + y  # bad: double space before x+y


def another_func():
    pass  # bad: wrong indentation (2 spaces)
