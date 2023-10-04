from src.phone import Phone
from src.item import Item

def test_phone_creation():
    # Тестирование создания объекта Phone
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert str(phone) == 'iPhone 14'
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone.number_of_sim == 2

def test_addition():
    # Тестирование сложения экземпляров Phone и Item
    phone = Phone("iPhone 14", 120000, 5, 2)
    item = Item("Смартфон", 10000, 20)
    assert item + phone == 25  # Сложение Item и Phone должно возвращать сумму количества товара
    assert phone + phone == 10  # Сложение двух Phone должно возвращать сумму количества товара

def test_invalid_addition():
    # Тестирование недопустимого сложения Phone с объектами, не являющимися Phone или Item
    phone = Phone("iPhone 14", 120000, 5, 2)
    non_phone_item = "Не Phone или Item"
    try:
        result = phone + non_phone_item  # Попытка сложения Phone и объекта, не являющегося Phone или Item, должна вызывать ошибку
    except ValueError as e:
        assert str(e) == "Можно складывать только экземпляры Phone или Item"
