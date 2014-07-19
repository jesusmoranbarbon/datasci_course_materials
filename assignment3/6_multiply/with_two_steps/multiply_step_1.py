import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def F_Map(record):
    nombre_matriz = record[0]
    indice_i = record[1]
    indice_j=record[2]
    valor_ij=record[3]
    lista_matriz=[]
    lista_matriz.append(nombre_matriz)
    if nombre_matriz=='a':
      lista_matriz.append(indice_i)
      lista_matriz.append(valor_ij)
      mr.emit_intermediate(indice_j,lista_matriz)
    else:   
      lista_matriz.append(indice_j)
      lista_matriz.append(valor_ij)
      mr.emit_intermediate(indice_i,lista_matriz)

# Part 3
def F_Reduce(clave, lista_de_valores):
    lista_con_A=[]
    lista_con_B=[]
    for v in lista_de_valores:
      if v[0]=='a':
	lista_con_A.append(v)
      else:
	lista_con_B.append(v)
     
    for elementoA in lista_con_A:
       for elementoB in lista_con_B:
	 lista_i_l=[]
	 lista_i_l.append(elementoA[1])
	 lista_i_l.append(elementoB[1])
	 mr.emit((lista_i_l,elementoA[2]*elementoB[2]))



# Part 4
# Desde la consola se le tiene que pasar un json como argumento
entrada = open(sys.argv[1])
mr.execute(entrada, F_Map, F_Reduce)
