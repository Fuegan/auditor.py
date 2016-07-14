#!/usr/bin/env python

import os
import time
#import nmap


#Introducir informacion basica sobre la auditoria
print("Bienvenido al creador de estructuras de carpetas para auditoria v 0.2")
empresa = input('Por favor introduzca el nombre de la empresa a auditar:')
auditor=input('Por favor introduzca el nombre del auditor asignado:')
#rango=input('Por favor introduzca la subred a auditar (Direccion ip/mascara de red):')

#Creacion de carpetas donde contener la informacion
ruta=os.environ["HOME"]+str("/Auditoria/")+str(empresa)
os.makedirs(ruta+"/imagenes_videos/Escaneo")
os.makedirs(ruta+"/imagenes_videos/Reconocimiento")
os.makedirs(ruta+"/imagenes_videos/Analisis_vulnerabilidades")
os.makedirs(ruta+"/imagenes_videos/Explotación")
os.makedirs(ruta+"/Reporte_aplicaciones")
os.makedirs(ruta+"/Data")
#Creacion de archivo de bitacora
fb=str(ruta)+str('/bitacora.txt')
bitacora=open( fb , 'w')
bitacora.write('Auditoria:\nEmpresa: '+ empresa + '\nAuditor asignado: '+auditor +  '\nBitacora:\n')
bitacora.close()
bitacora=open( fb , 'a')
ahora = str(time.strftime('%y %b %d') + " - " + time.strftime('%H:%M'))
bitacora.write(ahora)
bitacora.close()
