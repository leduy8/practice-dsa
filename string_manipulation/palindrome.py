def is_palindrome(string):
    if string is None:
        return None

    mid = len(string) // 2
    
    if len(string) % 2 == 0:
        return string[:mid] == string[mid:][::-1]

    return string[:mid] == string[mid + 1:][::-1]


print(is_palindrome('abba'))
print(is_palindrome('abcba'))
print(is_palindrome('abca'))