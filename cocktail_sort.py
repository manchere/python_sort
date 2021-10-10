# coding=utf-8
"""
 Cocktail sort / tri shaker algorithme
"""
def tri_shaker(table = []):
    """
    fonction pour cocktail sort
    """
    interversion = True # variable pour vérifier si le tableau est trié
    start = 0 # variable pour definir à partir de quel index commencer le tri
    stop = len(table) - 1 # variable pour définir à partir de quel index commencer le tri
    while interversion is True:

        interversion = False #mettre la variable "interversion" à False avant de trier (restera "False si aucun tri n'est effectué")
        for i in range(start, stop): # tri de gauche à droite
            if table[i] > table[i + 1]:
                table[i], table[i + 1] = table[i + 1], table[i] # intervertir les valeurs
                interversion = True
        stop -= 1
        # A present la derniere valeur trié
        # dans le tableau est la plus grande, décrémenter "stop" de 1 pour ne pas acceder au dernier index du tableau
        # au prochain tri de gauche à droite

        if not interversion:
            break
        # Si aucune interversion n'a été effectué, sortir de la boucle "while"

        interversion = False # remettre la variable "interversion" à false avant de trier (restera "False si aucun tri est effectué")
        for i in range(stop - 1, start - 1,  -1):
            if table[i] > table[i + 1]:
                table[i], table[i + 1] = table[i + 1], table[i]
                interversion = True
        start += 1
        # A present la premiere valeur trié
        # dans le tableau est la plus petite, incrémenter "start" de 1 pour ne pas acceder au premier index du tableau
        # au prochain tri de droite à gauche

    return table

print(tri_shaker([3,2,31,5,3,32,34,1,5]))
 