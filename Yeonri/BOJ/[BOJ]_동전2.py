N, K = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(input()))

dp = [0] * (K + 1)


for j in range(1, K + 1):
    if j % coins[0] == 0:
        dp[j] = dp[j - 1] + 1
    else:
        dp[j] = dp[j - 1]

for i in range(N):
    for j in range(1, K + 1):
        
        if j % coins[i] == 0: 
            dp[j] = 1


print(dp)
print(dp[-1])