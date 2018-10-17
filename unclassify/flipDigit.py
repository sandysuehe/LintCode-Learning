def flipDigit(nums):
    n = len(nums)
    dp = [0] * n
    zero_count = 0

    for i in range(0, n):
        if nums[i] == 0:
            zero_count += 1

        if i == 0:
            dp[i] = 0
        else:
            if nums[i] == 0:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + 1
            dp[i] = min(dp[i], zero_count)
    return dp[n-1]

nums = [1,0,0,1,1,1]
print flipDigit(nums)
