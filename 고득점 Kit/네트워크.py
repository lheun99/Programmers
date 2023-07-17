def solution(n, computers):
    res = 0
    visited = [False] * n

    def dfs(j):
        visited[j] = True

        for i in range(n):
            if not visited[i] and computers[j][i]:
                dfs(i)

    for j in range(n):
        if not visited[j]:
            dfs(j)
            res += 1

    print(res)


solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
