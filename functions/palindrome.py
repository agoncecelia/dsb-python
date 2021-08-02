palindrome = 'Talat'

def check_palindrome(string):
    hold = ""
    for x in string:
        hold = x + hold

    if string.lower() == hold.lower():
        return True
    return False

print(check_palindrome(palindrome))
