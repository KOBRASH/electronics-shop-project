import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all_items = []  # Изменим имя атрибута для ясности

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name  # Приватный атрибут name
        self.price = price
        self.quantity = quantity
        Item.all_items.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
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

    @classmethod
    def set_discount_rate(cls, rate: float) -> None:
        """
        Устанавливает уровень скидки для всех товаров этого класса.

        :param rate: Уровень скидки в виде десятичной дроби (например, 0.85 для 15% скидки).
        """
        cls.pay_rate = rate

    @classmethod
    def get_all_items(cls) -> list:
        """
        Возвращает список всех созданных экземпляров класса.

        :return: Список всех товаров.
        """
        return cls.all_items

    @classmethod
    def instantiate_from_csv(cls, file_path: str) -> None:
        """
        Создает экземпляры класса Item из данных CSV-файла.

        :param file_path: Путь к CSV-файлу с данными.
        """
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
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