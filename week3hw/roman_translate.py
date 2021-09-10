def roman_translate(text):
    r_numerals = {"I" : 1,
                 "V" : 5,
                 "X" : 10}
    result = 0

    for i in range(len(text)):
        result += r_numerals[text[i]]
    for i in range(len(text)-1):
        if text[i] == "I" and (r_numerals[text[i]] < r_numerals[text[i+1]]):
            result = result - 2
    
    return result

print(roman_translate("XIV"))
print(roman_translate("XXI"))