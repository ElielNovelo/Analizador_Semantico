import ply.yacc as yacc
from Analizador_lexico import tokens

resultado_gramatica = []
type_variables = {} #GUARDA LAS VARIBLES CON SU TIPO Y VALOR
tipo_salida = [] #GUARDA SI LA EJECUCION ES EXITOSA O ERRONEA
variable = "" #GUARDA EL NOMBRE DE LA VARIABLE
typo = "" #GUARDA EL TYPO DE LA VARIABLE
list_valor = [] # PARA GUARDAS EL CONTENIDO DE LA VARIABLE DONTENIDA EN EL DICCIONARIO ESTO PARA PODER TRATARLO
 
precedence = (
    ('left', 'SEMI'),
    ('left', 'EQUALS'),
    ('left', 'MENORQ', 'MAYORQ',
     'MENORIGUAL', 'MAYORIGUAL'),
    ('left', 'MULTI','DIVISION'),
    ('left', 'SUMA','RESTA'),
)

nombres = {}

def SemanticaINT(t): #FUNCION PARA IDENTIFICAR SI LA ASIGNACION QUE SE LE HACE A LA VARIABLE
    #CORRESPONDE A TIPO DE VARIABLE DECLARADA (INT, DOUBLE)
    lista = t
    global list_valor
    global tipo_salida
    list_valor = lista[variable]
    # print(type(list_valor[1]).__name__)
    if list_valor[0] == (type(list_valor[1]).__name__) :
        tipo_salida.append('Ejecucion Exitosa')
    else :
        tipo_salida.append('Error “Asignación de tipo {} incorrecta”'.format(list_valor[0]))

def SemanticaF(t):
    #FUNCION PARA IDENTIFICAR SI LA ASIGNACION QUE SE LE HACE A LA VARIABLE
    #CORRESPONDE A TIPO DE VARIABLE DECLARADA (INT, DOUBLE)
    lista = t
    global list_valor
    global tipo_salida
    list_valor = lista[variable]
    if (type(list_valor[1]).__name__) == 'float' : bol = 'double' 
    else : bol = ''
    if list_valor[0] == bol :
        tipo_salida.append('Ejecucion Exitosa')
    else :
        tipo_salida.append('Error “Asignación de tipo {} incorrecta”'.format(list_valor[0]))

def SemanticaFloat(t):
    #FUNCION PARA IDENTIFICAR SI LA ASIGNACION QUE SE LE HACE A LA VARIABLE
    #CORRESPONDE A TIPO DE VARIABLE DECLARADA (INT, DOUBLE)
    lista = t
    global list_valor
    global tipo_salida
    list_valor = lista[variable]
    if list_valor[0] == (type(list_valor[1]).__name__) :
        tipo_salida.append('Ejecucion Exitosa')
    else :
        tipo_salida.append('Error “Asignación de tipo {} incorrecta”'.format(list_valor[0]))

def SemanticaBool(t):
    #FUNCION PARA IDENTIFICAR SI LA ASIGNACION QUE SE LE HACE A LA VARIABLE
    #CORRESPONDE A TIPO DE VARIABLE DECLARADA (INT, DOUBLE)
    lista = t
    global list_valor
    global tipo_salida
    list_valor = lista[variable]
    if list_valor[0] == (type(list_valor[1]).__name__) :
        tipo_salida.append('Ejecucion Exitosa')
    else :
        tipo_salida.append('Error “Asignación de tipo {} incorrecta”'.format(list_valor[0]))

def SemanticaString(t):
    #FUNCION PARA IDENTIFICAR SI LA ASIGNACION QUE SE LE HACE A LA VARIABLE
    #CORRESPONDE A TIPO DE VARIABLE DECLARADA (INT, DOUBLE)
    lista = t
    global list_valor
    global tipo_salida
    list_valor = lista[variable]
    if list_valor[0] == 'string' : bol = 'str' 
    else : bol = ''
    if bol == (type(list_valor[1]).__name__) :
        tipo_salida.append('Ejecucion Exitosa')
    else :
        tipo_salida.append('Error “Asignación de tipo {} incorrecta”'.format(list_valor[0]))


def SemanticaString_linedw(t):
    #FUNCION PARA IDENTIFICAR SI LA ASIGNACION QUE SE LE HACE A LA VARIABLE
    #CORRESPONDE A TIPO DE VARIABLE DECLARADA (INT, DOUBLE)
    lista = t
    global list_valor
    global tipo_salida
    global aviso
    list_valor = lista[variable]
    if type(typo).__name__ == 'str' : bol = 'string' 
    else : bol = ''
    if list_valor == bol :
        tipo_salida.append('Ejecucion Exitosa')
    else :
        tipo_salida.append('Error “Asignación de tipo {} incorrecta”'.format(list_valor))

def SemanticaBool_linedw(t):
    #FUNCION PARA IDENTIFICAR SI LA ASIGNACION QUE SE LE HACE A LA VARIABLE
    #CORRESPONDE A TIPO DE VARIABLE DECLARADA (INT, DOUBLE)
    lista = t
    global list_valor
    global tipo_salida
    list_valor = lista[variable]
    if list_valor == type(typo).__name__ :
        tipo_salida.append('Ejecucion Exitosa')
    else :
        tipo_salida.append('Error “Asignación de tipo {} incorrecta”'.format(list_valor))

def SemanticaFloat_linedw(t):
    #FUNCION PARA IDENTIFICAR SI LA ASIGNACION QUE SE LE HACE A LA VARIABLE
    #CORRESPONDE A TIPO DE VARIABLE DECLARADA (INT, DOUBLE)
    lista = t
    global list_valor
    global tipo_salida
    list_valor = lista[variable]
    if list_valor == type(typo).__name__ :
        tipo_salida.append('Ejecucion Exitosa')
    else :
        tipo_salida.append('Error “Asignación de tipo {} incorrecta”'.format(list_valor))

def SemanticaF_linedw(t):
    #FUNCION PARA IDENTIFICAR SI LA ASIGNACION QUE SE LE HACE A LA VARIABLE
    #CORRESPONDE A TIPO DE VARIABLE DECLARADA (INT, DOUBLE)
    lista = t
    global list_valor
    global tipo_salida
    global aviso
    list_valor = lista[variable]
    if type(typo).__name__ == 'float' : bol = 'double' 
    else : bol = ''
    if list_valor == bol :
        tipo_salida.append('Ejecucion Exitosa')
    else :
        tipo_salida.append('Error “Asignación de tipo {} incorrecta”'.format(list_valor))
    

def Semantica_linedw(t):
    #FUNCION PARA IDENTIFICAR SI LA ASIGNACION QUE SE LE HACE A LA VARIABLE
    #CORRESPONDE A TIPO DE VARIABLE DECLARADA (INT, DOUBLE)
    lista = t
    global list_valor
    global tipo_salida
    # global aviso
    list_valor = lista[variable] # guardame lo que en el lista_valor lo que esta contenido en diccionario con variable
    if list_valor == type(typo).__name__ :
        tipo_salida.append('Ejecucion Exitosa')
    else :
        tipo_salida.append('Error “Asignación de tipo {} incorrecta”'.format(list_valor))
    
    # if lista.keys(0) != lista.values(1) :
    #     aviso.append('Las variables {} no coiciden, puede que no se haya declarado'.format(lista.keys(0)))
        
    
def p_declaracion_asignar(t):
    'declaracion : INT expresion EQUALS expresion SEMI'
    nombres[t[1]] = t[3]
    global type_variables
    type_variables[t[2]] = [t[1], t[4]] # agregar la variable como clave con su tipo y valor de asignacion como valor
    global variable
    variable = t[2] 
    SemanticaINT(type_variables)
    # tipo_dato.append(type(t[4]))
    
def p_declaracion_int(t):
    'declaracion :   INT expresion SEMI'
    nombres[t[1]] = t[3]
    global type_variables
    global variable
    type_variables[t[2]] = t[1]#guardo la viariable con su tipo
    variable = t[2]


def p_declaracion_asignar2(t):
    'declaracion : DOUBLE expresion EQUALS expresion SEMI'
    nombres[t[1]] = t[3]
    global type_variables
    type_variables[t[2]] = [t[1], t[4]]# agregar la variable como clave con su tipo y valor de asignacion como valor
    global variable
    variable = t[2]
    SemanticaF(type_variables)
    
def p_declaracion_double(t):
    'declaracion :  DOUBLE expresion SEMI'
    nombres[t[1]] = t[3]
    global type_variables
    global variable
    type_variables[t[2]] = t[1]#guardo la viariable con su tipo
    variable = t[2]

    
def p_declaracion_asignar3(t):
    'declaracion : FLOAT expresion EQUALS expresion SEMI'
    nombres[t[1]] = t[3]
    global type_variables
    type_variables[t[2]] = [t[1], t[4]]# agregar la variable como clave con su tipo y valor de asignacion como valor
    global variable
    variable = t[2]
    SemanticaFloat(type_variables)

def p_declaracion_float(t):
    'declaracion :  FLOAT expresion SEMI'
    nombres[t[1]] = t[3]
    global type_variables
    global variable
    type_variables[t[2]] = t[1]#guardo la viariable con su tipo
    variable = t[2]

def p_declaracion_asignar5(t):
    'declaracion : BOOL expresion EQUALS expresion SEMI'
    nombres[t[1]] = t[3]
    global type_variables
    type_variables[t[2]] = [t[1], t[4]]# agregar la variable como clave con su tipo y valor de asignacion como valor
    global variable
    variable = t[2]
    SemanticaBool(type_variables)

def p_declaracion_bool(t):
    'declaracion :  BOOL expresion SEMI'
    nombres[t[1]] = t[3]
    global type_variables
    global variable
    type_variables[t[2]] = t[1]#guardo la viariable con su tipo
    variable = t[2]

def p_declaracion_asignar4(t):
    'declaracion : STRING expresion EQUALS expresion SEMI'
    nombres[t[1]] = t[3]
    global type_variables
    type_variables[t[2]] = [t[1], t[4]]# agregar la variable como clave con su tipo y valor de asignacion como valor
    global variable
    variable = t[2]
    SemanticaString(type_variables)

def p_declaracion_string(t):
    'declaracion :  STRING expresion SEMI'
    nombres[t[1]] = t[3]
    global type_variables
    global variable
    type_variables[t[2]] = t[1]#guardo la viariable con su tipo
    variable = t[2]


def p_declaracion_asignarV(t):
    'declaracion :  expresion EQUALS expresion SEMI'
    nombres[t[1]] = t[3]
    global typo
    type_variables[t[3]] = t[1]#guardo la viariable con su tipo
    typo = t[3]
    
    #dependiendo de tipo de valor de asignacion es la funcion que se ejecuta
    if  type(typo).__name__ == 'int' :
        Semantica_linedw(type_variables)
    elif type_variables[variable] == 'double':
        SemanticaF_linedw(type_variables)
    elif type(typo).__name__ == 'float' :
        SemanticaFloat_linedw(type_variables)
    elif type(typo).__name__ == 'bool' :
        SemanticaBool_linedw(type_variables)
    elif type(typo).__name__ == 'str' :
        SemanticaString_linedw(type_variables)

#DEFINICION DE ESPRE
def p_declaracion_expr(t):
    'declaracion : expresion SEMI'
    t[0] = t[1]

    
def p_expresion_operaciones(t):
    '''
    expresion  :   expresion SUMA expresion 
                |   expresion RESTA expresion 
                |   expresion MULTI expresion
                |   expresion DIVISION expresion 

    '''
    #como debe de expresarse las operaciones cuando se este compilando 
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]

def p_expresion_minus(t):
    'expresion : RESTA expresion %prec RESTA'
    t[0] = -t[2]

#como se definen las expresiones entre parentesis y corchetes con expreciones


# sintactico de expresiones logicas
def p_expresion_logicas(t):
    '''
    expresion   :  expresion MENORQ expresion 
                |  expresion MAYORQ expresion 
                |  expresion MENORIGUAL expresion 
                |   expresion MAYORIGUAL expresion 

    ''' #cada una de las variantes en las expresiones logicas
    if t[2] == "<":
        t[0] = t[1] < t[3]
    elif t[2] == ">":
        t[0] = t[1] > t[3]
    elif t[2] == "<=":
        t[0] = t[1] <= t[3]
    elif t[2] == ">=":
        t[0] = t[1] >= t[3]
        
def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = t[1]

def p_expresion_numero(t):
    'expresion : NUMERO'
    t[0] = t[1]

def p_expresion_id(t):
    'expresion : ID'
    t[0] = t[1]
    
def p_expresion_string(t):
    'expresion : TXT'
    t[0] = t[1]


res = False
def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {:4} en el valor {:4}".format(
            str(t.type), str(t.value))
        global res
        res = True
    else:
        resultado = "Error sintactico {}".format(t)
    resultado_gramatica.append(resultado)


# instanciamos el analizador sistactico
parser = yacc.yacc()
    

#funcion que caputa de manera presisa los erroes
def prueba_sintactica(data):
    global resultado_gramatica

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else:
            print("")
    return resultado_gramatica

#importamos el archivo a analizar
path = "prueba.java"

#verificacion y capura de error al buscar el archivo
try:
    archivo = open(path, 'r')
except:
    print("el archivo no se encontro")
    quit()

text = ""
for linea in archivo:
    text += linea

#impresion de los resultados de manera ordena.
prueba_sintactica(text)
print()
print('----------------------------Analizador Sintactico ----------------------')
print()
print('\n'.join(list(map(''.join, resultado_gramatica))))
if(res) : print("Alguna sintaxis no es valida\n")
else : print("Ejecucion exitosa\n")

print('\n\n----------------------------Analizador Semantico ----------------------')

#IMPRESION DEL RESULTADO DE LA EJECUCION
print(tipo_salida[0])

print("\n")


list_A = ['ELIEL DAVID NOVELO CAHUM', 
          'REYES GUADALUPE KAUIL ESPADAS',
          'MARCO ANTONIO BAEZA CAHUM']

print("\t\t\t\t\tRealizado por \n", list_A, "\n")


