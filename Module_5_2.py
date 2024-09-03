class House:
    def __init__(self, Name, Num_of_floors):
        self.name = Name
        self.num_of_floors = Num_of_floors

    def go_to(self, Floor):
        if Floor < 1 or Floor > self.num_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1,Floor+1):
                print(i)

    def __len__(self):
        return self.num_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.num_of_floors}'

new_house = House('ЖК Эльбрус', 30)
new_house1 = House('ЖК Горский', 18)
new_house2 = House('Домик в деревне', 2)
new_house1.go_to(5)
new_house2.go_to(10)

# __str__
print(new_house1)
print(new_house2)

# __len__
print(len(new_house1))
print(len(new_house2))