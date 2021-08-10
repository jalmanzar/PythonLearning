import pytest

def palin__brute_test():
    from palindrome import palin_brute

    assert palin_brute("aba") == True

def palin_conven_test():
    from palindrome import palin_conven

    assert palin_conven("aba") == True