from plates import is_valid

def test_is_valid_morethan6chars():
    assert is_valid("ab34567") == False
    assert is_valid("abcdefg") == False
    assert is_valid("ABCD123") == False

def test_is_valid_valid():
    assert is_valid("ab3456") == True
    assert is_valid("abcdef") == True
    assert is_valid("ABCD12") == True

def test_is_valid_valid_digits():
    assert is_valid("123456") == False
    assert is_valid("ab45ff") == False
    assert is_valid("AB45cd") == False

def test_is_valid_valid_min_chars():
    assert is_valid("ab") == True
    assert is_valid("ab2") == True