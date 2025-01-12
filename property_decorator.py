class Celsius:
    def __init__(self, temp):
        self.temp = temp

    def to_fahrenheit(self):
        return self.temp * 9 / 5 + 32

    @property  # декорируем геттер свойством проперти и метод становится свойством temperature
    def temperature(self):
        return self.temp

    @temperature.setter  # декорируем свойством температур с методом геттер
    def temperature(self, value):
        if self.temp < - 273.15:
            raise ValueError
        else:
            self.temp = value


class Notebook:
    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
        for n, v in enumerate(self._notes, 1):
            print(f'{n}.{v}')

