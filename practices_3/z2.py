class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name, "сидит")

    def roll_over(self):
        print(self.name, "перекатывается")


my_dog = Dog(name='willie', age='6 лет')
print(my_dog.age,my_dog.name)
my_dog.sit()
my_dog.roll_over()

my_dog2=Dog(name='lucy', age='3')
my_dog2.sit()
my_dog2.roll_over()

