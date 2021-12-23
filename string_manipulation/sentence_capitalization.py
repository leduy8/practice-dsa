def sentence_capitalization(sentence: str):
    if sentence is None:
        return None
    
    split = sentence.split()
    split = [word.capitalize() for word in split]
    
    return ' '.join(split)


print(sentence_capitalization("life is beautiful"))
print(sentence_capitalization("life   is  truly    beautiful"))
print(sentence_capitalization(""))
print(sentence_capitalization("  "))
print(sentence_capitalization(None))