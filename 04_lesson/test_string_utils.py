import pytest
from string_utils import StringUtils


# Функция capitalize
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("test", "Test"),
        ("test test", "Test test"),
        ("Test", "Test"),
        ("тест", "Тест"),
    ]
)
def test_capitalize_positive(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize(
    "input_str", "expected",
    [
        ('  ', '  '),
        ('', ''),
    ]
)
def test_capitalize_negative(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_str) == expected


# Функция trim
@pytest.mark.parametrize(
    "input_str, expected",
    [
        (" test", "test"),
        ("   test", "test"),
    ]
)
def test_trim_positive(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("test", "test"),
        ('  ', ''),
        ('', ''),
    ]
)
def test_trim_negative(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.trim(input_str) == expected


# Функция contains
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("test", "s", True),
        ("test train", "a", True),
        ("test", "a", False)
    ]
)
def test_contains_positive(input_str, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.contains(input_str, symbol) == expected


# Используются разные раскладки для input_str и symbol
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("Test", "Т", False),
    ]
)
def test_contains_negative(input_str, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.contains(input_str, symbol) == expected


# Функция delete_symbol
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("Test", "T", "est"),
        ("Test", "s", "Tet"),
        ("Test test", " ", "Testtest"),
        ("Test", "t", "Tes"),
    ]
)
def test_delete_symbol_positive(input_str, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("Test", "a", "Test"),
    ]
)
def test_delete_symbol_negative(input_str, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(input_str, symbol) == expected
