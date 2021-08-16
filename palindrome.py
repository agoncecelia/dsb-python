def check_palindrome(str):
    reversed = ""
    for x in str:
        reversed = x + reversed
    if reversed.lower() == str.lower():
        return True
    print(reversed.lower())
    return False

print(check_palindrome("Ramus aga sumar"))
