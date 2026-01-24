class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Step 1: Sort the array
        nums.sort()
        
        max_pair_sum = 0
        n = len(nums)
        
        # Step 2: Pair smallest with largest
        # We only need to iterate through the first half
        for i in range(n // 2):
            # Sum of the current smallest (i) and largest (n-1-i)
            current_sum = nums[i] + nums[n - 1 - i]
            
            # Update the maximum pair sum found so far
            max_pair_sum = max(max_pair_sum, current_sum)
            
        return max_pair_sum
