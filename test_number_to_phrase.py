import pytest
import number_to_phrase

def test_unit_to_phrase():
    assert number_to_phrase.unit_to_phrase(1) == 'one'
    assert number_to_phrase.unit_to_phrase(10) == 'ten'
    assert number_to_phrase.unit_to_phrase(25) == 'twentyfive'
    assert number_to_phrase.unit_to_phrase(150) == 'onehundredfifty'
    assert number_to_phrase.unit_to_phrase(115) == 'onehundredfifteen'