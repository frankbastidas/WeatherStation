import datetime
import time
import random


def fecha_dat(self):
    #hora local    
    x=datetime.datetime.now()
    fecha2="%s/%s/%s" % (x.day, x.month, x.year)
    #fecha2="%s" % (x.minute)

    tiempo="%s:%s:%s" % (x.hour,x.minute,x.second)    

    #valor variables con 2 decimales
    y=str("%.2f" % (SHT21(1).read_temperature()))
    z=str("%.2f" % (SHT21(1).read_humidity()))
    v=str("%.2f" % (velprom))
    ###############
    #cambiar de archivo por dia
    if fecha2!=fecha:
        archivo.close()
        ########################
        #creacion de carpeta escritura de variables a carpeta
        #archivo=open((str(x.year)+"_"+str(x.month)+"_"+str(x.day)+".csv"),"a")
        archivo=open((str(x.hour)+"_"+str(x.minute)+".csv"),"a")
        archivo.write("fecha,valor0,valor1,valor2"+"\n")    
        fecha=fecha2    
        
    archivo.write(tiempo + "," + y +"," + z +"," + v +"\n")
    #############################
    #visualizacion
    #print ("%s , %s" % (tiempo,y))
    


