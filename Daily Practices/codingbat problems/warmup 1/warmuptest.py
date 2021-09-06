import pytest
from warmup1 import sleep_in

def testfunction():
    assert sleep_in(True, True) == True
    assert sleep_in(True, False) == False
    assert sleep_in(False, True) == True