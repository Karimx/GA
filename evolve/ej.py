from pyevolve import GSimpleGA
from pyevolve import G1DList
from pyevolve import Selectors
from pyevolve import Initializators, Mutators
from pyevolve import DBAdapters

# Find negative values
def eval_func(chromosome):
   ataques = 0
   ngenes = len(chromosome)
   # score = len(filter(lambda x: x==0, chromosome.genomeList))
   for gen in chromosome:
        for c in range(0, ngenes):
            if gen + c == chromosome[c] + c:
                ataques += 1
            if chromosome[gen] - c == chromosome[c] - c:
                ataques += 1

# Genome instance
genome = G1DList.G1DList(20)
genome.setParams(rangemin=-6.0, rangemax=6.0)

# Change the initializator to Real values
genome.initializator.set(Initializators.G1DListInitializatorReal)
l=Initializators.G1DListInitializatorReal

print genome

#print l