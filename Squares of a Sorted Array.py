class Solution(object):
    def sortedSquares(self, nums):
        
        i=0
        j=len(nums)-1
        k= len(nums)-1
        ls = []
        
        while i<=j:
            if (nums[j]*nums[j]) > (nums[i]*nums[i]):
                ls.append(nums[j]*nums[j])
                j-=1
            elif (i==j):
                ls.append(nums[j]*nums[j])
                j-=1
                i+=1
                
            elif (nums[j]*nums[j]) == (nums[i]*nums[i]):
                ls.append(nums[j]*nums[j])
                ls.append(nums[i]*nums[i])
                j-=1
                i+=1
            
            else:
                ls.append(nums[i]*nums[i])
                i+=1
        ls.reverse()
        return ls
        #here in above if it is possible to store elements in reverse order then can reduce time complexity also. it is like ls[k--]    
        # n=[]
        # for i in nums:
        #     n.append(i*i)
        # return sorted(n)
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
