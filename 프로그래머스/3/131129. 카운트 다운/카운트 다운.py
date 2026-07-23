# DP로 풀이
def solution(target):
    INF = int(1e9)

    dp = [[INF, 0] for _ in range(target + 1)]
    dp[0] = [0, 0]

    scores = []

    # 싱글 1~20
    for number in range(1, 21):
        scores.append((number, 1))

    # 더블과 트리플
    for number in range(1, 21):
        scores.append((number * 2, 0))
        scores.append((number * 3, 0))

    # 불
    scores.append((50, 1))

    for current in range(1, target + 1):
        for score, single_or_bull in scores:

            if current - score < 0:
                continue

            previous = current - score

            dart_count = dp[previous][0] + 1
            count_single_or_bull = (
                dp[previous][1] + single_or_bull
            )

            if dart_count < dp[current][0]:
                dp[current] = [
                    dart_count,
                    count_single_or_bull
                ]

            elif dart_count == dp[current][0]:
                if count_single_or_bull > dp[current][1]:
                    dp[current] = [
                        dart_count,
                        count_single_or_bull
                    ]

    return dp[target]