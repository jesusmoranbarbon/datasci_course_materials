import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    clave=record[1]
    mr.emit_intermediate(clave, record)

# Part 3
def reducer(clave, lista_de_valores):
    #Obtenemos el nombre de las 2 tablas
    continua= True
    tipo1=lista_de_valores[0][0]
    tipo2=""
    i=1
    while continua:
	if lista_de_valores[i][0]!=tipo1:
	  tipo2=lista_de_valores[i][0]
	  continua=False
	i=i+1
    
    #Creamos 2 listas con los valores de cada tabla
    lista_tipo1=[]
    lista_tipo2=[]
    for tabla in lista_de_valores:
      if tabla[0]==tipo1:
	lista_tipo1.append(tabla)
      elif tabla [0]==tipo2:
	lista_tipo2.append(tabla)
    
    
    #Creamos la union
    combinaciontuplas=[]
    for tuplatipo1 in lista_tipo1:
      for tuplatipo2 in lista_tipo2:
	combinaciontuplas=tuplatipo1+tuplatipo2
	mr.emit((combinaciontuplas))
    
# Part 4
# Desde la consola se le tiene que pasar un json como argumento
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)