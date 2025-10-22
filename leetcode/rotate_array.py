def rotate(nums : list[int], k : int)-> None:
    n = len(nums)
    k = k%n
    nums.reverse() # La fonction reverse inverse la liste et retourne none
    nums[:k]= reversed(nums[:k]) 
    nums[k:]= reversed(nums[k:])

nums = [1,2,3,4,5]
rotate(nums,5)
print(nums)