from firebase import firebase

firebase=firebase.FirebaseApplication('https://frankstation-ffdb0.firebaseio.com/')


"""agregar o crear"""
"""result=firebase.get('/datos',None)"""
"""result=firebase.post('/user',{'nuevo':'val1'})"""
"""result=firebase.put('datos','temperatura',nuev)"""
result=firebase.put('datos','humedad',16.24)

"""eliminar"""
"""result=firebase.delete('/datos','temperatura')"""

print (result)
