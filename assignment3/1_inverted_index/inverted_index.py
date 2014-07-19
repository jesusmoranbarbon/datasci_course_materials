import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # clave: identificador de documento
    # valor: Contenido de documento
    clave = record[0]
    valor = record[1]
    palabras = valor.split()
    for w in palabras:
      mr.emit_intermediate(w, clave)

# Part 3
def reducer(clave, lista_de_valores):
    # clave: palabra
    # valor: lista de nombre de documentos en los que aparece
    documento_anterior=""
    lista=[]
    lista_de_valores.sort()
    for documento_actual in lista_de_valores:
      if documento_actual!=documento_anterior:
	lista.append(documento_actual)
	documento_anterior=documento_actual
    mr.emit((clave, lista))
    
# Part 4
# Desde la consola se le tiene que pasar un json como argumento
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
