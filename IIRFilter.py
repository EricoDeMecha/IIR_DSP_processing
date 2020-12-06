import IIR2Filter


class IIRFilter:
    def __init__(self, sos):
        self.sos = sos
        self.IIR = [IIR2Filter.IIR2Filter(*self.sos) for i in range(20)]  # creates a chain of IIR2Filter objects and
        # pass the elements of the sos to the constructor of each.

    def filter(self, x):
        result = [obj.filter(x) for obj in self.IIR]  # pass the value x through  the chain of IIR2Filters while
        # calling the filter function.
        return sum(result)/len(result)
