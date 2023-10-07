import csv

# Класс-исключение для обработки ошибок при создании экземпляров из CSV
class InstantiateCSVError(Exception):
    pass

class Item:
    pay_rate = 1.0
    all_items = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all_items.append(self)


    def name(self):
        return self._name


    def name(self, value):
        if len(value) <= 10:
            self._name = value
        else:
            self._name = value[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


    def set_discount_rate(cls, rate: float) -> None:
        """
        Устанавливает уровень скидки для всех товаров этого класса.

        :param rate: Уровень скидки в виде десятичной дроби (например, 0.85 для 15% скидки).
        """
        cls.pay_rate = rate


    def get_all_items(cls) -> list:
        """
        Возвращает список всех созданных экземпляров класса.

        :return: Список всех товаров.
        """
        return cls.all_items


    def instantiate_from_csv(cls, file_path: str = 'items.csv') -> None:
        """
        Создает экземпляры класса Item из данных CSV-файла.

        :param file_path: Путь к CSV-файлу с данными.
        """
        try:
            with open(file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row.get('name')
                    price = row.get('price')
                    quantity = row.get('quantity')

                    if not (name and price and quantity):
                        raise InstantiateCSVError("Файл item.csv поврежден")

                    price = cls.string_to_number(price)
                    quantity = int(quantity)
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")


    def string_to_number(value: str) -> float:
        """
        Преобразует строку в число.

        :param value: Строка, представляющая число.
        :return: Преобразованное число.
        """
        return float(value)

    def __repr__(self):
        """
        Магический метод __repr__ для представления объекта в виде строки.
        """
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Магический метод __str__ для представления объекта в виде строки.
        """
        return self.name
