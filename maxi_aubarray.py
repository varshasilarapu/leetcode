class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c_sum = 0
        Max_sum =nums[0]

        for n in nums:
            c_sum+=n
            Max_sum = max(Max_sum,c_sum)
            if c_sum <0:
                c_sum=0
        return Max_sum
