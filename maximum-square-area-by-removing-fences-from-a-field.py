class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # Step 1: Add the boundary fences 1 and m/n to the lists
        # We need to consider the outer borders of the field as valid fence lines
        hFences.extend([1, m])
        vFences.extend([1, n])
        
        # Sort the fences to easily calculate distances between pairs
        hFences.sort()
        vFences.sort()
        
        # Step 2: Calculate all possible distances (heights) between horizontal fences
        h_diffs = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                # The distance between fence j and fence i
                h_diffs.add(hFences[j] - hFences[i])
                
        # Step 3: Calculate vertical distances and check for intersection with horizontal distances
        max_side = -1
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_diff = vFences[j] - vFences[i]
                
                # If this vertical width matches a horizontal height, we found a square
                if v_diff in h_diffs:
                    max_side = max(max_side, v_diff)
        
        # Step 4: Return result
        if max_side == -1:
            return -1
        
        # Calculate area with modulo as requested
        return (max_side * max_side) % (10**9 + 7)
