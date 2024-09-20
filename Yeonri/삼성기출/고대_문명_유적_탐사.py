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

DXY = [(1, 0), (0, 1), (0, -1)]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def chk_spin(matrix, lst, spin_count, x, y):
    # 처음 유물 체크
    # 방향 회전
    # 유물 체크

    # return (회전 값, 최종 값)

    pass

def chk_number(matrix):
    visited = defaultdict(list)

    # 각 번호에 대한 값을 저장하도록 만든다.
    # 탐색을 전체 값에 대해 하지 않고, 회전한 값들에 대해서만 탐색을 하도록 만든다.
    # 모든 방향에 대해서 탐색을 진행하도록 한다.

    # 탐색을 줄이기 위한 위의 방식에 대한 엣지 케이스
    # 만약에 회전을 하지 않는 부분에 연결이 되어있는 케이스는 탐색을 하지 못한다.

    # 따라서 모든 좌표를 탐색하도록 설정을 먼저 해본다.

    for i in range(N):
        for j in range(N):
            s_x, s_y = (i, j)

            queue = deque([(s_x, s_y)])

            tmp_dir = set()
            tmp_dir.add((s_x, s_y))

            count = 1

            while queue:

                x, y = queue.popleft()

                for dx, dy in DXY:
                    nx, ny = x + dx, y + dy

                    if not is_valid(nx, ny): continue
                    if matrix[x][y] != matrix[nx][ny]: continue

                    tmp_dir.add((nx, ny))
                    count += 1
                    queue.append((nx, ny))

            if count >= 3:
                if matrix[x][y] not in visited:
                    visited[matrix[x][y]].append((count, tmp_dir))

                else:
                    tmp_count, _ = visited[matrix[x][y]]
                    if tmp_count < count:
                        visited[matrix[x][y]] = [(count, tmp_dir)]



N = 5 # 매트릭스 크기
S = 3 # 회전 크기

K, M = map(int, input().split())
matrix = [list(map(int, input().split()))for _ in range(N)]
pre_number = deque(list(map(int, input().split())))

result = {} # (번호, 회전수, 최종 값)

count = 0

for j in range(1,N-1):
    for i in range(1,N-1):
        for k in range(3):

            tmp_matrix = deepcopy(matrix)
            tmp_number = pre_number[:]

            # 매트릭스, 유물 번호, 회전 값, x, y
            # chk_spin()
            result.add((count, chk_spin(matrix, tmp_number, k, i, j)))

            # 최대 값이 같을 때, count를 기준으로 순서를 체크한다.
            count += 1
