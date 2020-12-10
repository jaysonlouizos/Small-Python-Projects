import creditcard

def test_identify_card():
    assert creditcard.identify_card('4556737586899855') == True