from pprint import pprint
from collections import deque
from copy import deepcopy

K, M = map(int, input().split())
N = 5

origin_matrix = [list(map(int, input().split())) for _ in range(N)]

pre_number = list(map(int, input().split()))



def chk_spin(matrix, lst, spin_count, x, y):
    count = 0

    # 3x3 부분 행렬 추출
    temp = [
        [matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1]],
        [matrix[i][j - 1], matrix[i][j], matrix[i][j + 1]],
        [matrix[i + 1][j - 1], matrix[i + 1][j], matrix[i + 1][j + 1]]
    ]

    if spin_count == 0:
        # 90도 회전
        rotated = [
            [temp[2][0], temp[1][0], temp[0][0]],  # 1st column
            [temp[2][1], temp[1][1], temp[0][1]],  # 2nd column
            [temp[2][2], temp[1][2], temp[0][2]]  # 3rd column
        ]

    if spin_count == 1:
        # 180도 회전
        rotated = [
            [temp[2][2], temp[2][1], temp[2][0]],
            [temp[1][2], temp[1][1], temp[1][0]],
            [temp[0][2], temp[0][1], temp[0][0]]
        ]

    elif spin_count == 2:
        # 270도 회전 (90도 반시계 방향)
        rotated = [
            [temp[0][2], temp[1][2], temp[2][2]],
            [temp[0][1], temp[1][1], temp[2][1]],
            [temp[0][0], temp[1][0], temp[2][0]]
        ]

    # 회전된 값을 원래 행렬에 반영
    for di in range(3):
        for dj in range(3):
            matrix[i - 1 + di][j - 1 + dj] = rotated[di][dj]



    # return (spin_count, )


for j in range(1, N - 1):
    for i in range(1, N - 1):
        for k in range(3):
            tmp_matrix = deepcopy(origin_matrix)
            tmp_number = deepcopy(pre_number)

            chk_spin(tmp_matrix, tmp_number, k, i, j)