# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Work:
    def __init__(self, hours: int, worker: str):
        """
        Создание и подготовка к работе объекта "Работа"

        :param hours: Количество рабочих часов
        :param worker: Имя рабочего

        Примеры:
        >>> work = Work(8, 'Вася')  # инициализация экземпляра класса
        """

        if not isinstance(worker, int):
            raise TypeError('Имя рабочего не может состоять из чисел')
        if worker == '':
            raise ValueError('Имя рабочего не может быть пустым')
        self.worker = worker

        if not isinstance(hours, int):
            raise TypeError('Часы должны быть типа int')
        if hours < 0:
            raise ValueError('Часы не могут быть меньше 0')

        self.hours = hours

    def hours_check(self) -> bool:
        """
        Функция проверяет количество часов для отработки данной работы

        :return Является ли количество часов достаточным для работы

        Примеры:
        >>> work = Work(1, 'Вася')
        >>> work.hours_check()
        """

        ...

    def add_hours(self, hours: int) -> None:
        """
        Добавление часов в работу.
        :param hours: Количество часов, добавленных для работы

        :raise ValueError: Если количество часов для переработки превысет 4
        Примеры:
        >>> work = Work(8, 'Коля')
        >>> work.add_hours(2)
        """
        if not isinstance(hours, int):
            raise TypeError('Часы должны быть в формате целого числа')
        if hours < 0:
            raise ValueError('Часы не могут быть отрицательным числом')
        ...

class Shop:
    def __init__(self, capacity_products: int, discount: int):
        """
        Создание и подготовка к работе объекта "Магазин"

        :param capacity_products: Количество продуктов в магазине
        :param discount: Скидка на продукты

        Примеры:
        >>> shop = Shop(150, 15)  # инициализация экземпляра класса
        """

        if not isinstance(capacity_products, int):
            raise TypeError('Количество продуктов может быть только целочисленным')
        if capacity_products < 0:
            raise ValueError('Количество продуктов не может быть меньше 0')
        self.capacity_products = capacity_products

        if not isinstance(discount, int):
            raise TypeError('Скидка должна быть типа int')
        if discount < 0:
            raise ValueError('Cкидка не может быть меньше 0')

        self.discount = discount

    def discount_check(self) -> bool:
        """
        Функция проверяет, достаточная ли скидка в магазине

        :return: Является ли процент скидки достаточным
        :raise ValueError: Если скидка больше 100 процентов

        Примеры:
        >>> shop = Shop(150, 15)
        >>> shop.discount_check()
        """

        ...

    def products_add(self, product: int) -> None:
        """
        Добавление продуктов в магазин.
        :param product:
        :raise ValueError: Если количество продуктов будет меньше 20
        Примеры:
        >>> shop = Shop(150, 15)
        >>> shop.products_add(30)
        """
        if not isinstance(product, int):
            raise TypeError('Количество продуктов должно быть в формате целого числа')
        if product < 0:
            raise ValueError('Количество продуктов не может быть отрицательным числом')
        ...

class Park:
    def __init__(self, amount_trees: int, animals: int):
        """
        Создание и подготовка к работе объекта "Парк"

        :param amount_trees: Количество деревьев в парке
        :param animals: Количество животных в парке

        Примеры:
        >>> park = Park(300, 20)  # инициализация экземпляра класса
        """

        if not isinstance(amount_trees, int):
            raise TypeError('Количество деревьев может быть только целочисленным')
        if amount_trees < 0:
            raise ValueError('Количество деревьев не может быть меньше 0')
        self.amount_trees = amount_trees

        if not isinstance(animals, int):
            raise TypeError('Количество животных может быть только целочисленным')
        if animals < 0:
            raise ValueError('Количество животных не может быть меньше 0')

        self.animals = animals

    def trees_check(self, area: (float, int)) -> bool:
        """
        Функция проверяет, достаточно ли деревьев высажено в парке

        :return: Является ли количетсво деревьев достаточным
        :param area: Площадь парка
        :raise ValueError: Если процент растительности меньше 30

        Примеры:
        >>> park = Park(300, 20)
        >>> park.trees_check(1500)
        """
        if not isinstance(area, (float, int)):
            raise TypeError('Площадь парка не может быть в буквенном виде')
        if area < 0:
            raise ValueError('Площадь парка не может быть меньше 0')
        ...

    def add_trees(self, trees: int) -> None:
        """
        Посадка деревьев в парке.
        :param trees: Количество дополнительных деревьев для парка
        :raise ValueError: Если количество дереьвев будет меньше 5
        Примеры:
        >>> park = Park(300, 20)
        >>> park.add_trees(30)
        """
        if not isinstance(trees, int):
            raise TypeError('Количество деревьев должно быть в формате целого числа')
        if trees < 0:
            raise ValueError('Количество деревьев не может быть отрицательным числом')
        ...





if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
