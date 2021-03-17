def qsort(inlist):
    if not inlist:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater


    
print(qsort([29, 9, 13, 56, 90, 23, 102]))
