
def check_condition(string):
    if (string[0] not in "aeiou") and (string == string.lower()):
        if string.isalpha():
            return True
    return False
def exract_string(string_list):

    result = [string for string in string_list if check_condition(string)]
    return result

string_list = ["Hello", "123", "AI", "Coding","moin","moin.","moin#","apple"]

print(exract_string(string_list))

#output : ['moin']

