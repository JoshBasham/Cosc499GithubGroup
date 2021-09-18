##the median of the array

def median(nums):
    n = len(nums)
    if n%2 == 0:
        median1 = nums[n//2]
        median2 = nums[n//2-1]
        median = (median1 + median2)/2
    else:
        median = nums[n//2]
    return median