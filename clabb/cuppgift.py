import random
from statistik import Statistik


def findKthBest(k, data, low, high, statistik):
    '''från specen'''
    pivotindex = random.randint(low, high)
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]

    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low, high, data[high], statistik)

    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]

    statistik.nrComparisons += 1
    if pivotmid == k:
        return data[pivotmid]
    elif k < pivotmid:
        return findKthBest(k, data, low, pivotmid - 1, statistik)
    else:
        return findKthBest(k, data, pivotmid + 1, high, statistik)


def partitionera(data, v, h, pivot, statistik):
    '''fårn föreläs 7,specen, den tar O(n) jämförelser'''
    v -= 1
    while True:
        v += 1
        statistik.nrComparisons += 1
        while data[v] < pivot:
            statistik.nrComparisons += 1
            v = v + 1
        h = h - 1    # hoppa över pivot
        statistik.nrComparisons += 1
        while h != 0 and data[h] > pivot:
            statistik.nrComparisons += 1
            h = h - 1
        data[v], data[h] = data[h], data[v]

        statistik.nrComparisons += 1
        if v >= h:
            break
    data[v], data[h] = data[h], data[v]
    return v


def generateList(N, partition=1):
    if partition == 1:  # två tal fårn inte förekomma 2 ggr
        data = list(range(0, N))
        random.shuffle(data)
        return data
    else:
        data = [None] * N
        for i in range(0, N):
            data[i] = random.randint(0, N-1)
    return data


if __name__ == '__main__':
    skrivtab = True
    tests = 1000
    minN = 10
    maxN = 50
    mink = 1
    NStepLen = 5
    kStepLen = 1
    if skrivtab is True:
        matlabEmptyCell = 'NaN'
        csvtab = open("tab.csv", 'w')
        mtabmean = open("tabmean.m", 'w', encoding="utf-8")
        mtabls = open("tabls.m", 'w', encoding="utf-8")

        csvtab.write('N\k')
        mtabmean.write('meant=['+matlabEmptyCell)
        mtabls.write("ls=nan("+str((maxN-minN)/NStepLen+2)+","+str(maxN/kStepLen)+","+str(tests) +");\n")
        kindex=0
        for k in range(mink, maxN, kStepLen):
            csvtab.write(','+str(k))
            mtabmean.write(','+str(k))
            mtabls.write('ls(1,'+str(kindex+2)+',:)='+str(k)+';\n')
            kindex+=1
        Nindex=0
        for N in range(minN, maxN+1, NStepLen):
            print(N)
            csvtab.write('\n'+str(int(N)))
            mtabmean.write(';\n'+str(int(N)))
            mtabls.write('\n\nls('+str(Nindex+2)+',1,:)='+str(N)+';\n')
            kindex=0
            for k in range(mink, maxN, kStepLen):
                # for i in range(0, maxN, N//NStepLen):
                csvtab.write(',')
                mtabmean.write(',')
                if k < N:
                    statistik = Statistik()
                    data = generateList(N, 0)
                    best = findKthBest(k, data, 0, N-1, statistik)
                    for i in range(0, tests):
                        statistik.newSet()
                        data = generateList(N, 0)
                        best = findKthBest(k, data, 0, N-1, statistik)
                    csvtab.write(str(statistik.mean()))
                    mtabmean.write(str(statistik.mean()))
                    mtabls.write('ls('+str(Nindex+2)+','+str(kindex+2)+',:)='+str(statistik.comparisonsList)+';\n')
                else:
                    mtabmean.write(matlabEmptyCell)
                kindex+=1
            Nindex+=1
        csvtab.close()
        mtabmean.write('];')
        mtabmean.close()
        mtabls.close()
