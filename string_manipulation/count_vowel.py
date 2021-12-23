def count_vowel(string):
    if string is None or len(string) == 0:
        return 0

    vowels = ['a', 'u', 'i', 'e', 'o']
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    
    return count


print(count_vowel("hellO")) # 2
print(count_vowel(""))
print(count_vowel(None))