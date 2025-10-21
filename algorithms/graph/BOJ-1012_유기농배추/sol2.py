import sys
input = sys.stdin.readline

def dfs(field, x, y, M, N):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    field[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1:  # N은 행 개수, M은 열 개수
            dfs(field, nx, ny, M, N)

T = int(input())  # 테스트 케이스 수

for _ in range(T):  # 각 테스트 케이스마다 처리
    M, N, K = map(int, input().split())  # M은 가로길이(열), N은 세로길이(행)
    field = [[0] * M for _ in range(N)]  # N개 행, M개 열로 수정
    
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1  # x는 열(가로), y는 행(세로) → field[행][열]
    
    result = 0
    for i in range(N):  # N개 행
        for j in range(M):  # M개 열
            if field[i][j] == 1:  # 배추가 있을 때만 DFS 실행
                dfs(field, i, j, M, N)
                result += 1
    
    print(result)