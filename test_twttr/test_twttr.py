import pytest
from twttr import shorten

def test_no_vowels():
    assert shorten("bcdf") == "bcdf"

def test_all_vowels():
    assert shorten("aeiou") == ""

def test_mixed_case():
    assert shorten("aEIoU") == ""

def test_mixed_characters():
    assert shorten("Hello World") == "Hll Wrld"

def test_long_string():
    # Checking if the expected output is correct
    assert shorten("This is a long string with vowels") == "Ths s  lng strng wth vwls"

def test_empty_string():
    assert shorten("") == ""

def test_numbers_and_symbols():
    assert shorten("Th3 qu!ck br0wn f0x") == "Th3 q!ck br0wn f0x"

if __name__ == "__main__":
    pytest.main()
