"""
Module pour l'état de l'étape 2, Cas 1 : Plus court chemin entre deux sommets
Algorithme utilisé : A* (A-Star)
"""

from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape2.Etat import Etat
import math

class EtatCas1(Etat):
    """
    Classe pour définir un état pour le cas 1 de la tâche 2 (hérite de Etat).
    Le but de cet état est de trouver le chemin le plus court entre deux sommets du graphe en utilisant l'algorithme A*.
    """

    # Attributs
    # //////////////////////////////////////////////
    tg: GrapheDeLieux  # Le graphe représentant le monde
    position: int
    target: int
    # Constructeurs
    # //////////////////////////////////////////////
    def __init__(self, tg: GrapheDeLieux, position: int = None, target: int = None):
        """
        Constructeur d'un état pour le cas 1.
        Si `position` ou `target` est None, choisir le sommet 0 comme position de départ et le dernier sommet comme cible.

        :param tg: Graphe représentant le monde (objet GrapheDeLieux)
        :param position: Sommet courant de R2D2 (défaut : premier sommet 0)
        :param target: Sommet cible à atteindre (défaut : dernier sommet du graphe)
        """
        self.tg = tg

        # Choisir le sommet de départ par défaut si position est None
        if position is None:
            self.position = 0  # Premier sommet du graphe
        else :
            self.position = position


        # Choisir le sommet cible par défaut si target est None
        if target is None:
            self.target = self.tg.getNbSommets() - 1  # Dernier sommet du graphe

        else :
            self.target = target

    # Méthodes issues de Etat
    # //////////////////////////////////////////////
    def estSolution(self):
        """
        Détecte si l'état courant est une solution, c'est-à-dire si le sommet cible est atteint.

        :return: True si la position courante est le sommet cible, False sinon.
        """
        return self.position == self.target

    def successeurs(self):
        """
        Génère les états successeurs en se basant sur les voisins du sommet courant.

        :return: Liste des états successeurs (chaque état représente un voisin du sommet actuel).
        """
        successeurs = []
        voisins = self.tg.getAdjacents(self.position)  # Récupère les voisins du sommet actuel
        for voisin in voisins:
            successeurs.append(EtatCas1(self.tg, voisin, self.target))  # Crée un nouvel état pour chaque voisin
        return successeurs

    def k(self, e):
        """
        Coût du passage de l'état courant à l'état `e`.

        :param e: Un autre état (successeur de l'état courant).
        :return: Coût réel de l'arête entre `self.position` et `e.position`.
        """
        # Utiliser la méthode `getCoutArete` pour récupérer le coût entre les sommets
        return self.tg.getCoutArete(self.position, e.position)



    def displayPath(self, pere):
        """
        Affiche le chemin qui a mené à l'état courant en utilisant la map des pères.
        Calcule et affiche la longueur totale du chemin.

        :param pere: Dictionnaire donnant pour chaque état son état parent (chaîne des parents pour reconstruire le chemin).
        """
        chemin = []
        etat = self
        longueur_totale = 0

        if etat not in pere:
            print("Erreur : Le chemin n'a pas pu être reconstruit car l'état de départ est manquant dans `pere`.")
            return


        while etat in pere and pere[etat] is not None:
            chemin.append(etat.position)


            parent = pere[etat]
            cout_arete = self.tg.getCoutArete(etat.position, parent.position)
            longueur_totale += cout_arete

            etat = parent


        if etat is not None:
            chemin.append(etat.position)


        chemin.reverse()


        print(f"Chemin trouvé : {' , '.join(map(str, chemin))}")
        print(f"Longueur totale du chemin : {longueur_totale}")




    # Méthode heuristique (spécifique à A*)
    # //////////////////////////////////////////////
    def h(self):
        """
        Heuristique pour estimer la distance restante vers la cible.
        Utilise la méthode `dist` de `GrapheDeLieux` pour calculer la distance euclidienne.

        :return: Distance euclidienne entre la position courante et le sommet cible.
        """
        return GrapheDeLieux.dist(self.position, self.target, self.tg)


    # Méthodes pour pouvoir utiliser cet objet dans des listes et des dictionnaires
    # //////////////////////////////////////////////
    def __hash__(self):
        """
        Calcule un code de hachage unique pour cet état.

        :return: Code de hachage basé sur la position courante et la cible.
        """
        return hash((self.position, self.target))

    def __eq__(self, o):
        """
        Méthode de comparaison de l'état courant avec un autre état `o`.

        :param o: L'objet avec lequel on compare.
        :return: True si l'état courant et `o` sont égaux, False sinon.
        """
        return isinstance(o, EtatCas1) and self.position == o.position and self.target == o.target

    # Méthode pour affichage futur (héritée d'Object)
    # //////////////////////////////////////////////
    def __str__(self):
        """
        Représentation en chaîne de caractères de l'état courant pour affichage.

        :return: Représentation textuelle de l'état.
        """
        return f"EtatCas1(position={self.position}, target={self.target})"
