import doctest

# Класс №1
class Assistant:
    def __init__(self, energy: int, current_energy: int):
        # Атрибутам присваиваются значения аргументов конструктора объекта
        # self.energy = energy
        # self.current_energy = current_energy

        """
        Создание и подготовка к работе объекта "Ассистент"
        :param energy: максимальное значение энергии
        :param current_energy: текущая энергия

        Пример:
        >>> assistant = Assistant(100, 0)  # инициализация экземпляра класса
        """

        if not isinstance(energy, (int)):
            raise TypeError("Объем энергии должен быть типа int")
        if energy < 0:
            raise ValueError("Максимальное значение энергии не может быть отрицательным числом")
        self.energy = energy

        if not isinstance(current_energy, (int)):
            raise TypeError("Текущая энергия должно быть типа int")
        if current_energy < 0:
            raise ValueError("Текущая энергия не может быть отрицательным числом")
        self.current_energy = current_energy
        ...

# Метод №1
    def no_more_energy(self, current_energy: int) -> bool:
        """
        Функция которая проверяет иссякла ли энергия

        :param current_energy: текущая энергия

        :return: Иссякла ли энергия

        Примеры:
        # >>> assistant = Assistant(100, 0)  # инициализация экземпляра класса
        # >>> assistant.no_more_energy(0)
        """
        ...

# Метод №2 с doctest и специально допущенной ошибкой
    def assistant_rest(self, energy: int, current_energy: int, energy_plus: int) -> None:
        """
        Восстановление энергии.

        :param energy: Установленный максимум
        :param current_energy: Текущая энергия
        :param energy_plus: Объем добавляемой энергии

        :raise ValueError: Если количество добавляемой энергии превышает максимальное значение, то вызываем ошибку

        Примеры:
        >>> assistant = Assistant(100, 0)  # инициализация экземпляра класса
        >>> assistant.assistant_rest(100,0,25) # выдаёт ошибку, так как ожидалось что assistant восстановит 75 ед. энергии, вместо 25 ед.
        75
        """
        if not isinstance(energy_plus, (int)):
            raise TypeError("Восполняемая энергия должна быть типа int")
        if energy_plus < 0:
            raise ValueError("Восполняемая энергия должна положительным числом")
        
        if current_energy+energy_plus > energy:
            raise ValueError("Добавляемая энергия не должна превышать максимальное значение")
        return current_energy+energy_plus
        ...

# Метод №3 с реализованным doctest
    def conduct_research(self, current_energy: int, energy_minus: int) -> None:
        """
        Извлечение энергии для проведения исследовательской работы.

        :param current_energy: текущая энергия
        :param energy_minus: Объем затраченой энергии
        :raise ValueError: Если количество извлекаемого превышает количество энергии,
        то возвращается ошибка.

        :return: Объем затраченой энергии

        Примеры:
        >>> assistant = Assistant(100, 25)  # инициализация экземпляра класса 
        >>> assistant.conduct_research(25, 20)  # не выдаст ошибку, как как всё выполненно так, как мы и ожидали
        5
        """
        if not isinstance(energy_minus, (int)):
            raise TypeError("Объем затраченой энергии должен быть типа int")
        if energy_minus < 0:
            raise ValueError("Объем затраченой энергии должен быть положительным числом")
        
        if current_energy-energy_minus < 0:
            raise ValueError("Количество пассажиров, вышедших из машины не может превышать их изначальное количество")
        return current_energy-energy_minus
        ...


# Класс №2
class Car:
    def __init__(self, seats: int, occupied_seats: int):
        # Атрибутам присваиваются значения аргументов конструктора объекта
        # self.seats = seats
        # self.occupied_seats = occupied_seats

        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param seats: Количество мест
        :param occupied_seats: Количество занятых мест

        Примеры:
        >>> car = Car(5, 0)  # инициализация экземпляра класса
        """       
        
        if not isinstance(seats, (int)):
            raise TypeError("Количество мест должно быть типа int")
        if seats <= 0:
            raise ValueError("Количество мест должно быть положительным числом")
        self.seats = seats

        if not isinstance(occupied_seats, (int)):
            raise TypeError("Количество занятых мест должна быть int")
        if occupied_seats < 0:
            raise ValueError("Количество занятых мест не может быть отрицательным числом")
        self.occupied_seats = occupied_seats

# Метод №1
    def is_empty_car(self) -> bool:
        """
        Функция которая проверяет является ли машина пустой

        :return: Является ли машина пустой

        Примеры:
        >>> car = Car(5, 3)  # инициализация экземпляра класса
        >>> car.is_empty_car()
        """
        ...

# Метод №2 с реализованным doctest
    def add_passenger(self, seats: int, occupied_seats: int, passenger: int) -> None:
        """
        Добавление пассажиров в машину.
        :param passenger: Количество добавляемых пассажиров

        :raise ValueError: Если количество добавляемых пассажиров (включая водителя) превышает свободное место в машине, то вызываем ошибку

        Примеры:
        >>> car = Car(5, 3)  # инициализация экземпляра класса
        >>> car.add_passenger(5, 3, 2)  # не выдаст ошибку, как как всё выполненно так, как мы и ожидали
        5
        """
        if not isinstance(passenger, (int)):
            raise TypeError("Количество добавляемых пассажиров должно быть типа int")
        if passenger < 0:
            raise ValueError("Количество добавляемых пассажиров должно быть положительным числом")
        
        if occupied_seats+passenger > seats:
            raise ValueError("Количество добавляемых пассажиров не должно превышать максимальное значение")
        return occupied_seats+passenger
        ...

# Метод №3 с реализованным doctest
    def remove_passenger(self, occupied_seats: int, extracted_passenger: int) -> None:
        """
        Высадка пассажиров из автомобиля.

        :param occupied_seats: Количество занятых мест
        :param extracted_passenger: Количество пассажиров, вышедших из машины
        :raise ValueError: Если количество пассажиров, вышедших из автомобиля, превышает их количество,
        то возвращается ошибка.

        :return: Количество пассажиров, вышедших из машины

        Примеры:
        >>> car = Car(5, 3)  # инициализация экземпляра класса
        >>> car.remove_passenger(3, 3)  # не выдаст ошибку, как как всё выполненно так, как мы и ожидали
        0
        """
        if not isinstance(extracted_passenger, (int)):
            raise TypeError("Количество пассажиров, вышедших из машины должно быть типа int")
        if extracted_passenger < 0:
            raise ValueError("Количество пассажиров, вышедших из машины должно быть положительным числом")
        
        if occupied_seats-extracted_passenger < 0:
            raise ValueError("Количество пассажиров, вышедших из машины не может превышать их изначальное количество")
        return occupied_seats-extracted_passenger
        ...


# Класс №3
class Research_sample:
    def __init__(self, water_max: float, current_water: float):
        # Атрибутам присваиваются значения аргументов конструктора объекта
        # self.water_max = water_max
        # self.current_water = current_water
        """
        Создание и подготовка к работе объекта "Исследовательский образец"

        :param water_max: Объем максимально поглощаемой жидкости
        :param current_water: Объем налитой жидкости

        Примеры:
        >>> research_sample = Research_sample(100, 10)  # инициализация экземпляра класса
        """
        if not isinstance(water_max, (int, float)):
            raise TypeError("Объем максимально поглощаемой жидкости должен быть типа int или float")
        if water_max <= 0:
            raise ValueError("Объем максимально поглощаемой жидкости должен быть положительным числом")
        self.water_max = water_max

        if not isinstance(current_water, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if current_water < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.current_water = current_water
        ...

# Метод №1
    def insufficient_water(self, current_water: float) -> bool:
        """
        Функция которая проверяет недостаточно ли воды для исследуемого образца

        :param current_water: Объем налитой жидкости

        :return: Недостаточно ли воды

        Примеры:
        >>> research_sample = Research_sample(100, 10)
        >>> research_sample.insufficient_water(10)
        """
        ...

# Метод №2
    def add_water_to_sample(self, water_max: float, current_water: float, water: float) -> None:
        """
        Полив испытуемого образца.

        :param water_max: Объем максимально поглощаемой жидкости
        :param current_water: Объем налитой жидкости
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает максимально поглощаемую жидкость, то вызываем ошибку

        Примеры:
        >>> research_sample = Research_sample(100, 10)
        >>> research_sample.add_water_to_sample(100, 10, 50)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        # Реализацию методов не нужно, достаточно только заглушки в виде троеточия
        ...

# Метод №3
    def sample_absorbed_water(self, current_water: float, estimate_water: float) -> None:
        """
        Образец впитал воду.

        :param estimate_water: Объем поглощаемой жидкости
        :raise ValueError: Если количество поглощаемой жидкости превышает количество воды,
        то возвращается ошибка.

        :return: Объем поглощённой жидкости

        Примеры:
        >>> research_sample = Research_sample(100, 10)
        >>> research_sample.sample_absorbed_water(10, 5)
        """
        # Реализацию методов не нужно, достаточно только заглушки в виде троеточия
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации