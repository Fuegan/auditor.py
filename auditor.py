
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
