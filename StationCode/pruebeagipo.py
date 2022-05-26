from pyfire import pi_fire
from gpior import PIthing
from sht21

"""entradas"""
viento=24
"""variables booleanas"""
valant=1
"""configuracion de entradas GPIO""
gpio=PIthing()
gpio.inpin(viento)

while True:
    stateVel=gpio.readpin(viento)
    if (stateVel==0):
        
