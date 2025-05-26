class Animal:
    species1 = "Dog"

    def __init__(self, name, age):
        self.name = name
        self.age = age

Animal1 = Animal("Tommy",3)
print(f"{Animal1.species1} name is :{Animal1.name}")
