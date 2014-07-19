import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    nombre = record[0]
    nombre_amigo = record[1]
    lista_clave=[]
    lista_clave.append(nombre)
    lista_clave.append(nombre_amigo)
    mr.emit_intermediate(nombre,lista_clave)
    mr.emit_intermediate(nombre_amigo,lista_clave)

# Part 3
def reducer(clave, lista_de_valores):
    lista_de_los_que_soy_amigo=[]
    lista_de_amigos_mios=[]
    for valor in lista_de_valores:
      #Caso: soy amigo de
      if valor[0]==clave:
	if not valor[1] in lista_de_amigos_mios:
	  lista_de_amigos_mios.append(valor[1])
	
      #Caso me tiene como amigo
      elif valor[1]==clave:
	if not valor[0] in lista_de_los_que_soy_amigo:
	  lista_de_los_que_soy_amigo.append(valor[0])

    
    for mi_amigo in lista_de_amigos_mios:
      no_es_simetrico=True
      amigo_asimetrico=""
      for mi_amigo_asimetrico in lista_de_los_que_soy_amigo:
	if mi_amigo_asimetrico==mi_amigo:
	  no_es_simetrico=False
      if no_es_simetrico==True:
	mr.emit((clave,mi_amigo))
	mr.emit((mi_amigo,clave))


# Part 4
# Desde la consola se le tiene que pasar un json como argumento
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
