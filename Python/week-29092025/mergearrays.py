#Merge to arrays and sort them

#if i have to two arrays of respectve sizes n and m
#I can merge them in a single array of size n+m

# a = [1,2,3,4]
# x = len(a)
# b = [9,8,6,5]
# a[x:]=b
# a.sort()
# print(a)

def mergearrays_1(arr1, arr2):
    m = len(arr1)
    arr1[m:]=arr2
    arr1.sort()
    return arr1

def mergearrays_2(arr1,arr2):
    arr1.extend(arr2) 
    arr1.sort()
    return arr1

print(mergearrays_1(arr1=[3,6,7], arr2= [1,9,5]))
print(mergearrays_2(arr1=[3,6,7], arr2= [1,9,5]))


#Supprimer les occurences dans une liste 
def removeElement(nums, val):
    #Declare a pointer at the position 0
    k = 0
    # I go through the arrays
    for i in range(len(nums)):
        #I add the condition 
        #if the integer at the position i in nums != of val, I give it to nums[k]
        if nums[i]!=val:
            nums[k]= nums[i]
            k+=1
    return k
    

print("-------------------------------------------------------------")
# nums = [1,2,3,5,7,9,2,2]
# val = 2
# k=0
# for i in range (len(nums)):
#     if nums[i]!= val : 
#         nums[k]=nums[i]
#         k+=1
# print(k)
# print(nums)

print(removeElement(nums = [1,2,3,5,7,9,2,2],val=2))

