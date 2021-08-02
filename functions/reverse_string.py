name = "Agon"

def reverse_string(s):
    hold = ""
    for x in s:
        hold = x + hold
    return hold

print(reverse_string(name))
