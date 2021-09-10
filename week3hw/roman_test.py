import pytest
from romantranslate import romannumerals

def roman_test():
    assert romannumerals("XIV") == 14
    assert romannumerals("III") == 3
    assert romannumerals("V") == 5
    assert romannumerals ("X") == 10