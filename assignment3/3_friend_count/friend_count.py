import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    nombre = record[0]
    nombre_amigo = record[1]
    mr.emit_intermediate(nombre, 1)

# Part 3
def reducer(clave, lista_de_valores):
    total = 0
    for v in lista_de_valores:
      total += v
    mr.emit((clave, total))

# Part 4
# Desde la consola se le tiene que pasar un json como argumento
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
