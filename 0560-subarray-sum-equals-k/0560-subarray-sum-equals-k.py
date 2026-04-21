class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixsum = 0
        freq = {0:1}
        for i in nums :
            prefixsum += i
            count += freq.get(prefixsum - k,0)
            freq[prefixsum] = freq.get(prefixsum,0)+1
        return count
        
        