# Sissi Xu S3C2
def groupSum(start, nums, target):
    if target == 0:
        return True
    if start == len(nums) and target != 0:
        return False
    return groupSum(start + 1, nums, target-nums[start]) or groupSum(start + 1, nums, target)
def groupSum6(start, nums, target):
    if target == 0:
        return True
    elif nums[start] == 6:
        return groupSum6(start + 1, nums, target - nums[start])
    elif start == len(nums) and target != 0:
        return False
    return groupSum6(start + 1, nums, target - nums[start]) or groupSum6(start + 1, nums, target)
def groupNoAdj(start, nums, target):
    if target == 0:
        return True
    elif start >= len(nums) and target != 0:
        return False
    return groupNoAdj(start + 2, nums, target - nums[start]) or groupNoAdj(start + 1, nums, target)
def groupSum5(start, nums, target):
    if  target == 0:
        return True
    elif start == len(nums) and target != 0:
        return False
    elif nums[start] % 5 == 0 and nums[start + 1] == 1:
        return groupSum5(start + 2, nums, target - nums[start])
    elif nums[strat] % 5 == 0:
        return groupSum5(start + 1, nums, target - nums[start])
    return groupSum5(start + 1, nums, target - nums[start]) or groupSum5(start + 1, nums, target)
def groupSumClump(start, nums, target):
    i = 1
    if target == 0:
        return True
    elif start >= len(nums) and target != 0:
        return False
    elif start < len(nums) - 1:
        while nums[start] == nums[start + i] and (start + i) < len(nums) - 1:
            i = i+1
    return groupSumClump(start + i, nums, target - nums[start]*i) or groupSumClump(start + i, nums, target)
def splitArray(nums, x = 0, y = 0, start = 0):
    if start == len(nums) and x == y:
        return True
    elif start >= len(nums) and x != y:
        return False
    return splitArray(nums, x+nums[start], y, start+1) or splitArray(nums, x, y_nums[start], start+1)
def splitOdd10(nums,x = 0,y = 0,start = 0):
    if start >= len(nums):
        if x % 10 == 0 and y % 2 == 1:
            return True
        if x % 2 == 1 and y % 10 == 0:
            return True
        return False
    return splitOdd10(nums, x+nums[start], y, start+1) or splitOdd10(nums, x, y+nums[start], start+1)
def split53(nums,x = 0,y = 0,start = 0):
    if start == len(nums) and x == y:
        return True
    if start == len(nums) and x != y:
        return False
    if nums[start] % 5 == 0:
        return split53(nums,x+nums[start],y,start+1)
    if nums[start] % 3 == 0:
        return split53(nums,x,y+nums[start],start+1)
    return split53(nums, x+nums[start], y, start+1) or split53(nums, x, y+nums[start], start+1)
