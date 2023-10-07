import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


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

def test_name_setter():
    # Проверяем, что сеттер для имени товара обрезает его до 10 символов
    item = Item('TestItem', 10.0, 5)
    item.name = 'VeryLongItemName'
    assert item.name == 'VeryLongIte'  # Ожидаем обрезание до 10 символов

def test_instantiate_from_csv():
    # Предположим, у вас есть CSV-файл 'test_items.csv' с товарами
    Item.instantiate_from_csv('test_items.csv')
    all_items = Item.get_all_items()
    assert len(all_items) == 3  # Проверяем, что экземпляры были созданы из CSV-файла

def test_string_to_number():
    # Проверяем, что строковые числа корректно преобразуются в числа с плавающей запятой
    assert Item.string_to_number('5') == 5.0
    assert Item.string_to_number('5.0') == 5.0
    assert Item.string_to_number('5.5') == 5.5


def test_addition_with_phone():
    # Тестирование сложения Item и Phone
    phone = Phone("iPhone 14", 120000, 5, 2)
    item = Item("Смартфон", 10000, 20)
    assert phone + item == 25  # Сложение Phone и Item должно возвращать сумму количества товара

def test_instantiate_from_csv_file_not_found():
    # Тест на обработку FileNotFoundError при отсутствии файла
    with pytest.raises(FileNotFoundError) as context:
        Item.instantiate_from_csv('non_existent_file.csv')
    assert str(context.value) == "Отсутствует файл item.csv"

def test_instantiate_from_csv_corrupted_file():
    # Тест на обработку InstantiateCSVError при поврежденном файле
    with open('corrupted_items.csv', 'w') as file:
        # Создаем поврежденный файл, например, удалим одну из колонок
        file.write("name,price\n")
        file.write("Item1,10.0\n")
        file.write("Item2,15.0\n")

    with pytest.raises(InstantiateCSVError) as context:
        Item.instantiate_from_csv('corrupted_items.csv')
    assert str(context.value) == "Файл item.csv поврежден"


if __name__ == '__main__':
    pytest.main()
