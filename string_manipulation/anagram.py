def anagram_sort(string1, string2):
    if string1 is None or string2 is None:
        return False
    
    string1 = ''.join(sorted(string1))
    string2 = ''.join(sorted(string2))

    return string1 == string2


def anagram_histogram(string1, string2):
    if string1 is None or string2 is None:
        return False

    ENGLIST_LETTERS = 26
    frequences = [0 for _ in range(ENGLIST_LETTERS)]

    for char in string1:
        frequences[ord(char) - 97] += 1

    for char in string2:
        index = ord(char) - 97
        if frequences[index] == 0:
            return False

        frequences[index] -= 1

    return True


print(anagram_sort("abcd", "bdca"))
print(anagram_sort("abcd", "cadb"))
print(anagram_sort("abcd", "abcd"))
print(anagram_sort("abcd", "bdcb"))
print(anagram_sort(None, None))

print(anagram_histogram("abcd", "bdca"))
print(anagram_histogram("abcd", "cadb"))
print(anagram_histogram("abcd", "abcd"))
print(anagram_histogram("abcd", "bdcb"))
print(anagram_histogram(None, None))