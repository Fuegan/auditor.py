#!/usr/bin/env python

import os
#import nmap
print("Bienvenido al creador de estructuras de carpetas para auditoria v 0.1")
empresa = input('Por favor introduzca el nombre de la empresa a auditar:')
auditor=input('Por favor introduzca el nombre del auditor asignado:')
#rango=input('Por favor introduzca la subred a auditar (Direccion ip/mascara de red):')
ruta=os.environ["HOME"]+str("/Auditoria/")+str(empresa)
os.makedirs(ruta+"/imagenes_videos/Escaneo")
os.makedirs(ruta+"/imagenes_videos/Reconocimiento")
os.makedirs(ruta+"/imagenes_videos/Analisis_vulnerabilidades")
os.makedirs(ruta+"/imagenes_videos/Explotacion")
os.makedirs(ruta+"/Reporte_aplicaciones")
os.makedirs(ruta+"/Data")
fb=str(ruta)+str('bitacora.txt')
bitacora=open( fb , 'w')
bitacora.write('Auditoria:\nEmpresa: '+ empresa + '\nAuditor asignado: '+auditor +  '\nBitacora dia 1:\n')
bitacora.close()
