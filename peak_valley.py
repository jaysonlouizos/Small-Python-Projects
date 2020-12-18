def peak(data:list) -> list:
    working = 1
    peak = []
    while working != len(data) - 1:
        
        bigger = working + 1
        smaller = working - 1
        if working ==  len(data):
            bigger = working
        if data[bigger] < data[working] and data[smaller] < data[working]:
            peak.append(working)
        working = 1 + working 
    
    return peak

def valley(data:list) -> list:
    working = 1
    valley = []    
    while working != len(data) - 1:
        
        bigger = working + 1
        smaller = working - 1
        if working ==  len(data):    
            bigger = working
        if data[bigger] > data[working] and data[smaller] > data[working]:
            valley.append(working) 
        working = 1 + working
    
    return valley

def peaks_valleys(data):
    finallist = []
    finallist.extend(peak(data))
    finallist.extend(valley(data))
    finallist.sort()
    flood(data,peak(data))
    return finallist

peaks_valleys([1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9])