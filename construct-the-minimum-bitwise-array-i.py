class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for p in nums:
            if p == 2:
                ans.append(-1)
            else:
                # Find the position of the first zero bit starting from LSB
                # Since p is prime > 2, it is always odd, so loop starts checking higher bits.
                bit = 1
                while (p & bit):
                    bit <<= 1
                
                # 'bit' is now the value of the first zero bit (e.g., for 7 (111), bit is 8 (1000))
                # We subtract half of that value (bit >> 1) to flip the MSB of the trailing 1s.
                ans.append(p - (bit >> 1))
                
        return ans

  
