class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # If k is 1, the difference between the score and itself is always 0
        if k == 1:
            return 0
        
        # Sort the scores to group closest values together
        nums.sort()
        
        # Initialize minimum difference to infinity
        min_diff = float('inf')
        
        # Use a sliding window of size k
        # We iterate through the array where 'i' is the start of the window
        # and 'i + k - 1' is the end of the window.
        for i in range(len(nums) - k + 1):
            # The difference for the current window is the last element minus the first
            current_diff = nums[i + k - 1] - nums[i]
            
            # Update the global minimum
            if current_diff < min_diff:
                min_diff = current_diff
                
        return min_diff
