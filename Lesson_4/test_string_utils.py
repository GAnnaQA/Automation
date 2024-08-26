import pytest
from string_utils import StringUtils

@pytest.mark.parametrize('input_string, expected_result', 
                         [("дом", "Дом"), 
                          ("Skypro", "Skypro"), 
                          ("hello, world", "Hello, world"), 
                          ("123", "123")
                          ])
def test_capitilize(input_string, expected_result):
    util = StringUtils()
    res = util.capitilize(input_string)
    assert res == expected_result

def test_capitilize_error():
    util = StringUtils()
    with pytest.raises(AttributeError):
        res = util.capitilize(125)

@pytest.mark.parametrize('input_string, expected_result', 
                         [
                            (" SkyPro", "SkyPro"), 
                            ("  Probel", "Probel"), 
                            ("    ", ""), 
                            ("  Probely   ", "Probely   "), 
                            ("NetProbelov", "NetProbelov"), 
                            ("Probel v centre", "Probel v centre")
                          ])
def test_trim(input_string, expected_result):
    util = StringUtils()
    res = util.trim(input_string)
    assert res == expected_result

@pytest.mark.parametrize('input_string, delimeter, list', 
                         [
                            ("a,b,c,d", ",", ["a", "b", "c", "d"]),
                            ("1:2:3:4", ":", ["1", "2", "3", "4"]),
                            ("", "", []),
                            (" ", "", []),
                            ("Hello, World.Goodbye, World", ".", ["Hello, World", "Goodbye, World"])
                         ])
def test_to_list(input_string, delimeter, list):
    util = StringUtils()
    res = util.to_list(input_string, delimeter)
    assert res == list

@pytest.mark.parametrize('input_string',
                        [
                            (123),
                            (None)
                        ])
def test_to_list_error(input_string):
    util = StringUtils()
    with pytest.raises(AttributeError):
        util.to_list(input_string)

@pytest.mark.parametrize('input_string, symbol, bool', 
                        [
                            ("Hello, World", "l", True),
                            ("Hi all", "w", False),
                            ("123", "3", True),
                            ("", "", False),
                            ("   ", "", False),
                            ("    ", " ", True)
                        ])
def test_contains(input_string, symbol, bool):
    util = StringUtils()
    res = util.contains(input_string, symbol)
    assert res == bool

def test_contains_error():
    util = StringUtils()
    with pytest.raises(AttributeError):
        util.contains(123, 2)

@pytest.mark.parametrize('input_string, symbol, result',
                        [
                           ("Hello, World!", "!", "Hello, World"),
                           ("12534", "5", "1234"),
                           (" He llo ", " ", "Hello"), 
                           ("Hi all", "o", "Hi all")  
                        ])
def test_delete_symbol(input_string, symbol, result):
    util = StringUtils()
    res = util.delete_symbol(input_string, symbol)
    assert res == result

@pytest.mark.parametrize('input_string, symbol',
                        [
                            (123, 2),
                            (None, "1")
                        ])
def test_delete_symbol_error(input_string, symbol):
    util = StringUtils()
    with pytest.raises(AttributeError):
        util.delete_symbol(input_string, symbol)

@pytest.mark.parametrize('input_string, symbol, bool',
                        [
                           ("!Hello, World!", "!", True),
                           ("51234", "5", True),
                           (" Hello ", " ", True), 
                           ("Hi all", "o", False),
                           (" ", " ", True)  
                        ])
def test_starts_with(input_string, symbol, bool):
    util = StringUtils()
    res = util.starts_with(input_string, symbol)
    assert res == bool

@pytest.mark.parametrize('input_string, symbol',
                        [
                            (123, 1),
                            (None, "")
                        ])
def test_starts_with_error(input_string, symbol):
    util = StringUtils()
    with pytest.raises(AttributeError):
        util.starts_with(input_string, symbol)

@pytest.mark.parametrize('input_string, symbol, bool',
                        [
                           ("!Hello, World!", "!", True),
                           ("12345", "5", True),
                           (" Hello ", " ", True), 
                           ("Hi all", "o", False),
                           (" ", " ", True)  
                        ])
def test_end_with(input_string, symbol, bool):
    util = StringUtils()
    res = util.end_with(input_string, symbol)
    assert res == bool

@pytest.mark.parametrize('input_string, symbol',
                        [
                            (123, 3),
                            (None, "")
                        ])
def test_end_with_error(input_string, symbol):
    util = StringUtils()
    with pytest.raises(AttributeError):
        util.end_with(input_string, symbol)

@pytest.mark.parametrize('input_string, bool',
                        [
                           ("", True),
                           ("   ", True),
                           (" Hello ", False), 
                           (",", False) 
                        ])
def test_is_empty(input_string, bool):
    util = StringUtils()
    res = util.is_empty(input_string)
    assert res == bool

@pytest.mark.parametrize('input_string',
                        [
                            (123),
                            (None)
                        ])
def test_is_empty_error(input_string):
    util = StringUtils()
    with pytest.raises(AttributeError):
        util.is_empty(input_string)

@pytest.mark.parametrize('input_list, joiner, result',
                        [
                           (["Hello", "World"], "_", "Hello_World"),
                           ([], ".", ""),
                           (["Hello", " ", "World"], ":", "Hello: :World"), 
                        ])
def test_list_to_string(input_list, joiner, result):
    util = StringUtils()
    res = util.list_to_string(input_list, joiner)
    assert res == result

def test_list_to_string_whitout_joiner():
    util = StringUtils()
    res = util.list_to_string([1,2,3])
    assert res == "1, 2, 3"