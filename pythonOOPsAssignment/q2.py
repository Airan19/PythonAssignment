"""Create arithmetics class to calculate avg, mean, mode and standard deviation

"""

class Arithmetics:
    def __init__(self, data):
        self.data = data

    # The average of all the elements present in data list
    def mean(self):
        return sum(self.data) / len(self.data)


    def median(self):
        self.data.sort()
        # If the length of list is even then we will have two elements as mid from either side of the list,
        # thus after finding those elements we find their mean
        if len(self.data) % 2 == 0:
            median1 = self.data[len(self.data)//2]
            median2 = self.data[len(self.data)//2 - 1]
            median = (median1 + median2)/2
        
        # or if length of data list is odd, then we will simply get one mid element
        else:
            median = self.data[len(self.data)//2]
        return median
        
    # To find the element with maximum frequency in the data list
    def mode(self):
        mode = None
        count = 0
        for i in self.data:
            curr_frequency = self.data.count(i)
            if curr_frequency > count:
                count = curr_frequency
                mode = i
        return mode
    
    def stddev(self):
        mean = self.mean()
        variance = sum([((x - mean) ** 2) for x in self.data]) / (len(self.data)-1)
        return variance**0.5


data = [1,2,3,4,5,6,7,8,9,10]
calc = Arithmetics(data)
print("Mean: ", calc.mean())
print("Median: ", calc.median())
print("Mode: ", calc.mode())
print("Standard Deviation: ", calc.stddev())
