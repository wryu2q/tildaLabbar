class Statistik:
    def __init__(self):
        self.nrComparisons = 0
        self.comparisonsList = []

    def __str__(self):
        return 'max='+str(self.max())+' min='+str(self.min())+' mean='+str(self.mean())

    def newSet(self):
        self.comparisonsList.append(self.nrComparisons)
        self.nrComparisons = 0

    def max(self):
        return max(self.comparisonsList)

    def min(self):
        return min(self.comparisonsList)

    def mean(self):
        return sum(self.comparisonsList)/len(self.comparisonsList)

    def varians(self):
        mean = self.mean()
        var = 0
        for i in range(0, len(self.comparisonsList)):
            var += (self.comparisonsList[i] - mean)**2
        return var/len(self.comparisonsList)-1
