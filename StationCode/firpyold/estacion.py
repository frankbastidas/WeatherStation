from pyfire import pi_fire
from gpior import PIthing
from sht21 import SHT21
import time
"""entradas"""
viento=4
"""variables meteorologicas y configuracion"""
tem='temperatura'
hum='humedad'
vient='Vel Viento'
firepi=pi_fire()
"""variables booleanas y contadores"""
pi=3.141592654
valant=1
cont=0
flagtime1=0
flagtime2=0
inicio1=0
inicio2=0
fin1=0
fin2=0
real_time=0
velkh=0
contvel=0
timefin=0
timetotal=0
velprom=0
"""configuracion de entradas y salidas GPIO"""
gpio=PIthing()
gpio.inpin(viento)
"""tiempo de inicio"""
timeini=time.time()

while True:
    stateVel=gpio.readpin(viento)
    #print stateVel
    if (stateVel==False):
        if(valant!=stateVel):                        
            cont=cont+1
            if(flagtime1==True):
                inicio1=time.time()
                flagtime1=False
                if(flagtime2==False):
                    fin2=time.time()
                    flagtime2=True
                    real_time=fin2-inicio2
                    velkh=3.0/20.0*pi*3.6/real_time                    
                    contvel=contvel+velkh
            
            else:
                fin1=time.time()
                flagtime1=True
                real_time=fin1-inicio1
                velkh=3.0/20.0*pi*3.6/real_time
                contvel=contvel+velkh
                if(flagtime2==True):
                    inicio2=time.time()
                    flagtime2=False
        valant=0
    else:
        valant=1

    timefin=time.time()
    timetotal=timefin-timeini
    if(timetotal>=13):
        if cont>1:
            velprom=contvel/(cont-1)
        else:
            velprom=0
        """Envio de datos a firebase"""        
        firepi.addfire(tem,round(SHT21(1).read_temperature(),2))
        firepi.addfire(hum,round(SHT21(1).read_humidity(),2))
        firepi.addfire(vient,round(velprom,2))
        

        #print ("Temperature: %s" % round(SHT21(1).read_temperature(),2))
        #print ("Humidity: %s" % round(SHT21(1).read_humidity(),2))
        #print ("vel Viento: %s" % round(velprom,2))

        """reset de variables"""
        valant=1
        flagtime1=True
        flagtime2=True
        velkh=0
        contvel=0
        cont=0
        timeini=time.time()

gpio.gpioend()                                          
