def pivInd(table):
    return int(round(len(table) * 0.5))

def interversion(val1, val2):
    val1, val2 = val2, val1

def partitionneur(table):
    small_indice = 0
    interversion(table[0], table[pivInd(table)])

    for indice in range(1, len(table)):
        if table[0] > table[indice]:
            small_indice += 1
            interversion(table[small_indice], table[indice])

    interversion(table[0], table[small_indice])
    return table

def quick_sort1(table):
    if len(table) > 1:
        quick_sort1(partitionneur(table), start, end)
        quick_sort1(partitionneur(),)
    else:
        return table

t = [23,4,63,5,6,5,2,10]

# def quickSort(start, end):
print(partitionneur(t))

#-----------------------------------------------------------------------------------------------------------------------
def quicksort(table):
    if len(table) <=  1:
        return table
    else:
        pivot = table.pop()
    high_sub = []
    low_sub = []
    for item in table:
        if item < pivot:
            low_sub.append(item)
        else:
            high_sub.append(item)
    return quicksort(low_sub) + [pivot] + quicksort(high_sub)

print(quicksort([34,6,4,5667,333,55,43]))