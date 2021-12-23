def remove_duplicate(string):
    if string is None:
        return ''

    output = ''
    seen = set()
    for char in string:
        if char not in seen:
            seen.add(char)
            output += char

    return output
            


print(remove_duplicate("Life is beautiful"))
print(remove_duplicate("  "))
print(remove_duplicate(""))
print(remove_duplicate(None))