# 5*5 격자
# 3*3 격자를 선택해서 회전 -> 회전이 가능한 위치를 선택하도록 한다.
# 회전 함수를 설정 90도로 설정한 후, 2배 3배를 한다. -> 90 180 270
# 획득 가치를 최대화 -> 회전 각도가 제일 작은 것 선택
# 회전 중심 좌표의 열이 가장 작은 구간, 열이 같다면 행이 가장 작은 구간
# 새로운 유물 생성 -> 열 다음 행  for i in range(N-1, -1, -1) for j in range(0, N - 1)
# 유물 연쇄 획득 가능

# 1. 유물 획득이 가능한지 확인
# 2. 회전 -> 유물 획득 확인
# 3. 유물 가능하면 획득 후, 채워놓기
# 4. 유물 획득 가능 확인

# 가능 범위 (1,1) ~ (4,4)

# K 탐사 반복 횟수, M 유물 조각 개수
from collections import deque
from collections import defaultdict
from copy import deepcopy

DXY = [(1, 0), (-1, 0),(0, 1), (0, -1)]

def rotate(matrix, init_i, init_j):
    new_matrix = [x[:] for x in matrix] # 복사한 메트릭스를 다시 복사

    for i in range(-1, 2):
        for j in range(-1, 2):
            new_matrix[init_i + j][init_j - i] = matrix[init_i + i][init_j + j]

    return new_matrix


def bfs(matrix, visited, i, j, flag):
    s_x, s_y = (i, j)
    queue = deque([(s_x, s_y)])

    tmp_dir = set()
    tmp_dir.add((s_x, s_y))
    visited.add((s_x, s_y))

    count = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in DXY:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited and matrix[x][y] == matrix[nx][ny]:
                tmp_dir.add((nx, ny))
                visited.add((nx, ny))
                count += 1
                queue.append((nx, ny))

    if count >= 3:
        if flag:
            for x, y in tmp_dir:
                matrix[x][y] = 0
        return count
    return 0


def chk_matrix(matrix, flag):

    # 각 방문 좌표들을 vistied set에 저장
    # 탐색을 전체 값에 대해 하지 않고, 회전한 값들에 대해서만 탐색을 하도록 만든다.
    # 모든 방향에 대해서 탐색을 진행하도록 한다.

    # 탐색을 줄이기 위한 위의 방식에 대한 엣지 케이스
    # 만약에 회전을 하지 않는 부분에 연결이 되어있는 케이스는 탐색을 하지 못한다.

    # 따라서 모든 좌표를 탐색하도록 설정을 먼저 해본다.

    visited = set()
    result = 0

    for i in range(N):
        for j in range(N):
            if (i, j) not in visited:
                result += bfs(matrix, visited, i, j, flag)

    return result


N = 5 # 매트릭스 크기
S = 3 # 회전 크기

K, M = map(int, input().split())
matrix = [list(map(int, input().split()))for _ in range(N)]
pre_number = deque(list(map(int, input().split())))

result = []

for _ in range(K): # 탐색 횟수
    max_count = 0
    for rotation_count in range(1, 4):
        for init_j in range(1, N-1): # 중심 좌표 선택
            for init_i in range(1, N-1):

                new_matrix = [x[:] for x in matrix] # 깊은 복사

                for _ in range(rotation_count): # 회전 횟수 만큼 회전
                    new_matrix = rotate(new_matrix, init_i, init_j)

                # 최대 값을 가지는 matrix를 먼저 확인할 수 있도록 flag 설정
                # False는 유물 발굴을 하지 않는다.
                tmp_count = chk_matrix(new_matrix, False)

                if max_count < tmp_count:
                    max_count = tmp_count
                    result_matrix = new_matrix

    if max_count == 0:
        break

    count = 0

    # 최종적으로 선택된 matrix를 이용해서 유물 발굴을 시작

    while True:
        t = chk_matrix(result_matrix, True)
        if t == 0:
            break
        count += t

        for j in range(N):
            for i in range(4, -1, -1):
                if result_matrix[i][j] == 0:
                    result_matrix[i][j] = pre_number.popleft()

    result.append(count)
    
    # 다음 단계를 위해 result_matrix를 원본 matrix에 저장
    matrix = result_matrix

print(*result)
