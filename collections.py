#set1 = set([1,2,3,4])
#set2 = {5,6,7,8,4}
#print(set1 | set2)
#print(set1 & set2)
#print(set1 - set2)
#print(set1 ^ set2)
#
#weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Friday')
#print(weekdays[0])
#
#print(weekdays)
#
#student = {
#    "name": "Agon Cecelia",
#    "courses": ["1001", "1002", "2003"],
#    "email": "agonn.c@gmail.com",
#    "id": "10012332"
#}

""" me e kriju ni funksion qe pranon liste si argument dhe kthen nje dictionary ne kete forme:

{
    "odd": {
        "list": [1,3,5,7],
        "sum": 16,
        "len_of_list": 4
    },
    "even": {
        "list": [2,4,6],
        "sum": 12,
        "len_of_list": 3
    }
}
"""
""" check if a string is palindrome returns true or false"""

def list_filter(l):
    odd_list = []
    even_list = []
    odd_sum = 0
    even_sum = 0
    for x in l:
        if x % 2 == 0:
            even_list.append(x)
            even_sum += x
        else:
            odd_list.append(x)
            odd_sum += x

    return {
        "odd": {
            "sum": odd_sum,
            "list": odd_list,
            "len": len(odd_list)
        },
        "even": {
            "sum": even_sum,
            "list": even_list,
            "len": len(even_list)
        }
    }

numbers = [2,100,3,12,313,44,33,22]
print(list_filter(numbers))
