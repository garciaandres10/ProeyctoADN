ADN

7: def funcion_base(caracter_base):(TODOS)

	pass:

1: def obtener_complemento (base):
    complemento = ""
    if(base == "A")
        complemento = "T"

    elif (base=="G"):
        complemento = "C"

    elif (base== "T"):
        complemento ="A"

    else:
        complemento = "G"

    return complemento

2: def generar_complemento (cadena):(EDWARD)

	pass:

3: def validar_base (letra)
    bases = ["A", "T", "C", "G"]
    es_base=False
    for i in bases:
        if (letra==i):
            es_base = True

    return es_base

4: def calcular_porcentaje(cadena1,cadena2): (ANDRES)

	pass:

5:  def validar_correspondencia_cadenas(cadena1,cadena2):(LUISA)

	pass:

6: validar_todas_bases(cadena):(ANDRES)

	pass:


bases = ["A","T","C","G"]

#Funcion que genera el complemento de una base
def complemento_base(base):
   """
   (str)->str
   #casos de prueba
   >>> complemento_base("A")
   'T'
   >>> complemento_base("C")
   'G'
   >>> complemento_base("T")
   'A'

   :param base: recibe una base para definir su complemento
   :return: retorna el complemento de la base
   """
   #desarrollo de la funcion
   complento = ""
   if (base == "A"):
     complento = complento + "T"
   elif (base == "T"):
     complento = complento + "A"
   elif (base == "C"):
     complento = complento + "G"
   else:
     complento = complento + "C"
   return complento

# funcion para generar una cadena complementaria
def retorna_complemento(cadena):
"""
(str)->str
#casos de prueba
>>> retorna_complemento("AT")
'TA'
>>> retorna_complemento("TA")
'AT'
>>> retorna_complemento("CG")
'GC'

:param cadena: recibe una cadena de adn
:return: retorna el complemento de adn
"""
#desarrollo de la fincion
resultado = ""
for i in cadena:
   resultado = resultado + complemento_base(i)
return resultado

#funcion para verificar si hay una base
def es_base(letra):
  """
  (str)->boolean

  # casos de prueba

  >>> es_base("A")
  True
  >>> es_base("O")
  False
  >>> es_base("G")
  True

  :param letra: CORRESPONDE A UNA LETRA CUALQUIERA PARA SABER SI ES BASE DE LA CADENA ADN
  :return: RETORNA UN BOOLEANO SEA  TRUE SI LA LATRA CORRESPONDE A UNA SECUENCIA DE ADN Y FALSE SI NO
  """

  # desarrollo funciones
  coincidencia = 0
  resultado = False
  for i in bases:
      if(letra==i):
          coincidencia=coincidencia+1
  if (coincidencia>0):
      resultado = True
  return resultado

# funcion para validar una base
def cadena_valida(cadena):
  """
  (str)-> boolean
  # casos de prueba
  >>> cadena_valida("ACT")
  True

  >>> cadena_valida("XYZ")
  False
  >>> cadena_valida("TCG")
  True

  :param cadena: RECIBE UNA CADENA PARA VERIFICAR SI ES VALIDA
  :return:RETORNA TRUE SI ES VALIDA LA CADENA O FLASE SI ES INCORRECTA
  """
  # desarrollo funcion
  errores = 0
  resultado = False
  for i in cadena:
      validar = es_base(i)
      if (validar==False):
          errores=errores+1
  if(errores==0):
      resultado=True
  return resultado

#funcion que calcula el porcentaje correspondiente de una cadena y otra
def porcentaje_correspondencia(cadenaBase,cadenaComplem):
   """
   (str,str)-> float
   #casos de prueba
   >>> porcentaje_correspondencia("AT","TA")
   TA
   100.0
   >>> porcentaje_correspondencia("CG","GT")
   GT
   50.0
   >>> porcentaje_correspondencia("AAA","GCG")
   GCG
   0.0


   :param cadenaBase: primera cadena de adn a comparar para su porcentaje
   :param cadenaComplem: segunda cadena recibida para comparar su porcentaje
   :return: retorna el porcentaje total en termino de reales
   """
   # desarrollo de funcion
   complementoReal = retorna_complemento(cadenaBase)
   print(complementoReal)
   total = len(cadenaComplem)
   coincidencias = 0
   cont = 0
   while (cont < total):
     if (cadenaComplem[cont]==complementoReal[cont]):
        coincidencias = coincidencias + 1
        cont = cont + 1
        porcentaje = (coincidencias*100)/total
        porcentaje = round(porcentaje,2)
   return porcentaje

# funcion que valida la correspondencia entre dos cadenas
def correspondencia_Cadenas(cadenaBase,cadenaComplem):
   """
   (str,str)-> boolean
   #casos de prueba
   >>> correspondencia_Cadenas("AT","TA")
   True
   >>> correspondencia_Cadenas("TA","TG")
   False
   >>> correspondencia_Cadenas("GC","CG")
   True

   :param cadenaBase: cadena base DE ADN A COMPARAR
   :param cadenaComplem: CADENA SECUNDARIA DE ADN A COMPARAR
   :return: TRUE SI LA CADENA ES CORRESPONDIENTE Y FALSE SI NO LO ES
   """
   # desarrollo funcion
   complementoReal = retorna_complemento(cadenaBase)
   correspondencia = False
   if (complementoReal == cadenaComplem):
       correspondencia = True
   return correspondencia

#
def correspondencia_base(base,complem):
   """
   (str,str)-> str
  
   >>> correspondencia_base("A","C")
   >>> correspondencia_base()
   >>>correspondencia_base()
   :param base:
   :param complem:
   :return: retorna valor verdadero
   """
#desarrollo funcion   
   complem_real = complemento_base(base)
   correspondencia = False
   if (complem == complem_real):
     correspondencia = True
     return correspondencia




