def partitionneur(pivot, table = []):
    small_indice = 0
    indice = 0 
    pivot, table[0] = table[0], pivot

    for indice in range(len(table) - 1):
        if table[indice] < pivot:
            small_indice += 1
            table[small_indice], table[indice] = table[indice], table[small_indice]
    
    pivot, table[small_indice] = table[small_indice], pivot

    return table


t = [23,4,63,5,6,5,2,10]



print(partitionneur(t[-1], t))