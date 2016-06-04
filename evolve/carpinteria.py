from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Consts
import math

# Los genes reprecentan a las estaciones y
# Su pocicion reprecenta el numero de la estacion
# posicion 21 reprecenta el espacio de trabajo 2,1
# 8*4
#
# *, 2, 3, 4, 5, 6, 7, 8
# *,10,11,12,13,14, *, *
# *,18,19,20,21,22,23,24
# *,26,27,28,29,30,31,32


# configuracion
generaciones = 100
poblacionInicial = 1000


def Acoordenadas(gen):
    if gen % 8 == 0:
        x = 8
    else:
        x = round(gen % 8 - 0.1)
    if gen % 8 == 0:
        y = gen / 8
    else:
        y = gen / 8 + 1
    return [int(x), int(y)]


def distanciaEuclideana(a, b):
    return math.sqrt(math.pow(b[0] - a[0], 2) + math.pow(b[1] - a[1], 2))


estaciones = []

estaciones.append("Materia Prima") #fija
estaciones.append("Tripay")       #fija
estaciones.append("Estacion 1")
estaciones.append("Estacion 2")
estaciones.append("Estacion 3")
estaciones.append("Eclopeadora")
estaciones.append("Destrazadora")
estaciones.append("Trompo")
estaciones.append("Cepillo")
estaciones.append("Sierra cinta")
estaciones.append("Soporte U 1")
estaciones.append("Soporte U 2")
estaciones.append("Canteadora R")
estaciones.append("Canteadora")
estaciones.append("Almacen Producto") #fija


ruta1 = [estaciones.index("Estacion 1"),
         estaciones.index("Materia Prima"),
         estaciones.index("Canteadora R"),
         estaciones.index("Cepillo"),
         estaciones.index("Soporte U 2"),
         estaciones.index("Canteadora"),
         estaciones.index("Soporte U 1"),
         estaciones.append("Estacion 1"),
         estaciones.append("Tripay"),
         estaciones.append("Estacion 1"),
         estaciones.append("Soporte U 2"),
         estaciones.append("Estacion 1"),
         estaciones.append("Almacen Producto"),
         estaciones.append("Bano")
         ]


fijas=[[estaciones.index("Materia Prima"),1],
       [estaciones.index("Materia Prima"),9],
       [estaciones.index("Tripay"),17],
       [estaciones.index("Bano"),25],
       [estaciones.index("Almacen Producto"),15],
       [estaciones.index("Almacen Producto"),16]

       ]

ruta2 = [estaciones.index("Estacion 2"), estaciones.append("Almacen Producto")]
ruta3 = [estaciones.index("Estacion 3"), estaciones.append("Almacen")]


def eval_func(cromosoma):
    ocupados = [[1, 2], [1, 3], [1, 4], [2, 8]]


    cromosoma[0] = 1
    cromosoma[14] = 15

    score1 = 0
    score2 = 0
    score3 = 0
    ocupados2=[1,9,17,25,15,16]


    for c in range(1, len(cromosoma)):
        ocupados2.append(cromosoma[c-1])


        ocupados=[]
        ocupados.append(fijas)

        #inyectar Fijos
        for i in fijas:
            cromosoma[i[1]]=i[1]

        print("-inyectados-")
        print(cromosoma)

        #coordenada = Acoordenadas(cromosoma[c - 1])
        #for i in ocupados:
        #    if coordenada[0] == i[0] and coordenada[1] == i[1]:
        #        return 10000

        for r1 in range(0, len(ruta1)-1):
            score1 += distanciaEuclideana(Acoordenadas(cromosoma[r1]), Acoordenadas(cromosoma[r1 + 1])) * 2.2


    return score1


genome = G1DList.G1DList(12)

# Sets the range max and min of the 1D List
genome.setParams(rangemin=1, rangemax=32)
# The evaluator function (evaluation function)
genome.evaluator.set(eval_func)
# Genetic Algorithm Instance
ga = GSimpleGA.GSimpleGA(genome)
ga.minimax = Consts.minimaxType["minimize"]
# Set the Roulette Wheel selector method, the number of generations and
ga.selector.set(Selectors.GRouletteWheel)
ga.setGenerations(generaciones)
# ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)

ga.setPopulationSize(poblacionInicial)
# Sets the DB Adapter, the resetDB flag will make the Adapter recreate
# the database and erase all data every run, you should use this flag
# just in the first time, after the pyevolve.db was created, you can
# omit it.
# sqlite_adapter = DBAdapters.DBSQLite(identify="ex1", resetDB=True)
# ga.setDBAdapter(sqlite_adapter)

# Do the evolution, with stats dump
# frequency of 20 generations
#ga.evolve(freq_stats=50)

#res = ga.bestIndividual()
res=[2,3,4,5,6,7,8,10,12,13,14,11,18,19,20]

print(res)
print(eval_func(res))
lista = []
for r in range(0, len(res)):
    print(r, res[r], Acoordenadas(res[r]), estaciones[r - 1])

print("----------")


