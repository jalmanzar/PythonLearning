import pytest
from roman_translate import roman_translate

def test_roman():
    assert roman_translate("XIV") == 14
    assert roman_translate("III") == 3
    assert roman_translate("V") == 5
    assert roman_translate ("X") == 10