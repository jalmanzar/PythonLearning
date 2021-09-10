def roman_translate(text):
    r_numerals = {"I" : 1,
                 "V" : 5,
                 "X" : 10}
    result = 0

    for i in text:
        result += r_numerals[i]
    for i in text:
        if i == "I" and (r_numerals[i] < r_numerals[i+1]):
            result = result - 2
    
    return result

print(roman_translate("XIV"))