class Solution(object):
    def moveZeroes(self, nums): 
        num=0
        zr=0
        while len(nums)>num:
            if nums[num]==0:
                num+=1
            elif nums[num] != 0:
                if nums[num]==nums[zr]:
                    num+=1
                    zr+=1
                else:
                    nums[zr]=nums[num]
                    nums[num]=0
                    num+=1
                    zr+=1
                    
                    
#second solutions using inbuild fun
       
#         for i in nums:
#             if i is 0:
#                 nums.remove(i)
#                 nums.append(0)

        
