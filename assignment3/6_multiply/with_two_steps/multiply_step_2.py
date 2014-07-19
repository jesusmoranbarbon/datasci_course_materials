import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def F_Map(record):
    indice_i = record[0][0]
    indice_l = record[0][1]
    valor=record[1]
    lista_i_l=[]
    lista_i_l.append(indice_l)
    lista_i_l.append(valor)
    mr.emit_intermediate(indice_i,lista_i_l)

# Part 3
def F_Reduce(clave, lista_de_valores):
    lista_de_sumas=[]
    maximo=0
    for v in lista_de_valores:
	if v[0]>maximo:
	  maximo=v[0]
    
    indice=0
    while indice<=maximo:
      lista_de_sumas.append(0)
      indice=indice+1
    
    for elemento in lista_de_valores:
      lista_de_sumas[elemento[0]]=lista_de_sumas[elemento[0]]+elemento[1]
    
    l=0
    for suma in lista_de_sumas:
      lista_final=[]
      lista_final.append(clave)
      lista_final.append(l)
      l=l+1
      lista_final.append(suma)
      mr.emit((lista_final))




# Part 4
# Desde la consola se le tiene que pasar un json como argumento
entrada = open(sys.argv[1])
mr.execute(entrada, F_Map, F_Reduce)
