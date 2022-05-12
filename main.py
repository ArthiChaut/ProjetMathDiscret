import numpy as np
import csv

def main():
    
    with open("Vecteur.csv", 'r') as data:
        content = csv.reader(data)

        for line in content:
            vect = line
    print(vect)
    print(pageRankLinear(None, 0.9, vect))
    print(pageRankPower(None, 0.9, vect))

    


"""
IN : Une matrice d’adjacence 1 A d’un graphe dirigé, pondéré et régulier G, un vecteur
     de personnalisation v, ainsi qu’un paramètre de téléportation α compris entre
     0 et 1 (0.9 par défaut et pour les résultats à présenter). Toutes ces valeurs sont non-
     négatives.

OUT : Un vecteur x contenant les scores d’importance des noeuds ordonnés dans
      le même ordre que la matrice d’adjacence.

"""  
def pageRankLinear(A, alpha, v):
    #TODO
    pass

"""
IN : Une matrice d’adjacence A d’un graphe dirigé, pondéré et régulier G, un vec-
     teur de personnalisation v, ainsi qu’un paramètre de téléportation α compris entre 0
     et 1, α ∈ ]0, 1[ (0.9 par défaut et pour les résultats à présenter).

OUT : Un vecteur x contenant les scores d’importance des noeuds ordonnés dans
      le même ordre que la matrice d’adjacence.

"""  

def pageRankPower(A, alpha, v):
    #TODO
    pass

if __name__ == '__main__':
    main()