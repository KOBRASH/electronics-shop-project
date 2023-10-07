import pytest
from src.keyboard import Keyboard


# Тест на инициализацию клавиатуры
def test_keyboard_initialization():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"


# Тест на проверку языка по умолчанию
def test_keyboard_default_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"


# Тест на изменение языка клавиатуры
def test_keyboard_change_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"

