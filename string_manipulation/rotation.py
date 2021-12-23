def rotate(string, mark):
    return string[mark:] + string[:mark]

def rotation(word1: str, word2: str):
    if word1 is None or word2 is None or len(word1) != len(word2):
        return False

    index = word1.index(word2[0])
    word1 = rotate(word1, index)

    return word1 == word2


print(rotation('ABCD', 'DABC')) # True
print(rotation('ABCD', 'CDAB')) # True
print(rotation('ABCD', 'ADBC')) # False
print(rotation('ABCD', 'ABCD')) # True
print(rotation('ABCD', None)) # False
print(rotation('ABCD', 'ABCDE')) # False