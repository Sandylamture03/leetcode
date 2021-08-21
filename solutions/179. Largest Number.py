class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if max(nums)==0:
            return '0'
        
        for i in range(0,len(nums)):
            nums[i]=str(nums[i])
               
        
        ln=[nums[0]]
        
        for i in range(1,len(nums)):
            placed=0
            for j in range(0,len(ln)):
                if nums[i]+ln[j]>=ln[j]+nums[i]:
                    ln.insert(j,nums[i])
                    placed=1
                    break
            if placed==0:
                ln.append(nums[i])
        
        largest_number=''.join(ln)
        return largest_number
