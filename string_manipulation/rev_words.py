def reverse_word(string: str):
    if string is None:
        return ''
        
    split = string.strip().split(' ')
    return ' '.join(split[::-1])


print(reverse_word("  Life is beautiful "))
print(reverse_word("Life   "))
print(reverse_word(""))
print(reverse_word(None))