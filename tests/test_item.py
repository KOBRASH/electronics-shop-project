import pytest
from src.item import Item

# Фикстура для создания экземпляров класса Item для тестирования
@pytest.fixture
def create_items():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    yield item1, item2
    Item.all_items = []  # Очищаем список всех товаров после завершения тестов

def test_calculate_total_price(create_items):
    item1, item2 = create_items

    # Проверяем, правильно ли вычисляется общая стоимость товаров
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount(create_items):
    item1, _ = create_items

    # Проверяем, что скидка применяется корректно
    assert item1.price == 10000.0
    Item.set_discount_rate(0.8)  # Устанавливаем скидку на все товары
    item1.apply_discount()
    assert item1.price == 8000.0

def test_set_discount_rate(create_items):
    _, item2 = create_items

    # Проверяем, что уровень скидки корректно устанавливается для всех товаров
    assert Item.pay_rate == 1.0
    Item.set_discount_rate(0.9)
    assert Item.pay_rate == 0.9
    item2.apply_discount()
    assert item2.price == 18000.0

def test_get_all_items(create_items):
    item1, item2 = create_items

    # Проверяем, что метод get_all_items возвращает список всех товаров
    all_items = Item.get_all_items()
    assert len(all_items) == 2
    assert item1 in all_items
    assert item2 in all_items
