from math_series import __version__
# from math_series.series import sum_series
from math_series.series import lucas
from math_series.series import fibonacci

def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_9():
    expected=34
    actual=fibonacci(9)
    assert expected == actual

def test_fibonacci_15():
    expected = 610
    actual= fibonacci(15)
    assert expected == actual

def test_lucas_10():
    expected = 123
    actual=lucas(10)
    assert expected == actual