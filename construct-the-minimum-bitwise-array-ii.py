class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for p in nums:
            if p == 2:
                ans.append(-1)
            else:
                # p is prime and > 2, so p is odd.
                # p + 1 clears the trailing ones of p and sets the next bit.
                # Example: p = 11 (1011_2) -> p+1 = 12 (1100_2)
                # The lowest set bit of p+1 is 4 (100_2).
                # The bit we want to remove from p to get the minimal answer 
                # is the one just to the right of that lowest set bit.
                # So we subtract (4 >> 1) = 2.
                # 11 - 2 = 9. Check: 9 | 10 = 11. Correct.
                
                # Get the lowest set bit of (p + 1)
                temp = p + 1
                lowbit = temp & -temp
                
                # Subtract half of the lowbit value
                ans.append(p - (lowbit >> 1))
                
        return ans
