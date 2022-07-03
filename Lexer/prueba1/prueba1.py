import ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['XMLCIERRE',
		'XMLINICIO',
		'COMILLAS',
		'IGUAL',
		'COMILLASDOBLES',
		'COMILLASSIMPLES',
		'SALTOLINEA',
		'NUMERO',
		'CERRADURA',
		'ENCODING',
		'ITEMINICIO',
		'ITEMCIERRE',
		'TEXTO','VERSION',
		'RSSAPERTURA',
		'DESCRIPTIONAPAERTURA',
		'CHANNELAPERTURA',
		'ITEMAPERTURA',
		'LINKAPERTURA',
		'TITLEAPERTURA',
		'RSSCERRADURA',
		'DESCRIPTIONCERRADURA',
		'CHANNELCERRDAURA',
		'ITEMCERRADURA',
		'LINKCERRADURA',
		'TITLECERRADURA','IGUAL',
		'PROTOCOLO',
		'BARRA','FORMATOCODIF']

t_ignore = ' \t'

def t_VERSION(t):
	r'[v][e][r][s][i][o][n][\s=]*'
	return t

def t_ENCODING(t):
	r'[e][n][c][o][d][i][n][g][\s=]*'
	return t

def t_PROTOCOLO(t):
	r'[hf][t][t][p][:s][:/]*'
	return t

t_COMILLASDOBLES=r'"'
t_COMILLASSIMPLES=r'\''
t_BARRA= r'/'
t_XMLCIERRE= r'\?>'
t_XMLINICIO= r'<\?xml'
t_IGUAL= r'='
t_CERRADURA= r'>'
t_RSSAPERTURA= r'<rss'
t_CHANNELAPERTURA= r'<channel>'
t_ITEMAPERTURA= r'<item>'
t_DESCRIPTIONAPAERTURA= r'<description>'
t_LINKAPERTURA= r'<link>'
t_TITLEAPERTURA= r'<title>'

t_RSSCERRADURA= r'</rss>'
t_CHANNELCERRDAURA= r'</channel>'
t_ITEMCERRADURA= r'</item>'
t_DESCRIPTIONCERRADURA= r'</description>'
t_LINKCERRADURA= r'</link>'
t_TITLECERRADURA= r'</title>'

def t_FORMATOCODIF(t):
	r'[uU][tT][fF][-][\d]'
	return t

def t_NUMERO(t):
	r'[\d][\d\.]*'
	return t

def t_TEXTO(t):
	r'[a-zA-Z][a-zA-Z0-9,-\.\s/?=:%&]*'
	return t

def t_SALTOLINEA(t):
	r'\r\n+'
	t.lexer.lineno += len(t.value)
	return t

def t_error(t):
	print(" - Caracter Ilegal - '%s'" % t.value[0])
	t.lexer.skip(1)

##############################################

def Inicio():
	print ("	LEXER - RSS 	")
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
	directorio = os.getcwd() + '\\'
	archivo = buscarFichero(directorio)
	test = directorio + archivo
	fp = codecs.open(test,"r","utf-8")
	cadena = fp.read()
	fp.close()
	Lexer(cadena)

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
	Lexer(cadena)

def Lexer(cadena):
	analizador = lex.lex()
	analizador.input(cadena)
	print(" * Listado de tokens * \n")
	while True:
		tok = analizador.token()
		if not tok : break
		print (tok)

Inicio()

########################################################

# <?xml version="1.0" encoding="UTF-8" ?>
# <rss version="2.0">
# <channel>
# <title>RSS de la cátedra de Sintaxis y Semántica de Lenguajes </title>
# <link>https://frre.cvg.utn.edu.ar/course/view.php?id=399</link>
# <description>Sintaxis y Semántica de Lenguajes de la U.T.N.F.R.Resistencia. </description>
# <item>
# <title>Planificacion 2022</title>
# <link>https://</link>
# <description>Planificacion de catedra, con cronograma de clases y evaluaciones</description>
# </item>
# <item>
# <title>Guia de Trabajos practicos</title>
# <link>https://</link>
# <description>Guía de ejercicios propuestos a resolver en clase practica</description>
# </item>
# <item>
# <title>Enunciado TPI</title>
# <link>https://wl</link>
# <description>Trabajo práctico integrador</description>
# </item>
# </channel>
# </rss>