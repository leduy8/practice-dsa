def most_repeated_char(string):
    if string is None:
        return None

    dup = {}
    max = 0
    res = ''

    for char in string:
        dup[char] = 1 if char not in dup else dup[char] + 1
            
    for val, i in dup.items():
        if max < i:
            max = i
            res = val
    
    return res


print(most_repeated_char("Life is beautiful"))
print(most_repeated_char("hahaha"))
print(most_repeated_char("  "))
print(most_repeated_char(""))
print(most_repeated_char(None))