"""

"""

def solutions(sorted_list):
    """
    给列表能不能返回和的一半方式
    :param sorted_list:
    :return:
    """
    N = len(sorted_list)
    sums = int(sum(sorted_list)/2)
    dp = [[False] * (sums+1)] * (N+1)
    for i in range(N):
        dp[i][0] = True
    for i in range(1, N+1):
        for j in range(1, sums+1):
            if j - sorted_list[i - 1] < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] | dp[i-1][j-sorted_list[i-1]]
    return dp[N][sums]

a = [1,2,2,5]
print(solutions(a))