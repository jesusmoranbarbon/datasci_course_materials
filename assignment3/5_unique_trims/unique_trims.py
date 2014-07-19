import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    clave = record[0]
    nucleo = record[1]
    nucleoMenos10=""
    indice=0
    while indice < len(nucleo)-10:
      letra = nucleo[indice]
      nucleoMenos10=nucleoMenos10+letra
      indice += 1
    mr.emit_intermediate(nucleoMenos10,nucleoMenos10)

# Part 3
def reducer(clave, lista_de_valores):
   mr.emit((lista_de_valores[0]))


# Part 4
# Desde la consola se le tiene que pasar un json como argumento
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
