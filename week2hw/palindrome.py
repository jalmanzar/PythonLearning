def palin_brute(set):
    pali = ""
    for i in range(len(set)):
        for j in range(len(set), i, -1):
            if set[i:j] == set[i:j][::-1]:
                if len(pali) < len(set[i:j]):
                    pali = set[i:j]
    return pali
        

def palin_expand(string):
    for i in string:
        return i

def teststring():
    string = "This is a test string"
    sliced = string[::-1]
    return sliced


print(teststring())