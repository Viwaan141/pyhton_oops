#Public -> attribute
#Protected -> _attribute
#private -> __attribute

class Car:
    wheels = 4
    _color = "Black"
    __year = 2017 

class Bmw(Car):
    def __init__(self):
        print("protected attribute color",self._color)

car = Car()
print("Public attribute wheels:",car.wheels)
bmw = Bmw()
print("Private attribute year:",car._Car__year)