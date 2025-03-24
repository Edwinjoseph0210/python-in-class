class Car:
    def __init__(self, make):
        self.__make = make  # Private attribute

    def get_make(self):  # Accessor method
        return self.__make

    def set_make(self, new_make):  # Mutator method
        self.__make = new_make

myCar = Car('Ford')
print(myCar.get_make())

myCar.set_make('Porsche')
print(myCar.get_make())
