from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape3.Solution import Solution
import random

class UneSolution(Solution): 
    tg: GrapheDeLieux

    def __init__(self, tg: GrapheDeLieux, cycle=None):
        self.tg = tg

        if cycle==None:
            self.cycle=[i for i in range(self.tg.getNbSommets())]
            random.shuffle(self.cycle)
            self.cycle.append(self.cycle[0])
        else:
            self.cycle=cycle

   
    def lesVoisins(self):
       
        voisin=[]
        list_i=[]
        for i in range(self.tg.getNbSommets()-1):
            index=random.randint(1,self.tg.getNbSommets()-1)
            index2=random.randint(index+1,self.tg.getNbSommets())
            while index in list_i:
                index=random.randint(1,self.tg.getNbSommets()-1)
                index2=random.randint(index+1,self.tg.getNbSommets())
            list_i.append(index)
            nouveau_cycle=self.cycle[0:index] + self.cycle[index2-1:index-1:-1] + self.cycle[index2:]
            voisin.append(UneSolution(self.tg,nouveau_cycle))
        return voisin

    def unVoisin(self):
        return [self.lesVoisins()[0]]

    def eval(self):
        val=0
        for i in range(len(self.cycle)-1):
            etat1=self.cycle[i]
            etat2=self.cycle[i+1]
            val+=GrapheDeLieux.dist(etat1,etat2,self.tg)
        return val

    def nelleSolution(self):
        cycle=[i for i in range(self.tg.getNbSommets())]
        random.shuffle(cycle)
        new_cycle=cycle+[cycle[0]]
        return UneSolution(self.tg,new_cycle)

    def displayPath(self):
        print("Sol courante : ",self.eval(),"\n",self.cycle,"\n")

   
    def __hash__(self):
        return hash(self.cycle)

    def __eq__(self, o):
        return self.eval == o


    def __str__(self):
       
        path_str = "Chemin optimal : " + " ".join(str(sommet) for sommet in self.cycle)
        return f"{path_str}\nValeur de la meilleure solution  {self.eval()}"
