class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 1. Sort the array.
        # The minimum difference must occur between adjacent elements in a sorted array.
        arr.sort()
        
        min_diff = float('inf')
        result = []
        
        # 2. Iterate through the array to compare adjacent pairs
        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]
            
            # If we find a new smaller difference, discard previous pairs and start a new list
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i], arr[i+1]]]
            
            # If we find a difference equal to the current minimum, append to the list
            elif diff == min_diff:
                result.append([arr[i], arr[i+1]])
                
        return result
