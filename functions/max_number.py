numbers = [2,100,3,12,313,44,33,22]

def min_max_num(l):
    biggest = l[0]
    smallest = l[0]
    for x in l:
        if x > biggest:
            biggest = x
        if x < smallest:
            smallest = x
    return biggest, smallest

print(min_max_num(numbers))

