def pal(word):
    normal = list(word)
    sortedlist = normal
    length = len(word) - 1
    backwards = []
    while length >= 0:
        backwards.append(sortedlist[length])
        length -= 1
    if backwards == normal:
        return True
    else:
        return False
def anagram(word1,word2):
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")    
    word1 = list(word1)
    word2 = list(word2)
    word1.sort()
    word2.sort()
    if word1 == word2:
        return True
    else:
        return False