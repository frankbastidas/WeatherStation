from firebase import firebase

firebase=firebase.FirebaseApplication('https:frankstation-ffdb0.firebaseio.com')

result=firebase.put('dato4','nuevo')
print (result)
