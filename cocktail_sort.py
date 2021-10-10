# coding=utf-8
"""
 Cocktail sort / tri shaker algorithme
"""
def tri_shaker(table = []):
    """
    fonction pour tri shaker
    """
    interversion = True # variable pour vérifier si le tableau est trié
    start = 0 # variable pour déterminer le premier indice à partir duquel le tri doit commencer
    stop = len(table) - 1 # variable pour déterminer le dernier indice de l'élement à trier
    while interversion is True:

        interversion = False # mettre la variable "interversion" à False avant de trier (restera "False si aucun tri n'est effectué")
        for i in range(start, stop): # tri de gauche à droite
            if table[i] > table[i + 1]:
                table[i], table[i + 1] = table[i + 1], table[i] # intervertir les valeurs
                interversion = True
        stop -= 1
        # A présent la dernière valeur trié
        # dans le tableau est la plus grande, décrémenter "stop" de 1 pour ne pas accéder au dernier indice du tableau
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
        # A présent la premiere valeur trié
        # dans le tableau est la plus petite, incrémenter "start" de 1 pour ne pas acceder au premier indice du tableau
        # au prochain tri de droite à gauche

    return table

print(tri_shaker([3,2,31,5,3,32,34,1,5]))
 