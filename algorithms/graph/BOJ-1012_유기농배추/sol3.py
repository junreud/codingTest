import sys
input = sys.stdin.readline

def dfs_iterative(field, start_x, start_y, M, N):
    """스택을 사용한 반복적 DFS - 재귀 깊이 제한 문제 해결"""
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    stack = [(start_x, start_y)]
    
    while stack:
        x, y = stack.pop()
        
        # 이미 방문했거나 범위를 벗어났으면 건너뛰기
        if x < 0 or x >= N or y < 0 or y >= M or field[x][y] == 0:
            continue
            
        field[x][y] = 0  # 방문 처리
        
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1:
                stack.append((nx, ny))

T = int(input())  # 테스트 케이스 수

for _ in range(T):  # 각 테스트 케이스마다 처리
    M, N, K = map(int, input().split())  # M은 가로길이(열), N은 세로길이(행)
    field = [[0] * M for _ in range(N)]  # N개 행, M개 열
    
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1  # x는 열(가로), y는 행(세로) → field[행][열]
    
    result = 0
    for i in range(N):  # N개 행
        for j in range(M):  # M개 열
            if field[i][j] == 1:  # 배추가 있을 때만 DFS 실행
                dfs_iterative(field, i, j, M, N)
                result += 1
    
    print(result)