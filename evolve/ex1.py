from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Selectors
from pyevolve import Consts
from pyevolve import Statistics
from pyevolve import DBAdapters
import pyevolve

# metodos por defecto
# One piont crosover
# Swap mutator
#
#

# This function is the evaluation function, we want
# to give high score to more zero'ed chromosomes
reinas = 8


def eval_func(chromosome):
    ataques = 0
    ngenes = len(chromosome)
    for gen in range(0, ngenes):
        cont=0
        for c in range(gen, ngenes):

            if chromosome[gen]  == chromosome[c] :
                ataques += 2
            if chromosome[gen] + cont == chromosome[c] :
                ataques += 1
            if chromosome[gen] - cont == chromosome[c] :
                ataques += 1
            cont+=1
    return ataques

# Enable the pyevolve logging system
# pyevolve.logEnable()

# Genome instance, 1D List of 50 elements
genome = G1DList.G1DList(reinas)

# Sets the range max and min of the 1D List
genome.setParams(rangemin=1, rangemax=reinas)

# The evaluator function (evaluation function)
genome.evaluator.set(eval_func)

# Genetic Algorithm Instance
ga = GSimpleGA.GSimpleGA(genome)
ga.minimax = Consts.minimaxType["minimize"]
# Set the Roulette Wheel selector method, the number of generations and
# the termination criteria
ga.selector.set(Selectors.GRouletteWheel)
ga.setGenerations(600)
ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)
ga.selector.set(Selectors.GRouletteWheel)
ga.setPopulationSize(100)
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
print ga.bestIndividual()
