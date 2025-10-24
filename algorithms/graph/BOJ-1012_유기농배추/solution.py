import sys
from collections import deque

input = sys.stdin.readline

def dfs(field, x, y, M, N):
    """DFS로 연결된 배추들 모두 방문"""
    # 방향 벡터: 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]  # x(행)의 변화량 - 세로 움직임
    dy = [0, 0, -1, 1]  # y(열)의 변화량 - 가로 움직임
    
    # 현재 위치 방문 표시
    field[x][y] = 0
    
    # 4방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 범위 체크 및 배추 확인
        if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1:
            dfs(field, nx, ny, M, N)

def bfs(field, start_x, start_y, M, N):
    """BFS로 연결된 배추들 모두 방문"""
    # 방향 벡터: 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(start_x, start_y)])
    field[start_x][start_y] = 0  # 방문 표시
    
    while queue:
        x, y = queue.popleft()
        
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 체크 및 배추 확인
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1:
                field[nx][ny] = 0  # 방문 표시
                queue.append((nx, ny))

def stack_dfs(field, start_x, start_y, M, N):
    """스택을 이용한 반복적 DFS"""
    # 방향 벡터: 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    stack = [(start_x, start_y)]
    field[start_x][start_y] = 0  # 방문 표시
    
    while stack:
        x, y = stack.pop()
        
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 체크 및 배추 확인
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1:
                field[nx][ny] = 0  # 방문 표시
                stack.append((nx, ny))

def solve():
    """메인 해결 함수"""
    T = int(input())  # 테스트 케이스 수
    
    for _ in range(T):
        M, N, K = map(int, input().split())
        
        # 배추밭 초기화 (M x N)
        field = [[0] * M for _ in range(N)]
        
        # 배추 위치 입력
        for _ in range(K):
            x, y = map(int, input().split())
            field[y][x] += 1
        
        # 연결 요소 개수 세기
        worm_count = 0

        for i in range(N):
            for j in range(M):
                if field[i][j] == 1:  # 아직 방문하지 않은 배추 발견
                    # DFS 또는 BFS로 연결된 배추들 모두 방문
                    # dfs(field, i, j, M, N)
                    bfs(field, i, j, M, N)  # BFS 사용으로 변경
                    worm_count += 1
        
        print(worm_count)

# 실행
solve()
