class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0
        
        while True:
            # Step 1: Check if the array is already sorted
            is_sorted = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    is_sorted = False
                    break
            
            if is_sorted:
                return operations
            
            # Step 2: Find the adjacent pair with the minimum sum
            # We initialize min_sum to infinity and best_idx to -1
            best_idx = -1
            min_sum = float('inf')
            
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]
                # We use strict inequality (<) to respect the "leftmost" tie-breaker rule.
                # If current_sum == min_sum, we keep the previous (smaller) index.
                if current_sum < min_sum:
                    min_sum = current_sum
                    best_idx = i
            
            # Step 3: Replace the pair with their sum
            new_val = nums[best_idx] + nums[best_idx + 1]
            nums[best_idx] = new_val
            nums.pop(best_idx + 1)
            
            operations += 1
