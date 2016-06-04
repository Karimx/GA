(* ::Package:: *)

Needs["BarCharts`"];Needs["Histograms`"];Needs["PieCharts`"]
Needs["ErrorBarPlots`"]
<<Combinatorica`


createChromosome[width_:1,opts___]:=Module[{paramRange,stepRange},
	paramRange=ParameterRange/.{opts}/.Options[createChromosome];
	stepRange=StepSizeRange/.{opts}/.Options[createChromosome];
	chromo[q[undef],p@@RandomReal[paramRange,width],s@@RandomReal[stepRange,width]]
];

Options[createChromosome]={ParameterRange->{-10,10},StepSizeRange->{0,1}};

createChromosomes[howMany_Integer:1,opts___]:=pop@@Table[createChromosome[ChromosomeWidth/.{opts}/.Options[createChromosomes],opts],{howMany}];

Options[createChromosomes]={ChromosomeWidth->1};



(esSelection[population_pop,howMany_Integer:1,opts___]:=Module[{},\
Switch[esSelectionMode/.{opts}/.Options[esSelection],
BEST,Take[Reverse[Sort[population]],howMany],
RANDOM,pop@@Table[population[[RandomInteger[{1,Length[population]}]]],\
{howMany}]]]) (Options[esSelection]={esSelectionMode->BEST};) \
(metaesSelection[population_List,howMany_Integer:1,opts___]:=Module[{\
qVals,metaQuals,indices,evalFct},evalFct=EvaluationFunction/.{opts}\
/.Options[metaesSelection];Switch[esSelectionMode/.{opts}/.Options[\
metaesSelection],
BEST,qVals=(Cases[#1,_q,\[Infinity]]&)/@population/.{q[x_]:>x};\
metaQuals=Reverse[Sort[MapIndexed[{N[evalFct[#1]],First[#2]}&,qVals]]]\
;indices=Take[Last/@metaQuals,howMany];(population[[#1]]&)/@indices,
RANDOM,Table[population[[RandomInteger[{1,Length[population]}]]],{\
howMany}]]]) \
(Options[metaesSelection]={EvaluationFunction->Mean,esSelectionMode->\
RANDOM};)



Evaluation[chromo[qualities_q,params_p,strategies_s],opts___]:=Module[\
{g},g=EvaluationFunction/.{opts}/.Options[Evaluation];
chromo[q[N[g[params]]],params,strategies]]
Options[Evaluation]={EvaluationFunction:>(Plus@@#1&)};


gauss[m_,s_]:=Random[NormalDistribution[m,s]]
chi[]:=RandomReal[{0,1}]
INTERMEDIATE=N[Mean[#1]]&;
DISCRETE=randomSelect[#1]&;
randomSelect[s_List]:=s[[RandomInteger[{1,Length[s]}]]]
randomSelectMultiple[s_List,n_Integer:1,opts___]:=Module[{m,i},m=(s[[#\
1]]&)/@(i=Take[RandomPermutation[Length[s]],n]);If[ReturnIndices/.{\
opts}/.Options[randomSelectMultiple],{m,i},m]]
Options[randomSelectMultiple]={ReturnIndices->False};



ClearAll[Mutation];

Mutation[chromo[_q,params_p,strategies_s],opts___]:=Module[{adapt},\
scale=StepSizeScale/.{opts}/.Options[Mutation];
adapt=StepSizeAdaptation/.{opts}/.Options[Mutation];
pRange=ParameterRange/.{opts}/.Options[Mutation];
sRange=StepSizeRange/.{opts}/.Options[Mutation];
chromo[q[undef],p@@MapThread[#1+gauss[0,#2]&,{List@@params,List@@\
strategies}]/.borderCheck[pRange],s@@(adapt/.{alpha->scale})/@\
strategies/.borderCheck[sRange]]]

Options[Mutation]={StepSizeScale->1.3,StepSizeAdaptation->(If[chi[]<0.\
5,N[#1  alpha],N[#1/alpha]]&),ParameterRange->{-10,10},StepSizeRange->\
{0,1}};

borderCheck[{min_,max_}]:={x_/;x<min:>min,x_/;x>max:>max}




Recombination[chromoPop_pop,opts___]:=Module[{objects,newObjects,\
strategies,newStrategies,rpo,rps,rfo,rfs,r,io,is},rpo=\
RecombinationPartners[OBJECTS]/.{opts}/.Options[Recombination];
rps=RecombinationPartners[STRATEGIES]/.{opts}/.Options[Recombination];\

rfo=RecombinationFunction[OBJECTS]/.{opts}/.Options[Recombination];
rfs=RecombinationFunction[STRATEGIES]/.{opts}/.Options[Recombination];\

objects=(List@@#1[[2]]&)/@List@@chromoPop;
strategies=(List@@#1[[3]]&)/@List@@chromoPop;
Switch[RecombinationRange[OBJECTS]/.{opts}/.Options[Recombination],\
LOCAL,newObjects=({r,io}=randomSelectMultiple[objects,rpo,\
ReturnIndices->True];
Recombine[r,Sequence@@Join[{opts},{RecombinationFunction->rfo}]]);,\
GLOBAL,newObjects=({r,io}=Transpose[(randomSelectMultiple[#1,rpo,\
ReturnIndices->True]&)/@Transpose[objects]];
Recombine[Transpose[r],Sequence@@Join[{opts},{RecombinationFunction->\
rfo}]]);];
Switch[RecombinationRange[STRATEGIES]/.{opts}/.Options[Recombination],\
LOCAL,If[(RecombineTogether/.{opts}/.Options[Recombination])&&(\
RecombinationRange[OBJECTS]/.{opts}/.Options[Recombination])===LOCAL,\
newStrategies=Recombine[strategies[[is=io]],Sequence@@Join[{opts},{\
RecombinationFunction->rfs}]],newStrategies=({r,is}=\
randomSelectMultiple[strategies,rps,ReturnIndices->True];
Recombine[r,Sequence@@Join[{opts},{RecombinationFunction->rfs}]]);],\
GLOBAL,If[(RecombineTogether/.{opts}/.Options[Recombination])&&(\
RecombinationRange[OBJECTS]/.{opts}/.Options[Recombination])===GLOBAL,\
newStrategies=Recombine[MapThread[Part,{Transpose[strategies],is=io}],\
Sequence@@Join[{opts},{RecombinationFunction->rfs}]],newStrategies=({\
r,is}=Transpose[(randomSelectMultiple[#1,rps,ReturnIndices->True]&)/@\
Transpose[strategies]];
Recombine[Transpose[r],Sequence@@Join[{opts},{RecombinationFunction->\
rfs}]])];];{chromo[q[undef],p@@newObjects,s@@newStrategies],Sort[io],\
Sort[is]}]

Options[Recombination]={RecombinationRange[OBJECTS]->LOCAL,\
RecombinationRange[STRATEGIES]->LOCAL,RecombinationPartners[OBJECTS]->\
2,RecombinationPartners[STRATEGIES]->2,RecombinationFunction[OBJECTS]->INTERMEDIATE,RecombinationFunction[STRATEGIES]->DISCRETE,\
RecombineTogether->True};



Recombine[params_List,opts___]:=(RecombinationFunction/.{opts}/.\
Options[Recombine])/@Transpose[params]

Options[Recombine]:={RecombinationFunction->(#1&)};





EvolutionStrategy[ES[m_?IntegerQ,r_?IntegerQ,s_?AtomQ,l_?IntegerQ,g_?\
IntegerQ,opts___] \
(i_:1)]:=Module[{initialParents,evalFct,parents,children,selPool},\
(*Print["ES evolution ..."];*)
If[(initialParents=InitialPopulation/.{opts}/.Options[\
EvolutionStrategy])==={},initialParents=createChromosomes[m,\
ChromosomeWidth->(ChromosomeWidth/.{opts}/.Options[EvolutionStrategy])\
,opts]];evalFct=EvaluationFunction/.{opts}/.Options[EvolutionStrategy]\
;
initialParents=(Evaluation[#1,EvaluationFunction:>evalFct]&)/@\
initialParents;
Table[NestList[(parents=#1;
children=(Evaluation[#1,EvaluationFunction:>evalFct]&)/@(Mutation[#1,\
opts]&)/@(First[Recombination[#1,RecombinationPartners[OBJECTS]->r,\
RecombinationPartners[STRATEGIES]->r,opts]]&)/@Partition[esSelection[\
parents,r l,esSelectionMode->RANDOM],r];
selPool=Switch[s,PLUS,Join[parents,children],COMMA,children];\
esSelection[selPool,m,esSelectionMode->BEST])&,initialParents,g],{i}]]\




EvolutionStrategy[ES[m1_?IntegerQ,r1_?IntegerQ,s1_?AtomQ,l1_ \
ES[m0_?IntegerQ,r0_?IntegerQ,s0_?AtomQ,l0_?IntegerQ,g0_?IntegerQ,\
opts0___],g1_?IntegerQ,opts1___] \
(i_:1)]:=Module[{initialMetaParents},Print["Meta-Evolution ..."];
initialMetaParents=Table[createChromosomes[m0,ChromosomeWidth->(\
ChromosomeWidth/.{opts0}/.Options[EvolutionStrategy]),opts0],{m1}];
initialMetaParents=((Evaluation[#1,opts0]&)/@#1&)/@initialMetaParents;\

NestList[(metaParents=#1;
metaChildren=(Last[First[EvolutionStrategy[ES[m0,r0,s0,l0,g0,\
InitialPopulation->#1,opts0]]]]&)/@(ms=metaesSelection[metaParents,l1,\
esSelectionMode->RANDOM,opts1];ms);selPool=Switch[s1,PLUS,Join[\
metaParents,metaChildren],COMMA,metaChildren];
metaesSelection[selPool,m1,esSelectionMode->BEST,opts1])&,\
initialMetaParents,g1]]

Options[EvolutionStrategy]={InitialPopulation->{}};
