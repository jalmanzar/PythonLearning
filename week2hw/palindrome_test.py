import pytest

def palin__brute_test():
    from palindrome import palin_brute

    assert palin_brute("aba") == True

def palin_expand_test():
    from palindrome import palin_expand

    assert palin_expand("aba") == True

print(palin__brute_test())