import string


def check_words(textdoc:str) -> dict:

    textdoc = open(textdoc)
    textdoc = textdoc.read()
    translator = str.maketrans('', '', string.punctuation)
    textdoc = textdoc.translate(translator)
    textdoc = textdoc.lower()
    textdoc = textdoc.split()
    word_dict = {}

    for i in range(len(textdoc)):
        if textdoc[i] in word_dict:
            word_dict[textdoc[i]] = word_dict[textdoc[i]] + 1
        elif textdoc[i] not in word_dict:
            word_dict.update({textdoc[i]:1})
    return word_dict

def check_pairs(textdoc:str) -> dict:
    word = input('what word do you want to check:')
    word = word.lower()
    textdoc = open(textdoc)
    textdoc = textdoc.read()
    translator = str.maketrans('', '', string.punctuation + '"')
    textdoc = textdoc.translate(translator)
    textdoc = textdoc.lower()
    textdoc = textdoc.split()
    word_dict = {}

    for i in range(len(textdoc)):
        if i == len(textdoc) - 1:
            break
        check = (textdoc[i],textdoc[i+1])
        if check[0] == word:
            if check in word_dict:
                word_dict[check] = word_dict[check] + 1
            elif check not in word_dict:
                word_dict.update({check:1})
    return word_dict



def most_used_word(textdoc:str):

    word_dict = check_words(textdoc)
    STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    for char in STOPWORDS:
        if char in word_dict:
            word_dict.pop(char)
    words = list(word_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])

def most_used_phrase(textdoc:str):
    word_dict = check_pairs(textdoc)
    words = list(word_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])
    


def check_len(textdoc:str) -> int:
    return len(check_words(textdoc))
