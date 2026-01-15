class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        # Helper function to find the maximum contiguous gap
        def get_max_gap(bars):
            if not bars:
                return 1
            
            # Sort bars to easily find consecutive sequences
            bars.sort()
            
            max_consecutive = 1
            current_consecutive = 1
            
            for i in range(1, len(bars)):
                # If current bar is exactly 1 greater than previous, it's consecutive
                if bars[i] == bars[i - 1] + 1:
                    current_consecutive += 1
                else:
                    # Sequence broken, update max and reset counter
                    max_consecutive = max(max_consecutive, current_consecutive)
                    current_consecutive = 1
            
            # Final check for the last sequence
            max_consecutive = max(max_consecutive, current_consecutive)
            
            # A sequence of k consecutive removed bars creates a gap of size k + 1
            return max_consecutive + 1

        # Get max gaps for horizontal and vertical dimensions
        max_h_gap = get_max_gap(hBars)
        max_v_gap = get_max_gap(vBars)
        
        # The largest square is limited by the smaller dimension
        side = min(max_h_gap, max_v_gap)
        
        return side * side
