import string

def compute_gradelevel(textdoc):
    grade_level= {
        
        1:'Kindergarten',
        2:'First Grade',
        3:'Second Grade',
        4:'Third Grade',
        5:'Fourth Grade',
        6:'Fifth Grade',
        7:'Sixth Grade',
        8:'Seventh Grade',
        9:'Eigth Grade',
        10:'Ninth Grade',
        11:'Tenth Grade',
        12:'Eleventh Grade',
        13:'Twelfth Grade',
        14: 'College',
    
        }
    textdoc = open(textdoc)
    textdoc = textdoc.read()
    words = get_words(textdoc)
    sentences = get_sentences(textdoc)
    char = get_characters(textdoc)
    reading_level = round(4.7*(char/words)+.5*(words/sentences)-21.43)

    reading_level = grade_level[reading_level]

    return reading_level
    
def get_words(textdoc:str) -> int:
    
    translator = str.maketrans('', '', string.punctuation)
    textdoc = textdoc.translate(translator)
    word_count = len(textdoc.split())
    return word_count

def get_characters(textdoc:str):

    translator = str.maketrans('', '', string.punctuation)
    textdoc = textdoc.translate(translator)
    char_list = list(textdoc)
    return len(char_list)



def get_sentences(textdoc:str):

    textdoc = textdoc.lower()
    translator = str.maketrans('', '', string.ascii_lowercase)
    textdoc = textdoc.translate(translator)
    
    sentence_count = textdoc.split()
    check = ['!','?','.']
    for char in sentence_count:
        if char not in check:
            sentence_count.pop(0)

    return len(sentence_count)
    
print(compute_gradelevel('alice.txt'))