# coding=utf-8
"""
 Bubble sort / tri a bulle algorithme
"""
def tri_a_bulle(table):
    """
    fonction pour tri a bulle
    """
    stop = len(table) - 1 # variable pour définir à partir de quel index commencer le tri

    for i in range(stop):
        for j in range(stop - i):
            if table[j] > table[j + 1]:
                table[j], table[j + 1] = table[j + 1], table[j]

    return table

print(tri_a_bulle([3,4,57,3,45,26,3]))

