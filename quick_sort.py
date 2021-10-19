def pivInd(table):
    return int(round(len(table) * 0.5))

def partitionneur(table):
    small_indice = 0
    table[0], table[pivInd(table)] = table[pivInd(table)], table[0]

    for indice in range(1, len(table)):
        if table[0] > table[indice]:
            small_indice += 1
            table[small_indice], table[indice] = table[indice], table[small_indice]

    table[0], table[small_indice] = table[small_indice], table[0]
      
    return table

t = [23,4,63,5,6,5,2,10]



print(partitionneur(t))
