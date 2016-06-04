from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Consts
import math

# configuracion
generaciones = 100
poblacionInicial = 100


def Acoordenadas(gen):
    if gen % 8 == 0:
        x = 8
    else:
        x = round(gen % 8 - 0.1)
    if gen % 8 == 0:
        y = gen / 8
    else:
        y = gen / 8 + 1
    return [x, y]


def distancia(a, b):
    return math.sqrt(math.pow(b[0] - a[0], 2) + math.pow(b[1] - a[1], 2))


ruta1 = []
ruta2 = []
ruta3 = []


def eval_func(cromosoma):
    ocupados = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 7], [2, 8]]
    score = 0
    actual = 0
    for c in range(1, len(cromosoma) ):
        coordenada = Acoordenadas(cromosoma[c - 1])

        for i in ocupados:
            if coordenada[0] == i[0] and coordenada[1] == i[1]:
                score += 100
        score += distancia(coordenada[cromosoma[c]], Acoordenadas(cromosoma[c]))

    return score


genome = G1DList.G1DList(14)

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
ga.evolve(freq_stats=50)

# Best individual
