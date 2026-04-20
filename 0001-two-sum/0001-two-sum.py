class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j] == target):
                    a.append(i)
                    a.append(j)
                    break
        return a
                