def sleep_in(weekday, vacation):
    if vacation == True:
        return True
    if weekday == True:
        return False
    if weekday == False:
        return True

print(sleep_in(True, True))