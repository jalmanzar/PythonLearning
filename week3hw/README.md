Problem statement:
Translate roman numerals to integers.

Example:
XIV = 14
IV = 4
X = 10
III = 3
IX = 9

How would I do this by hand?

I'd first decide what all of the symbols mean, and probably reference that. What this would look like is probably creating a dictionary of all of the assosciated values.

Then, I'd translate a roman numeral by parsing through it character by character.

In the example of XIV, I would translate X as 10, then add that to a "result." Translate I as 1 and add that to the "result." Check V and notice it's larger than I, which would mean I'd need to subtract Ix2 from the result. Then translate V as 5 and add to the result.

Pseudocode:
- Am supplied XIV
    - Translate X as 10, add to result
        - result == 10
    - Translate I as 1, add to result
        - result == 11
    - Translate V as 5, add to result
        - result == 16
    - Check any indexes and see the index before is smaller
        - subtract nx2 from result
    - I < V, subtract 1x2 from result
        - result == 14

Possible optimization:
    Check if the index is "I", check to see if next index is bigger, and subtract I from the result if it is. Continue the program.

Better Pseudocode? Just different:
- Am supplied XIV
    - Check if index is I
        - Translate X as 10, add to result
            - result == 10
    - Check if index is I
        - Is I, compare to next index
        - Is smaller than n + 1
            - Translate I as -1, add to result
            - result == 9
     - Check if index is I
        - Translate V as 5, add to result
            - result == 14

===================== First unit test error

roman_test.py F                                                                                                                                                                    [100%]

======================================================================================== FAILURES ========================================================================================
_______________________________________________________________________________________ test_roman _______________________________________________________________________________________

    def test_roman():
        assert roman_translate("XIV") == 14
>       assert roman_translate("III") == 3
E       AssertionError: assert -3 == 3
E        +  where -3 = roman_translate('III')

roman_test.py:6: AssertionError
================================================================================ short test summary info =================================================================================
FAILED roman_test.py::test_roman - AssertionError: assert -3 == 3
=================================================================================== 1 failed in 0.12s ====================================================================================

Looks like I need to fix the logic so that consecutive Is don't subtract from each other.