import json

class Animal():
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, color:str):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print("Чирик")

    def eat(self):
        print("Я ем зерна")

class Mammal(Animal):
    def __init__(self, name, age, size:str):
        super().__init__(name, age)
        self.size = size

    def make_sound(self):
        print("Гррр")

    def eat(self):
        print("Я ем траву")

class Reptile(Animal):
    def __init__(self, name, age, legs:bool):
        super().__init__(name, age)
        self.legs = legs

    def make_sound(self):
        print("Шшшшш")

    def eat(self):
        print("Я ем насекомых")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Worker():
    def __init__(self, name:str, experience:int):
        self.name = name
        self.age = experience

class ZooKeeper(Worker):
    def __init__(self, name, experience):
        super().__init__(name, experience)

    def feed_animal(self):
        print("Я покормил животных")

class Veterinarian(Worker):
    def __init__(self, name, experience):
        super().__init__(name, experience)

    def heal_animal(self):
        print("Я вылечил животного")


class Zoo():
    def __init__(self, name:str, adress:str):
        self.name = name
        self.adress = adress
        self.animals = []
        self.workers = []


    def add_animal(self, name, age):
        self.animals.append(Animal(name, age))

    def add_worker(self, name, experience):
        self.workers.append(Worker(name, experience))

    def print_info(self):
        if len(self.animals) > 0:
            print("Животные:")
            for animal in self.animals:
                print(f'{animal.name}, {animal.age}')

        if len(self.workers) > 0:
            print("Сотрудники:")
            for worker in self.workers:
                print(f'{worker.name}, {worker.age}')

    def set_data(self):
        zoo_list = self.__dict__

        json = {}

        for (key, value) in zoo_list.items():
            if isinstance(value, list):
                item_list = []
                for item in value:
                    item_list.append(item.__dict__)
                json[key] = item_list
            else:
                json[key] = value

        file = open('file.txt', 'w', encoding='utf-8')
        file.write(f'{json}')

def get_data():
    file = open('file.txt', 'r', encoding='utf-8')
    data = eval(file.readline())

    zoo = Zoo(data['name'], data['adress'])

    if data['animals']:
        for animal in data['animals']:
            # print(animal['name'])
            zoo.add_animal(animal['name'], animal['age'])

    if data['workers']:
        for worker in data['workers']:
            # print(animal['name'])
            zoo.add_worker(worker['name'], worker['age'])

    return zoo


bird = Bird("Воробей", 1, "Серый")
mammal = Mammal("Корова", 5, "Большая")
reptile = Reptile("Кобра", 2, False)




animals_list = [
    bird,
    mammal,
    reptile
]

# zoo = Zoo('ZeroZoo', 'пр. Науки, 1')
# zoo.add_animal('Слон', 48)
# zoo.add_animal('Жираф', 27)
# zoo.add_worker('Витек', 69)

# zoo_keeper = ZooKeeper('Витек', 3)
# veterinarian = Veterinarian('Cанек', 3)

# animal_sound(animals_list)
# zoo.print_info()
# zoo_keeper.feed_animal()
# veterinarian.heal_animal()


# zoo.set_data()
zoo = get_data()

print(zoo.__dict__)