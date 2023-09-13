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
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all_items.append(self)

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
