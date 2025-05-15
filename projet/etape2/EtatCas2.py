"""
module pour l'état de l'etape 2 dans le cas 2
"""
from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape2.Etat import Etat


class EtatCas2(Etat):
    """
    Classe pour définir un état pour le cas 2 de la tâche 2 (hérite de Etat)
    """

    tg: GrapheDeLieux
    courant: int
    a_visiter: list

    def __init__(self, tg: GrapheDeLieux, courant=0, a_visiter=None):
        """
        Constructeur d'un état pour le cas 2.

        :param tg: graphe représentant le monde
        :param courant: lieu actuel
        :param a_visiter: liste des lieux à visiter
        """
        self.tg = tg
        self.courant = courant
        self.a_visiter = a_visiter if a_visiter is not None else list(range(tg.getNbSommets()))
        if courant in self.a_visiter:
            self.a_visiter.remove(courant)

    def estSolution(self):
        """
        Méthode détectant si l'état est une solution.
        L'état est une solution si tous les lieux ont été visités et si on est revenu au point de départ.

        :return: True si c'est une solution, False sinon
        """
        return not self.a_visiter and self.courant == 0

    def successeurs(self):
        """
        Méthode permettant de récupérer la liste des états successeurs de l'état courant.

        :return: liste des états successeurs de l'état courant
        """
        successeurs = []
        for voisin in self.tg.getAdjacents(self.courant):
            if voisin in self.a_visiter:  # voisin a visiter
                nouveaux_a_visiter = self.a_visiter.copy()
                nouveaux_a_visiter.remove(voisin)
                successeurs.append(EtatCas2(self.tg, voisin, nouveaux_a_visiter))

            elif not self.a_visiter and voisin == 0:  # depart
                successeurs.append(EtatCas2(self.tg, 0, []))
        return successeurs

    def h(self):
        """
        Méthode permettant de récupérer l'heuristique de l'état courant.
        Heuristique basée sur le nombre de lieux restants multiplié par le poids minimum.

        :return: heuristique de l'état courant
        """
        return len(self.a_visiter) * self.tg.getPoidsMinAir()

    def k(self, e):
        """
        Méthode permettant de récupérer le coût du passage de l'état courant à l'état e.

        :param e: un état
        :return: coût du passage de l'état courant à l'état e
        """
        return self.tg.getCoutArete(self.courant, e.courant)

    def displayPath(self, pere):
        """
        Méthode pour afficher le chemin qui a mené à l'état courant en utilisant la map des pères.

        :param pere: map donnant pour chaque état, son père
        """
        chemin = []
        etat = self
        longueur_totale = 0

        if etat not in pere:
            print("Erreur : état pas dans père")
            return

        while etat in pere and pere[etat] is not None:
            chemin.append(etat.courant)

            parent = pere[etat]
            cout_arete = self.tg.getCoutArete(etat.courant, parent.courant)
            longueur_totale += cout_arete

            etat = parent

        if etat is not None:
            chemin.append(etat.courant)

        chemin.reverse()

        print(f"Chemin trouvé : {' , '.join(map(str, chemin))}")
        print(f"Longueur totale: {longueur_totale}")

    def __hash__(self):
        """
        Méthode permettant de récupérer le code de hachage de l'état courant
        pour une utilisation dans des tables de hachage.

        :return: code de hachage
        """
        return hash((self.courant, tuple(self.a_visiter)))

    def __eq__(self, o):
        """
        Méthode de comparaison de l'état courant avec l'objet o.

        :param o: l'objet avec lequel on compare
        :return: True si l'état courant et o sont égaux, False sinon
        """
        return isinstance(o, EtatCas2) and self.courant == o.courant and self.a_visiter == o.a_visiter

    def __str__(self):
        """
        Méthode mettant l'état courant sous la forme d'une chaîne de caractères en prévision d'un futur affichage.

        :return: représentation de l'état courant sous la forme d'une chaîne de caractères
        """
        return f"EtatCas2(position={self.courant}, a_visiter={self.a_visiter})"