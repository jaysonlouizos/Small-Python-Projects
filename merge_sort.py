import pytest

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        a = mergesort(arr[:mid])
        b = mergesort(arr[mid:])
        finallist = merge(a,b)
        return finallist
    else:
        return arr    

def merge(a,b):
    
    maxloop = len(a) + len(b)
    aloop = 0
    bloop = 0
    loop = 0
    finallist = []

    while maxloop != loop:
    
        if a[aloop] < b[bloop]:
            finallist.append(a[aloop])
            aloop = aloop + 1
            loop = loop + 1
            if aloop == len(a):
                a = [100000000000000000000]
                aloop = 0
    
        elif b[bloop] < a[aloop]:
            finallist.append(b[bloop])
            bloop = bloop + 1
            loop = loop + 1
            if bloop == len(b):
                b = [1000000000000000000000]
                bloop = 0

    return finallist
