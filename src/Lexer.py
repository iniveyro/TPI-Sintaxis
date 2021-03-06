import ply.lex as lex
import re
import codecs
import os
import sys
 
tokens = ['XMLCIERRE','XMLINICIO',
		'NUMERO','CERRADURA',
		'ENCODING','HTTP','HTTPS','FTP','FTPS',
		'IMAGEAPERTURA',
		'IMAGECERRADURA',
		'TEXTO','VERSION',
		'RSSAPERTURA',
		'DESCRIPTIONAPERTURA',
		'CHANNELAPERTURA',
		'ITEMAPERTURA',
		'LINKAPERTURA',
		'TITLEAPERTURA',
		'RSSCERRADURA',
		'DESCRIPTIONCERRADURA',
		'CHANNELCERRADURA',
		'ITEMCERRADURA',
		'LINKCERRADURA',
		'TITLECERRADURA','CATEGORYAPERTURA','CATEGORYCERRADURA',
		'URLAPERTURA','URLCERRADURA',
		'HEIGHTAPERTURA','HEIGHTCERRADURA',
		'WIDTHAPERTURA','WIDTHCERRADURA',
		'COPYRIGHTAPERTURA','COPYRIGHTCERRADURA','LINK','RANGOH','RANGOW']

t_ignore = ' \t'
 
def t_VERSION(t):
	r'[v][e][r][s][i][o][n][=]["][\d][\d\.]*["][\s]*'
	return (t)

def t_ENCODING(t):
	r'[e][n][c][o][d][i][n][g][=]["][uU][tT][fF][-][8]["][\s]*'
	return (t)

#PAG
def t_LINK(t):
	r'[/][a-zA-Z][a-zA-Z\.]*[a-zA-Z/][a-zA-Z0-9,-\.\s/?=:%&-()_#–/]*'
	return (t)

def t_HTTP(t):
	r'[h][t][t][p][:][/]'
	return (t)

def t_HTTPS(t):
	r'[h][t][t][p][s][:][/]'
	return (t)

def t_FTP(t):
	r'[f][t][p][:][/]'
	return (t)

def t_FTPS(t):
	r'[f][t][p][s][:][/]'
	return (t)

def t_RANGOW(t):
	r'[0-1][0-9][0-9]'
	return t

def t_RANGOH(t):
	r'[0-3][0-9][0-9]'
	return t
		

t_XMLCIERRE= r'\?>'
t_XMLINICIO= r'<\?xml'
t_CERRADURA= r'>'
t_RSSAPERTURA= r'<rss'
t_CHANNELAPERTURA= r'<channel>'
t_ITEMAPERTURA= r'<item>'
t_DESCRIPTIONAPERTURA= r'<description>'
t_LINKAPERTURA= r'<link>'
t_TITLEAPERTURA= r'<title>'
t_CATEGORYAPERTURA = r'<category>'
t_IMAGEAPERTURA=r'<image>'
t_URLAPERTURA=r'<url>'
t_COPYRIGHTAPERTURA=r'<copyright>'
t_COPYRIGHTCERRADURA=r'</copyright>'
t_HEIGHTAPERTURA=r'<height>'
t_WIDTHAPERTURA=r'<width>'
t_IMAGECERRADURA=r'</image>'
t_URLCERRADURA=r'</url>'
t_HEIGHTCERRADURA=r'</height>'
t_WIDTHCERRADURA=r'</width>'
t_CATEGORYCERRADURA = r'</category>'
t_RSSCERRADURA= r'</rss>'
t_CHANNELCERRADURA= r'</channel>'
t_ITEMCERRADURA= r'</item>'
t_DESCRIPTIONCERRADURA= r'</description>'
t_LINKCERRADURA= r'</link>'
t_TITLECERRADURA= r'</title>'

def t_NUMERO(t):
	r'[\d][\d\.]*'
	return (t)

def t_TEXTO(t):
	r'[a-zA-Z][a-zA-Z0-9,-\.\s/?=:%&-()_À-ÿ–]*'
	return (t)

def t_newline(t):
	r'\r\n+'
	t.lexer.lineno += len(t.value)

def t_error(t):
	print(" - Caracter Ilegal - '%s'" % t.value[0])
	t.lexer.skip(1)

analizador = lex.lex()

#def Inicio():
#	print ("	LEXER - RSS 	")
#	print ("Grupo: 4. \n")
#	print ("Que accion desea realizar? \n")
#	print (" * (1) Redactar codigo manualmente.")
#	print (" * (2) Abrir codigo desde un archivo.")
#	print (" * (Cualquier tecla) Cerrar programa.\n")
#	x=input ("Seleccione la accion a realizar: ")
#	if (x=="1"):
#		Manual()
#	elif (x=="2"):
#		Arch()
#	else:
#		print("Fin Del Programa.")	

#def buscarFichero(directorio):
#	print("Listado de archivos:")
#	fichero = []
#	numArch = ''
#	respuesta = False
#	cont = 1
#	for base,dirs,files in os.walk(directorio):
#		fichero.append(files)
#	for file in files:
#		print (str(cont)+". "+file)
#		cont=cont+1
#	print("\n")
#	while respuesta == False:
#		numArch= input('Seleccione el archivo a cargar: ')
#		for file in files:
#			if (file == files[int(numArch)-1]):
#				respuesta = True
#				break
#	return files[(int(numArch))-1]

#def Arch():
#	directorio = os.getcwd() + '\\'
#	archivo = buscarFichero(directorio)
#	test = directorio + archivo
#	fp = codecs.open(test,"r","utf-8")
#	cadena = fp.read()
#	fp.close()
#	Lexer(cadena)

#def Manual():
#	cadena = ''
#	while True:
#		try:
#			cad = input('> ')
#			if (cad == ''):
#				break	
#			cadena = cadena+cad+ '\n'
#		except EOFError:
#			break
#		if not cadena: continue
#	print ('\n')
#	Lexer(cadena)

#def Lex(cadena):
#	analizador = lex.lex()
#	analizador.input(cadena)
#	print(" * Listado de tokens * \n")
#	while True:
#		tok = analizador.token()
#		if not tok : break
#		print (tok)
#	print('')	
#	salida=input('PRESIONE CUALQUIER TECLA PARA FINALIZAR...')
#Inicio()