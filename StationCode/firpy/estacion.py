from pyfire import pi_fire
from gpior import PIthing
from sht21 import SHT21
import datetime
#from Fecha_datos import*
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

#x=datetime.datetime.now()
#fecha="%s/%s/%s" % (x.day, x.month, x.year)
#fecha="%s" % (x.minute)

#archivo=open((str(x.hour)+"_"+str(x.minute)+".csv"),"a")
#archivo.write("fecha,valor0,valor1,valor2"+"\n")


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
    if(timetotal>=7):
        if cont>1:
            velprom=contvel/(cont-1)
        else:
            velprom=0
        """Envio de datos a firebase"""
        #fecha_dat()
        temperaturafin=("%2.2f" % SHT21(1).read_temperature())
        humedadfin=("%2.2f" % SHT21(1).read_humidity())
        vientofin=("%2.2f" % velprom)
        
        x=datetime.datetime.now()        
        fecha2="%s/%s/%s" % (x.day, x.month, x.year)
        tiempo="%s:%s:%s" % (x.hour,x.minute,x.second)
        datosfecha=str(humedadfin)+","+str(vientofin)+","+str(temperaturafin)+","+tiempo+","+fecha2
        firepi.addfire(datosfecha)

        '''
        firepi.addfire(tem,SHT21(0).read_temperature())
        firepi.addfire(hum,SHT21(0).read_humidity())
        firepi.addfire(vient,velprom)
        
        
        print ("Temperature: %s" % SHT21(1).read_temperature())
        print ("Humidity: %s" % SHT21(1).read_humidity())
        print ("vel Viento: %s" % velprom)
        '''

        """reset de variables"""
        valant=1
        flagtime1=True
        flagtime2=True
        velkh=0
        contvel=0
        cont=0
        velprom=0
        timeini=time.time()

gpio.gpioend()
archivo.close()        
            
                    
            
        
