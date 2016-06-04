from pyevolve import GSimpleGA
from pyevolve import G1DList
from pyevolve import Selectors
from pyevolve import Initializators, Mutators
from pyevolve import DBAdapters

# Find negative values
def eval_func(ind):
   score = 0.0
   for x in xrange(0,len(ind)):
      if ind[x] <= 0.0: score += 0.1
   return score

# Genome instance
genome = G1DList.G1DList(20)
genome.setParams(rangemin=-6.0, rangemax=6.0)

# Change the initializator to Real values
genome.initializator.set(Initializators.G1DListInitializatorReal)
l=Initializators.G1DListInitializatorReal
print l;
# Change the mutator to Gaussian Mutator
genome.mutator.set(Mutators.G1DListMutatorRealGaussian)

# The evaluator function (objective function)
genome.evaluator.set(eval_func)

# Genetic Algorithm Instance
ga = GSimpleGA.GSimpleGA(genome)
ga.selector.set(Selectors.GRouletteWheel)
ga.nGenerations = 100

#
sqlite_adapter = DBAdapters.DBSQLite(identify="ex2", resetDB=True)
ga.setDBAdapter(sqlite_adapter)

# Do the evolution
# mostrar cada 5 generaciones
ga.evolve(5)

# Best individual
print ga.bestIndividual()