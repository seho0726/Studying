def solution(info, n, m):
    INF = float("inf")

    # dp[b] = B 흔적이 b일 때 A 흔적의 최솟값
    dp = [INF] * m
    dp[0] = 0

    for a_trace, b_trace in info:
        next_dp = [INF] * m

        for b in range(m):
            # 현재 상태가 불가능한 상태라면 건너뜀
            if dp[b] == INF:
                continue

            # 1. 현재 물건을 A가 훔치는 경우
            new_a = dp[b] + a_trace

            if new_a < n:
                next_dp[b] = min(next_dp[b], new_a)

            # 2. 현재 물건을 B가 훔치는 경우
            new_b = b + b_trace

            if new_b < m:
                next_dp[new_b] = min(
                    next_dp[new_b],
                    dp[b]
                )

        dp = next_dp

    answer = min(dp)

    if answer == INF:
        return -1

    return answer