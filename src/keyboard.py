from src.item import Item

# Создаем класс-миксин для изменения языка клавиатуры
class LanguageMixin:
    def __init__(self):
        self._language = "EN"  # Устанавливаем язык по умолчанию

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"

    @property
    def language(self):
        return self._language

# Создаем класс Keyboard с использованием множественного наследования
class Keyboard(Item, LanguageMixin):  # Наследуемся и от Item, и от LanguageMixin
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name

# Создаем класс Item
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# Теперь напишем тесты для класса Keyboard
if __name__ == '__main__':
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"

    # Попытка изменить язык напрямую должна вызвать ошибку AttributeError
    try:
        kb.language = 'CH'
    except AttributeError:
        print("AttributeError: property 'language' of 'Keyboard' object has no setter")
    else:
        raise AssertionError("Ошибка: AttributeError не было вызвано.")
