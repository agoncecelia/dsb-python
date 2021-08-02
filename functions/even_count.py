numbers = [2,100,3,12,313,44,33,22]

def even_sum(l):
    even_sum = 0
    for x in l:
        if x % 2 == 0:
            even_sum +=1
    return even_sum

print("There are", even_sum(numbers), "even numbers.")
