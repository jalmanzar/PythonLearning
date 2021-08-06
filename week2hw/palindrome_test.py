import pytest

def palin_test():
    from palindrome import palin_brute

    assert palin_brute("aba") == True
