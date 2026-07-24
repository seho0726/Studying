def solution(edges):
    MAX_NODE = 1_000_000

    indegree = [0] * (MAX_NODE + 1)
    outdegree = [0] * (MAX_NODE + 1)

    max_node = 0

    # 각 정점의 진입 차수와 진출 차수 계산
    for a, b in edges:
        outdegree[a] += 1
        indegree[b] += 1

        max_node = max(max_node, a, b)

    created = 0
    bar = 0
    eight = 0

    for node in range(1, max_node + 1):
        # 생성한 정점
        if indegree[node] == 0 and outdegree[node] >= 2:
            created = node

        # 막대 그래프의 마지막 정점
        elif indegree[node] > 0 and outdegree[node] == 0:
            bar += 1

        # 8자 그래프의 중앙 정점
        elif indegree[node] >= 2 and outdegree[node] == 2:
            eight += 1

    total_graphs = outdegree[created]
    donut = total_graphs - bar - eight

    return [created, donut, bar, eight]