
def arrayMean(numArray):
    count = len(numArray)
    sum =0
    for n in numArray:
        sum = n + sum
    mean = (sum / count)
    return mean



