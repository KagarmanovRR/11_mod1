class Car:
    # VIN-номер, марка, модель, год выпуска, мощность, пробег, кол-во владельцев, стоимость
    def __init__(self, VIN, old,  mark, model, year, power, km, amount, cost):
        self.VIN = VIN
        self.old = old
        self.mark = mark
        self.model = model
        self.year = int(year)
        self.power = int(power)
        self.km = int(km)
        self.amount = int(amount)
        self.cost = cost

    # вывод информации о текущем автомобиле
    def __str__(self):
        return f"{'VIN' if self.old=='б/у' else 'Госномер'}: {self.VIN}, марка: {self.mark}" \
               f" модель: {self.model}, год выпуска: {self.year}, мощность: {self.power}, лс, " \
               f" пробег: {self.km}, количество владельцев: {self.amount}, стоимость: {self.cost} млн. руб."
    # сумма налога
    def get_tax(self):
        if self.power < 100:
            tax=10
            sum_tax=self.power*tax
            return sum_tax
        elif self.power < 150:
            tax = 34
            sum_tax = self.power * tax
            return sum_tax
        else:
            tax = 49
            sum_tax = self.power * tax
            return sum_tax

    # увеличение пробега
    def set_mileage(self, kmr):
        self.km += kmr


avto_1 = Car("О811КК750", "б/у", 'Renaught', 'Duster', 2015, 110, 27889, 3, 1.2)
print(avto_1)
print("Налог на мощность:", avto_1.get_tax())
avto_2 = Car("1KLBN52TWXM186109", "новая", 'Renaught', 'Duster', 2021, 130, 7889, 2, 1.7)
print(avto_2)
print("Налог на мощность:", avto_2.get_tax())
avto_3 = Car("1KLBN52TWXM186109", "новая", 'Renaught', 'Duster', 2022, 180, 7889, 2, 3.7)
print(avto_3)
print("Налог на мощность:", avto_3.get_tax())
avto_3.set_mileage(1000)
print(avto_3)