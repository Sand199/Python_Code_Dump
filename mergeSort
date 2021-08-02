def mergeSort(L):
    def merge(La, Lb):
        Ln = []  
        a = b = 0
        while a < len(La) and b< len(Lb): 
            if La[a] < Lb[b]: 
                Ln.append(La[a])
                a += 1   
            else:    
                Ln.append(Lb[b])
                b += 1   
        if a == len(La): 
            Ln.extend(Lb[b:])
        else:    
            Ln.extend(La[a:])
        return Ln

    if len(L) < 2:
        return L 
    else:    
        q = len(L)//2
        return merge(mergeSort(L[0:q]),mergeSort(L[q:]))
