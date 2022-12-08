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

    # Перехват функции print, когда она преобразует свое значение в строкун
    def __str__(self):
        return f"{'VIN' if self.old=='б/у' else 'Госномер'}: {self.VIN}, марка: {self.mark}" \
               f" модель: {self.model}, год выпуска: {self.year}, мощность: {self.power}, лс, " \
               f" пробег: {self.km}, количество владельцев: {self.amount}, стоимость: {self.cost} млн. руб."

avto_1 = Car("О811КК750", "б/у", 'Renaught', 'Duster', 2015, 110, 27889, 3, 1.2)
print(avto_1)
avto_2 = Car("1KLBN52TWXM186109", "новая", 'Renaught', 'Duster', 2021, 130, 7889, 2, 1.7)
print(avto_2)