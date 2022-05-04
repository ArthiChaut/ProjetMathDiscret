import numpy as np

def main():
    with open("VecteurPersonnalisation_Groupe18.csv") as data:
        content = data.read()
    vect = []
    for i in content.split(','):
        vect += [float(i)]
    vect = np.asarray(vect)
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