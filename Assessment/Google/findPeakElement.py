nums = [1,2,1,3,5,6,4]


def findPeakElement(nums):
    # Base case
    if len(nums) == 0:
        return -1
    start , end = 0, len(nums) -1
    while start < end:
        mid = (end+start)//2
        if nums[mid] > nums[mid+1]:
            end = mid
        else:
            start = mid+1
    return start


print(findPeakElement(nums))