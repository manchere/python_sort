"""
 Cocktail sort / tri shaker algorithm
"""
def cocktail_sort(list_to_sort = []):
    """
    # function for cocktail sort
    """
    interversion = True
    start = 0
    stop = len(list_to_sort) - 1
    while interversion is True:

        interversion = False
        for i in range(start, stop):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                interversion = True
        stop -= 1
        

        if not interversion:
            break

        interversion = False
        for i in range(stop - 1, start - 1,  -1):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                interversion = True
        start += 1

    return list_to_sort

print(cocktail_sort([3,2,31,5,3,32,34,1,5]))

 
 