H, W = map(int, input().split())
s = [[x for x in input()] for i in range(H)]

from collections import deque

def bfs(maze, sh, sw):
    visited = [[0]*W for _ in range(H)]
    queue = deque([[sh, sw, 0]])
    visited[sh][sw] = 1
    maxlen = 0
    while queue:
        h, w , tmplen = queue.pop()
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            temp = tmplen
            new_h, new_w = h+j, w+k
            if new_h < 0 or new_h >= H or \
               new_w < 0 or new_w >= W:
                continue
            elif maze[new_h][new_w] != "#" and \
                 visited[new_h][new_w] == 0:
                visited[new_h][new_w] = 1
                temp += 1
                maxlen = max(maxlen, temp)
                queue.appendleft([new_h, new_w, temp])
    
    return maxlen

res = 0
for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            continue
        res = max(res, bfs(s, i, j))

print(res)
