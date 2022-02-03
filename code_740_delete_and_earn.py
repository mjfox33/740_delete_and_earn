class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            diff = abs(nums[0]-nums[1])
            return max(nums[0], nums[1]) if diff < 2 else nums[0]+nums[1]
        uni = sorted(set(nums))
        dp = [0]*len(uni)
        for i in range(len(uni)):
            n1 = uni[i]
            n0 = uni[i-1]
            if n1-n0 > 1:
                dp[i] = n1 * nums.count(n1) + dp[i-1]
            else:
                dp[i] = max(n1* nums.count(n1)+dp[i-2], dp[i-1])
        return max(dp[-1],dp[-2])

s = Solution()
s.deleteAndEarn([1,1,1,2,4,5,5,5,6])
