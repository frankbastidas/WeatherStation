import serial
import os,time

#enable serial Communication
port=serial.Serial("/dev/ttyS0", baudrate=115200, timeout=1)

#transmision de comandos AT
        
port.write('AT'+'\r\n')
rcv=port.read(10)
print (rcv)
time.sleep(1)

port.write('ATI'+'\r\n')
rcv=port.read(50)
print (rcv)
time.sleep(1)

"""
port.write('AT+CBAND=?'+'\r\n')
rcv=port.read(150)
print rcv
#time.sleep(1)

port.write('AT+CBAND?'+'\r\n')
rcv=port.read(150)
print rcv
#time.sleep(1)


port.write('AT+CBAND=EGSM_PCS_MODE'+'\r\n')
rcv=port.read(150)
print rcv
time.sleep(1)


#comunicacion con sim Movistar
port.write('AT+CBAND=EGSM_PCS_MODE'+'\r\n')
rcv=port.read(150)
print rcv
time.sleep(1)


port.write('AT+CSMINS?'+'\r\n')
rcv=port.read(150)
print rcv
#time.sleep(1)

port.write('AT+COPS?'+'\r\n')
rcv=port.read(150)
print rcv
#time.sleep(1)

port.write('AT+CSQ'+'\r\n')
rcv=port.read(150)
print rcv
#time.sleep(1)

port.write('AT+CFUN?'+'\r\n')
rcv=port.read(150)
print rcv
#time.sleep(1)

port.write('AT+CGATT?'+'\r\n')
rcv=port.read(150)
print rcv
#time.sleep(1)



port.write('AT+CBAND=EGSM_PCS_MODE'+'\r\n')
rcv=port.read(150)
print rcv
time.sleep(1)


port.write('AT+CSQ?'+'\r\n')
rcv=port.read(150)
print rcv
time.sleep(1)

port.write('AT+CPIN?'+'\r\n')
rcv=port.read(150)
print rcv
time.sleep(1)

port.write('AT+CREG?'+'\r\n')
rcv=port.read(150)
print rcv
time.sleep(1)

port.write('AT+CGATT?'+'\r\n')
rcv=port.read(150)
print rcv
time.sleep(1)

port.write('AT+CIPSTATUS'+'\r\n')
rcv=port.read(150)
print rcv
time.sleep(1)

port.write('AT+CGDCONT=1,\"IP\",\"internet.movistar.com.co\"'+'\r\n')
rcv=port.read(150)
print rcv
time.sleep(1)


port.write('AT+CSTT=\"lte.avantel.com.co\",\"avantel@datos",\"avantel\"'+'\r\n')
rcv=port.read(150)
print rcv
time.sleep(1)

port.write('AT+CREG?'+'\r\n')
rcv=port.read(150)
print rcv
time.sleep(1)

port.write('ATD*99#'+'\r\n')
rcv=port.read(150)
print rcv
time.sleep(3)

port.write('AT+CIPSHUT'+'\r\n')
rcv=port.read(150)
print rcv
time.sleep(1)

port.write('AT+CIFSR?'+'\r\n')
rcv=port.read(150)
print rcv
time.sleep(1)

port.write('AT+COPS?'+'\r\n')
rcv=port.read(10)
print rcv
time.sleep(1)

port.write('AT+COPS?'+'\r\n')
rcv=port.read(10)
print rcv
time.sleep(1)


port.write('AT+CIFSR'+'\r\n')
rcv=port.read(150)
print rcv

while  True:
    rcv=port.read(150)
    print rcv
"""
