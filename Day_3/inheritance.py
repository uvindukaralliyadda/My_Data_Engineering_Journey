class Mammal:
    def __init__(self,name):
        self.name=name

    def walk(self):
        print(f'{self.name} walk')


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass

dog1=Dog('Bingo')
dog1.walk()

cat1=Cat('Kitty')
cat1.walk()