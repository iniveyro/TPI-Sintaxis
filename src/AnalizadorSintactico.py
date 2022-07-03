import ply.yacc as yacc
import re
import codecs
import os
 
direccion = os.getcwd()

from Lexer import tokens
from sys import stdin

precendece = (
	('right','VERSION','ENCODING','NUMERO','TEXTO','URLA','URLB','LINKA','LINKB'),
	('left','DESCRIPTIONAPERTURA','DESCRIPTIONCERRADURA','TITLEAPERTURA','TITLECERRADURA','LINKAPERTURA','LINKCERRADURA'),
	('left','ITEMAPERTURA','ITEMCERRADURA','URLAPERTURA','URLCERRADURA'),
	('left','IMAGEAPERTURA','IMAGECERRADURA','COPYRIGHTAPERTURA','COPYRIGHTCERRADURA','CATEGORYAPERTURA','CATEGORYCERRADURA'),
	('left','CHANNELAPERTURA','CHANNELCERRADURA'),
	('left','RSSAPERTURA','RSSCERRADURA','CERRADURA'),
	('left','XMLINICIO','XMLCIERRE'),
	)

def p_sigma(p):
	'''sigma : a''' 
	print ("sigma")

def p_a(p):
	'''a : xml rss ''' 
	print ("a")

#ENCABEZADO XML

def p_xml(p):
	'''xml : XMLINICIO b XMLCIERRE ''' 
	print ("xml")

def p_b1(p):
	'''b : VERSION''' 
	print ("b 1")

def p_b2(p):
	'''b : VERSION ENCODING '''
	print ("b 2")

#CUERPO DEL RSS
 
def p_rss(p):
	'''rss : RSSAPERTURA VERSION CERRADURA channel RSSCERRADURA '''
	print ("rss")

def p_channel1(p):
	'''channel : CHANNELAPERTURA contchannel CHANNELCERRADURA channel '''
	print ("channel 1")

def p_channel2(p):
	'''channel : CHANNELAPERTURA contchannel CHANNELCERRADURA'''
	print ("channel 2")

def p_contchannel1(p):
	'''contchannel : title link desc item'''
	print ("contchannel 1")

def p_contchannel2(p):
	'''contchannel : title link desc opcionales item'''
	print ("contchannel 2")

def p_opcionales1(p):
	'''opcionales : category'''
	print ("opcionales 1")

def p_opcionales2(p):
	'''opcionales : category copy '''
	print ("opcionales 2")

def p_opcionales3(p):
	'''opcionales : copy '''
	print ("opcionales 3")

def p_opcionales4(p):
	'''opcionales : image'''
	print ("opcionales 4")

def p_opcionales5(p):
	'''opcionales : category copy image '''
	print ("opcionales 5")

def p_opcionales6(p):
	'''opcionales : copy image '''
	print ("opcionales 6")

def p_image(p):
	'''image : IMAGEAPERTURA url title link dimensiones IMAGECERRADURA'''
	print ("image")

def p_dimensiones(p):
	'''dimensiones : HEIGHTAPERTURA NUMERO HEIGHTCERRADURA WIDTHAPERTURA NUMERO WIDTHCERRADURA'''
	print ("dimensiones")

def p_category(p):
	'''category : CATEGORYAPERTURA TEXTO CATEGORYCERRADURA '''
	print ("category")

def p_copy(p):
	'''copy : COPYRIGHTAPERTURA TEXTO COPYRIGHTCERRADURA'''
	print ("copy")

def p_link1(p):
	'''link : LINKAPERTURA LINKA LINKCERRADURA '''
	print ("link - http o fttp")

def p_link2(p):
	'''link : LINKAPERTURA LINKB LINKCERRADURA '''
	print ("link - https o fttps")

def p_title(p):
	'''title : TITLEAPERTURA TEXTO TITLECERRADURA '''
	print ("title")

def p_desc(p):
	'''desc : DESCRIPTIONAPERTURA TEXTO DESCRIPTIONCERRADURA '''
	print ("desc")

def p_url1(p):
	'''url : URLAPERTURA LINKA URLCERRADURA '''
	print ("url - http o fttp")

def p_url2(p):
	'''url : URLAPERTURA LINKB URLCERRADURA '''
	print ("url - https o fttps")

def p_item1(p):
	'''item : ITEMAPERTURA contitem ITEMCERRADURA item '''
	print ("item 1")

def p_item2(p):
	'''item : ITEMAPERTURA contitem ITEMCERRADURA '''
	print ("item 2")

def p_contitem1(p):
	'''contitem : title link desc '''
	print ("contitem 1")

def p_contitem2(p):
	'''contitem : title link desc category '''
	print ("contitem 2")

#PRODUCCIONES A IGNORAR

def p_error(p):
	print("Error Sintaxis",p)
	print("En la linea"+str(p.lineno))

#Procedimientos del Programa

def Inicio():
	print ("	ANALIZADOR - RSS 	")
	print ("Grupo: 4. \n")
	print ("Que accion desea realizar? \n")
	print (" * (1) Redactar codigo manualmente.")
	print (" * (2) Abrir codigo desde un archivo.")
	print (" * (Cualquier tecla) Cerrar programa.\n")
	x=input ("Seleccione la accion a realizar: ")

	if (x=="1"):
		Manual()
	elif (x=="2"):
		Arch()
	else:
		print("Fin Del Programa.")	

def buscarFichero(directorio):
	print("Listado de archivos:")
	fichero = []
	numArch = ''
	respuesta = False
	cont = 1
	for base,dirs,files in os.walk(directorio):
		fichero.append(files)
	for file in files:
		print (str(cont)+". "+file)
		cont=cont+1
	print("\n")
	while respuesta == False:
		numArch= input('Seleccione el archivo a cargar: ')
		for file in files:
			if (file == files[int(numArch)-1]):
				respuesta = True
				break

	return files[(int(numArch))-1]

def Arch():
	directorio = direccion + '/test/'
	archivo = buscarFichero(directorio)
	test = directorio + archivo
	fp = codecs.open(test,"r","utf-8")
	cadena = fp.read()
	fp.close()
	parser = yacc.yacc()
	result = parser.parse(cadena)
	print(result)

def Manual():
	cadena = ''
	while True:
		try:
			cad = input('> ')
			if (cad == ''):
				break	
			cadena = cadena+cad+ '\n'
		except EOFError:
			break
		if not cadena: continue
	print ('\n')

	parser = yacc.yacc()
	result = parser.parse(cadena)
	print(result)

#Ejecucion del programa

Inicio()