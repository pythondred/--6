#реквест
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} едет'
    def stop(self):
        return f'{self.name} останавливается'
    def turn_right(self):
        return f'{self.name} поворачивает на право'
    def turn_left(self):
        return f'{self.name} поворачивает на лево'
    def show_speed(self):
        return f'Текущая скорость {self.name}  {self.speed} км/час'
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} состовляет {self.speed} км/час')
        if self.speed > 40:
            return f'Скорость {self.name} превышает разрешенную скорость автомобиля в городе'
        else:
            return f'Скорость {self.name} не превышает разрешенную скорость автомобиля в городе'
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} составляет {self.speed} км/час')
        if self.speed > 60:
            return f'{self.name} выше чем предельно допустимая'
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police(self):
        if self.is_police:
            return f'{self.name} это полицейчкая машина'
        else:
            return f'{self.name} это не полицейская машина'
mercedeses = SportCar(100, 'Черный', 'Мерседес', False)
zhiguli = TownCar(30, 'Белая', 'Жигули', False)
lada = WorkCar(70, 'Серая', 'Лада', True)
ford = PoliceCar(110, 'Синяя',  'Ford', True)
print(lada.turn_left())
print(f'Когда {zhiguli.turn_right()}, {mercedeses.stop()}')
print(f'{lada.go()} с высокой скоростью. Скорость {lada.show_speed()}')
print(f'{lada.name} цвета мокрого асфальта ({lada.color})')
print(f'Это {mercedeses.name} полицейская машина? {mercedeses.is_police}')
print(f'Это {lada.name}  полицейская машина? {lada.is_police}')
print(mercedeses.show_speed())
print(zhiguli.show_speed())
print(ford.police())
print(ford.show_speed())
