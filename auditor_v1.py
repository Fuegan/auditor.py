#!/usr/bin/env python
#############################################################################################
# Script para ayudar a organizar los datos de una auditoria de hacking                      #
# Autor:Fuegan                                                                              #
# email: albertogasco@gmail.com                                                             #
#############################################################################################

# -*- coding: utf-8 -*-

import os
import time
#import nmap

#Declaracion de variables globales
ruta=str(os.environ["HOME"]+str("/Auditoria/"))

#Creacion de carpetas donde contener la informacion
def Auditoria():
	texto="Seleccione la empresa que deseas auditar:\n"
	empresa, auditor = Empresa(texto)
	ruta=os.environ["HOME"]+str("/Auditoria/")+ empresa
	NuevaCarpeta(ruta+"/imagenes_videos/Escaneo")
	NuevaCarpeta(ruta+"/imagenes_videos/Reconocimiento")
	NuevaCarpeta(ruta+"/imagenes_videos/Analisis_vulnerabilidades")
	NuevaCarpeta(ruta+"/imagenes_videos/Explotacion")
	NuevaCarpeta(ruta+"/Reporte_aplicaciones")
	NuevaCarpeta(ruta+"/Data")
	archivo=str(ruta)+str('/bitacora.txt')
	comprobacion = os.path.exists(archivo)
	if comprobacion == False:
		contenido =('Auditoria:\n\nEmpresa: '+ str(empresa) + '\nAuditor asignado: '+ auditor +  '\n' + "Fecha de comienzo. ------- " + str(time.strftime('%y %b %d') + " - " + time.strftime('%H:%M')))
	else:
		contenido = "\nFecha de comienzo" + str(time.strftime('%y %b %d') + " - " + time.strftime('%H:%M'))
	NuevoArchivo(archivo,contenido)
	Menu()

#Funcion para comprobar existencia de archivo y si no crearlo
def NuevoArchivo(pathcompleto, contenido):
	archivo = os.path.exists(pathcompleto)
	if archivo == True:
		historico=open( pathcompleto , 'a')
		historico.write(contenido + "\n")
		historico.close()
	else:
		historico=open(pathcompleto, 'w')
		historico.write(contenido + "\n")
		historico.close()
	

#Funcion para comprobar existencia de carpeta y si no existe crearla 
def NuevaCarpeta (path):
	carpeta = os.path.exists(path)
	if carpeta == False:	
		os.makedirs(path)
	
#Funcion para registrar una nueva empresa
def NuevaEmpresa():
	os.system('clear') 
	empresa = input('Por favor introduzca el nombre de la empresa a auditar:')
	auditor=input('Por favor introduzca el nombre del auditor asignado:')
	NuevaCarpeta(ruta)
	ruta1 = ruta + str("configuracion/")
	nombre = "historico.cfg"
	configuracion = os.path.exists(os.environ["HOME"] + "/configuracion")
	registro = empresa + ";" + str(time.strftime('%y %b %d') + ";" + auditor +";" + ruta1 + empresa)
	NuevaCarpeta (ruta1)
	archivo = (ruta1+nombre)
	NuevoArchivo (archivo,registro)
	Menu()

#Eleccion de presa a la que auditar
def Empresa (texto):
	os.system('clear') 
	print (texto)
	historico= ruta + "/configuracion/historico.cfg"
	archi=open( historico ,'r')
	linea=archi.readline()
	contador = 1
	opciones = []
	while linea != "":
		lista = linea.split(";")
		print ( str(contador) + ".- " + lista[0])
		opciones.append(lista[0]) 
		contador = contador+1
		linea=archi.readline()
	archi.close()
	opcion = int(input("La opcion elegida es:"))
	return opciones[opcion-1],lista[2]
#Funcion para añadir bitacora a un archivo existente
def Bitacora():
	os.system('clear')
	texto= "Seleccione la auditoria que quiere continuar\n"
	empresa,auditor=Empresa(texto)
	archivo=ruta+empresa+"/bitacora.txt"
	print (empresa)
	editar=open( archivo , 'a')
	editar.write('\n' + time.strftime('%y %b %d') + " - " + time.strftime('%H:%M')+ "\n")
	editar.close()
	nano = "nano " + str(archivo)
	os.system(nano)
	Menu()
	
#Menu inicial de la aplicacion
def Menu():
	os.system('clear') 
	print ("Bienvenido al creador de estructuras de carpetas para auditoria v 0.2")
	opcion = input ("Selecione la opcion que desea realizar:\n\n1.-Registrar empresa a auditar.\n2.-Comenzar nueva auditoria.\n3.-Editar bitacora de una auditoria existente.\n4.-Salir.\n\n Opcion elegida: ")
	print (opcion)
	if opcion == '1':
		NuevaEmpresa()
	elif opcion == '2':
		Auditoria()
	elif opcion == '3':
		Bitacora()
	elif opcion == '4':
		os.system('clear') 
		exit()
	else:
		print ("La opcion elegida no es valida")

Menu()
