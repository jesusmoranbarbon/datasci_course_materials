import MapReduce
import sys

def mi_ordena(x,y):
  if x[1]>x[2]:
    return -1
  elif x[1]<x[2]:
    return 1
  else:
    return 0

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    nombre_matriz = record[0]
    indice_i = record[1]
    indice_j=record[2]
    valor_ij=record[3]
    lista_matriz=[]
    lista_matriz.append(nombre_matriz)
    if nombre_matriz=='a':
      lista_matriz.append(indice_j)
      lista_matriz.append(valor_ij)
      for indice in range (5):
	conjunto=(indice_i,indice)
	mr.emit_intermediate(conjunto,lista_matriz)
    else:   
      lista_matriz.append(indice_i)
      lista_matriz.append(valor_ij)
      for indice in range (5):
	conjunto=(indice,indice_j)
	mr.emit_intermediate(conjunto,lista_matriz)

# Part 3
def reducer(clave, lista_de_valores):
    lista_a=[]
    lista_b=[]
    for recorre in lista_de_valores:
      if recorre[0]=='a':
	lista_a.append(recorre)
      elif recorre[0]=='b':
	lista_b.append(recorre)
	
    total=0
    if len(lista_a)>=len(lista_b):
      for recorre_a in lista_a:
	elemento_j= recorre_a[1]
	for recorre_b in lista_b:
	  if recorre_b[1]==elemento_j:
	    total=total+recorre_b[2]*recorre_a[2]
	    
    elif len(lista_a)<len(lista_b):
      for recorre_b in lista_b:
	elemento_k=recorre_b[1]
	for recorre_a in lista_a:
	  if recorre_a[1]==elemento_k:
	    total=total+recorre_a[2]*recorre_b[2]
    
    if total >0:
      lista_emision=[]
      lista_emision.append(clave[0])
      lista_emision.append(clave[1])
      lista_emision.append(total)
      #mr.emit((lista_emision))
      mr.emit((clave[0],clave[1],total))



# Part 4
# Desde la consola se le tiene que pasar un json como argumento
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
