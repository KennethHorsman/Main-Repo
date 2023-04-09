# Vehicle.py

class Vehicle: 
    def __init__(self):
        self._fuel_capacity = 0
        self._max_speed = 0
        self._current_speed = 0 

    def set_speed(self, speed):
        self._current_speed = speed

    def get_speed(self):
        return self._current_speed

    def accelerate(self, mph):
        if self._current_speed + mph < max_speed:
            self._current_speed = self._current_speed + mph
        else: 
            print("This vehicle cannot go that fast.")

    def set_fuel_capacity(self, fuel):
        self._fuel_capacity = fuel

    def get_fuel_capacity(self):
        return self._fuel_capacity

    def set_max_speed(self, max):
        self._max_speed = max 

    def get_max_speed(self):
        return self._max_speed
    
# Motorcycle.py

from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, max_speed, current_speed, has_sidecar):
        super().__init__()
        self._has_sidecar = has_sidecar
        self._max_speed = max_speed
        self._current_speed = current_speed

    def set_sidecar(self, has_sidecar):
        self._has_sidecar = has_sidecar

    def get_sidecar(self):
        return self._has_sidecar

    @property
    def speed(self):
        return self._current_speed

    @property
    def sidecar(self):
        return self._has_sidecar

    def accelerate(self, mph):
        if self._current_speed + mph < self._max_speed:
            self._current_speed = self._current_speed + mph
        else: 
            print("This motorcycle cannot go that fast.")
            
# MyMotorcycleClassProgram.py 

from Motorcycle import Motorcycle

motorcycleOne = Motorcycle(90.0, 65.0, True)
motorcycleTwo = Motorcycle(85.0, 60.0, False)

motorcycleOne.accelerate(30.0)
motorcycleTwo.accelerate(20.0)

print("The current speed of motorcycleOne is " + str(motorcycleOne.speed))
print("The current speed of motorcycleTwo is " + str(motorcycleTwo.speed))

if motorcycleOne.get_sidecar():
   print("This motorcycle has a sidecar")
else:
   print("This motorcycle does not have a sidecar")

if motorcycleTwo.get_sidecar():
   print("This motorcycle has a sidecar")
else:
   print("This motorcycle does not have a sidecar")