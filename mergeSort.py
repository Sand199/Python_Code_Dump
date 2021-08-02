def mergeSort(L):
    """ Sorts a list at Complexity O(nlogn) where n is the len(L)"""
    def merge(La, Lb):
        Ln = []
        a = b = 0

        while a < len(La) and b < len(Lb):
            if La[a] < Lb[b]:
                Ln.append(La[a])
                a += 1
            else:
                Ln.append(Lb[b])
                b += 1

        while a < len(La):
            Ln.append(L[a])
            a += 1
        while b < len(Lb):
            Ln.append(L[b])
            b += 1
        return Ln

    if len(L) < 2:
        return L

    q = len(L)//2

    return merge(mergeSort(L[0:q]),mergeSort(L[q:]))

