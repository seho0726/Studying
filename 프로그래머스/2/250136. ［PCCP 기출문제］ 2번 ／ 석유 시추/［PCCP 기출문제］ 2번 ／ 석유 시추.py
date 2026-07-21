# BFS 사용
from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    visited = [[False] * m for _ in range(n)]
    
    # 얻을 수 있는 석유량
    oil_by_column = [0] * m
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def bfs(start_row, start_col):
        queue = deque([(start_row, start_col)])
        visited[start_row][start_col] = True
        
        oil_size = 0
        columns = set()
        
        while queue:
            row, col = queue.popleft()
            
            oil_size += 1
            columns.add(col)
            
            for i in range(4):
                next_row = row + dr[i]
                next_col = col + dc[i]
                
                # 격자 범위 체크
                if 0 <= next_row < n and 0 <= next_col < m:
                    # 석유이면서 아직 방문하지 않은 칸
                    if land[next_row][next_col] == 1 and not visited[next_row][next_col]:
                        visited[next_row][next_col] = True
                        queue.append((next_row, next_col))
                        
        return oil_size, columns
        
    for row in range(n):
        for col in range(m):
            if land[row][col] == 1 and not visited[row][col]:
                oil_size, columns = bfs(row, col)

                for column in columns:
                    oil_by_column[column] += oil_size
        
    return max(oil_by_column)