def twoSum(nums, target: int):
    h={}
    for i,num in enumerate(nums):
        r=target-num
        if r not in h:
            h[num]=i
        else:
            return [h[r],i]

print(twoSum(nums=[3,3], target=6))