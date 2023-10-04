# Импортируем класс Item из файла item.py
from src.item import Item

# Определяем класс Phone, наследующий атрибуты класса Item
class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название смартфона.
        :param price: Цена за одну единицу смартфона.
        :param quantity: Количество смартфонов в магазине.
        :param number_of_sim: Количество поддерживаемых SIM-карт.
        """
        # Вызываем конструктор родительского класса (Item) с помощью super()
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    # Реализуем __repr__ для представления объектов Phone в виде строки
    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    # Реализуем __str__ для получения строкового представления объектов Phone
    def __str__(self):
        return self.name

    # Реализуем __add__ для возможности сложения экземпляров Phone и Item
    def __add__(self, other):
        # Проверяем, является ли другой объект экземпляром Phone или Item
        if isinstance(other, (Phone, Item)):
            # Складываем количество товара двух объектов и возвращаем результат
            return self.quantity + other.quantity
        else:
            raise ValueError("Можно складывать только экземпляры Phone или Item")

    # Геттер и сеттер для атрибута number_of_sim
    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        # Проверяем, что значение является положительным целым числом
        if isinstance(value, int) and value > 0:
            self._number_of_sim = value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
