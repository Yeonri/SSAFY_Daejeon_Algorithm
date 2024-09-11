N, K = map(int, input().split())

dp = [0] * (K + 1)
coin = []

# 모든 동전에 대해서 처음 0은 전부 만들 수 있으므로 1로 설정한다.

for _ in range(N):
    coin.append(int(input()))

# 맨 처음값을 저장하기 위해 맨 처음 코인으로 i를 만들 수 있을 때, 1을 작성한다.
# -> 사용할 수 있는 동전은 하나밖에 없기 때문에
for i in range(K + 1):
    if i % coin[0] == 0:
        dp[i] = 1

# 다음 코인들에 대해서 가능한 수들을 더해준다.

for i in range(1, N):
    for j in range(K + 1):

        if j - coin[i] < 0: continue

        # if i == N -1:
        #     print(j, dp[j - coin[i]])

        dp[j] += dp[j - coin[i]]

print(dp[-1])


# 제일 처음 값인 0을 설정하는 방법

# N, K = map(int, input().split())

# dp = [[0] * (K + 1) for _ in range(N)]
# coin = []

# # 모든 동전에 대해서 처음 0은 전부 만들 수 있으므로 1로 설정한다.
# for i in range(N):
#     dp[i][0] = 1

# for _ in range(N):
#     coin.append(int(input()))

# coin.sort()

# # 맨 처음값을 저장하기 위해 맨 처음 코인으로 i를 만들 수 있을 때, 1을 작성한다.
# # -> 사용할 수 있는 동전은 하나밖에 없기 때문에
# for i in range(K + 1):
#     if i % coin[0] == 0:
#         dp[0][i] = 1

# # 현재 위치는 현재 선택된 동전의 dp배열에서 [i - (현재 동전의 수)]를 더해주고,
# # 위에서 만들 수 있는 경우의 수를 합쳐준다. 

# for i in range(1, N):
#     for j in range(1, K + 1):
#         dp[i][j] = dp[i][j-coin[i]] + dp[i - 1][j]

# print(dp[-1][-1])