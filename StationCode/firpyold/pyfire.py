from firebase import firebase

firebase=firebase.FirebaseApplication('https://frankstation-ffdb0.firebaseio.com/')

class pi_fire(object):
    def addfire(self,nombre,valor):
        try:
            result=firebase.put('datos',nombre,valor)
        except IOError, e:
            return 0
            

    def delfire(self,nomb):
        result=firebase.delete('/datos',nomb)


"""agregar o crear"""
"""result=firebase.get('/user',None)"""
"""result=firebase.post('/user',{'nuevo':'val1'})"""
"""result=firebase.put('datos','temperatura',nuev)"""
"""result=firebase.put('datos','humedad',nuev)"""

"""eliminar"""
"""result=firebase.delete('/datos','temperatura')"""

"""print (result)"""
