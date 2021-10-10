# coding=utf-8
"""
 Bubble sort / tri a bulle algorithme
"""
def tri_a_bulle(table):
    """
    fonction pour tri a bulle
    """
    stop = len(table) - 1 # variable pour determiner l'indice auquel le tri termine

    for i in range(stop): 
        for j in range(stop - i):
            if table[j] > table[j + 1]: # si la valeur de gauche est plus grande que la valeur suivante de droite
                table[j], table[j + 1] = table[j + 1], table[j] # intervertir les valeurs

    return table

print(tri_a_bulle([3,4,57,3,45,26,3]))