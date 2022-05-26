from firebase import firebase

firebase=firebase.FirebaseApplication('https://frankstation-ffdb0.firebaseio.com/')

class pi_fire(object):
    def addfire(self,valor):
        #result=firebase.put('datos',nombre,valor)
        _=firebase.post('datosclima',valor)

    def delfire(self,nomb):
        _=firebase.delete('/datosclima',nomb)


"""agregar o crear"""
"""result=firebase.get('/user',None)"""
"""result=firebase.post('/user',{'nuevo':'val1'})"""
"""result=firebase.put('datos','temperatura',nuev)"""
"""result=firebase.put('datos','humedad',nuev)"""

"""eliminar"""
"""result=firebase.delete('/datos','temperatura')"""

"""print (result)"""
