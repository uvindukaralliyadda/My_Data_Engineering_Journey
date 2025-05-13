# Derfine a type called person which has name attribute and talk method

class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f'Hi {self.name}')


John=Person("Uvindu Karalliyadda")
John.talk()

bob=Person("Bob")
bob.talk()
