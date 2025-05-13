import random

for i in range(3):
    #random value
    print(random.randint(10,20))

members=['Uvindu','Chamuditha','Janadhi']
leader=random.choice(members)
print(leader)

class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second


roll1=Dice()
print(roll1.roll())