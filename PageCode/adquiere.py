from firebase import firebase
import json
from time import gmtime,strftime
import random,datetime

autenticacion=firebase.FirebaseAuthentication(secret='l314GJTofs2o1tXZqWNlpKPWcL49uofVtTZ2Zl9X',email='frank940919@gmail.com')

firebase = firebase.FirebaseApplication('https://frankstation-ffdb0.firebaseio.com',authentication=autenticacion)

#_=firebase.post('/datosclima',fecha)
result=firebase.get('/datosclima',None)
cont=0

#print(len(result))
valores=[]
#datosval=[]

humedadn=[]
velocidadn=[]
temperaturan=[]
horan=[]
fechan=[]
p2=[]
nuevo={}

for _,v in result.items():
    valores.append(v)

#nuevo[0]=valores[len(result)-1].split(",")
#print(nuevo[0])
n=0
#460 datos en 1 hora
#['82.71', '0.00', '21.39', '18:51:18', '17/10/2018']

for i in range(len(result)-42,len(result)):
    nuevo[n]=valores[i].split(",")
    humedadn.append(nuevo[n][0])
    velocidadn.append(nuevo[n][1])
    temperaturan.append(nuevo[n][2])
    horan.append(nuevo[n][3])
    fechan.append(nuevo[n][4])
    n=n+1
nuevo=[0]
#print(horan[len(horan)-1])