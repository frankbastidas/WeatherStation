from flask import Flask, render_template, request, Response
from adquiere import valores, firebase, humedadn,velocidadn,temperaturan,fechan,horan
import time
import random, json
global n
app = Flask(__name__)
n=4

#nuevo=datosval
#lnuevo=['h2','h3']

@app.route('/valoresclimatologicas')
def clima():
    def generate():                        
        '''a=firebase.get('/datos',None)
        h=a['humedad']        
        t=a['temperatura']        
        v=a['Vel Viento']        '''
        humedadn2=[]
        velocidadn2=[]
        temperaturan2=[]
        horan2=[]
        fechan2=[]
        nuevo2={}             
        valores2=[]

        result=firebase.get('/datosclima',None)
        for _,v in result.items():
            valores2.append(v)
        
        nuevo2[0]=valores2[len(result)-1].split(",")
        humedadn2.append(nuevo2[0][0])
        velocidadn2.append(nuevo2[0][1])
        temperaturan2.append(nuevo2[0][2])
        horan2.append(nuevo2[0][3])
        fechan2.append(nuevo2[0][4])
        
        t=temperaturan2[len(temperaturan2)-1]
        v=velocidadn2[len(velocidadn2)-1]
        h=humedadn2[len(humedadn2)-1]
        horaactual=horan2
        valorescli={
            'temperatura': t,
            'velocidad': v,
            'humedad': h,
            'hora':horaactual
        }
        #pala2=str(h)+' %'
        #yield('data: {0}\n\n'.format(pala2))                                 
        yield('data: {0}\n\n'.format(json.dumps(valorescli)))             
    return Response(generate(), mimetype='text/event-stream')

'''
@app.route('/valordetemperaturareal')
def tempera():
    def generate2():        
        global t1
        a=firebase.get('/datos',None)    
        t=a['temperatura']
        #pala2=str(t)+' ºC'
        #yield('data: {0}\n\n'.format(pala2))   
        yield('data: {0}\n\n'.format(t))        
    return Response(generate2(), mimetype='text/event-stream')

@app.route('/valordevelocidadreal')
def veloc():
    def generate3():        
        global v1
        a=firebase.get('/datos',None)    
        v=a['Vel Viento']
        #pala2=str(v)+' Km/h'
        #yield('data: {0}\n\n'.format(pala2))
        yield('data: {0}\n\n'.format(v))        
    return Response(generate3(), mimetype='text/event-stream')
'''
@app.route('/index.html',methods=['GET','POST'])
@app.route('/')
def indexn():
    return render_template('index.html')

@app.route('/page2.html',methods=['GET','POST'])
@app.route('/page2')
def index():
    return render_template('page2.html',humedadn=humedadn,horan=horan)
    #return render_template('page2.html')

@app.route('/page3.html',methods=['GET','POST'])
@app.route('/page3')
def index2():    
    return render_template('page3.html',velocidadn=velocidadn,horan=horan)

@app.route('/page4.html',methods=['GET','POST'])
@app.route('/page4')
def index3():    
    return render_template('page4.html',temperaturan=temperaturan,horan=horan)

@app.route('/page5.html',methods=['GET','POST'])
@app.route('/page5')
def index4():    
    return render_template('page5.html')

@app.route('/page6.html',methods=['GET','POST'])
@app.route('/page6')
def index5():    
    return render_template('page6.html')

@app.route('/page7.html',methods=['GET','POST'])
@app.route('/page7')
def index6():    
    return render_template('page7.html')

@app.route('/page1.html',methods=['GET','POST'])
@app.route('/page1')
def page2():        
    result=firebase.get('/datosclima',None)    
    
    valores=[]

    humedadn=[]
    velocidadn=[]
    temperaturan=[]
    horan=[]    
    nuevo={}

    for _,v in result.items():
        valores.append(v)    
    n=0    

    for i in range(len(result)-42,len(result)):
        nuevo[n]=valores[i].split(",")
        humedadn.append(nuevo[n][0])
        velocidadn.append(nuevo[n][1])
        temperaturan.append(nuevo[n][2])
        horan.append(nuevo[n][3])        
        n=n+1
    nuevo=[0]
    return render_template('page1.html',temperaturan=temperaturan,humedadn=humedadn,velocidadn=velocidadn,horan=horan)

if __name__=='__main__':
    app.run(port=3000,debug=True,threaded=True)
    