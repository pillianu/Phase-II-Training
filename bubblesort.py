def bubblesort(nums):
    n=len(nums)
    fixPosition=n-1
    while fixPosition>0:
        for i in range(0,fixPosition):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
            #print(nums)
        fixPosition-=1
nums=[9,8,7,6,5,4,3,2,1]
print("Befoe Sorting",nums)
bubblesort(nums)
print("Before Sorting",nums)