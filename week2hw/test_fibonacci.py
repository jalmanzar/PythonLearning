import pytest

def calc_test():
    from fibonacci import fibonacci_calc
  
    assert fibonacci_calc(5) == 17
    assert fibonacci_calc(8) == 21

def recur_test():
    from fibonacci import fibonacci_recur

    assert fibonacci_recur(5) == 5
    assert fibonacci_recur(8) == 21

