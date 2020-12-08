import palindrome

def test_pal():
    assert palindrome.pal('racecar') == True
    assert palindrome.pal('hockey') == False
    assert palindrome.pal('toot') == True
def test_anagram():
    assert palindrome.anagram('dog', 'god') == True
    assert palindrome.anagram('anagram', 'nag a ram') == True
    assert palindrome.anagram('hotel', 'boat') == False