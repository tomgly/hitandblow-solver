from .scoring import score

# 残り候補から次の最強手を提案する関数
def suggest_best_guess(candidates: list[str]) -> str:
    best_guess = None
    best_score = float('inf')

    # 各候補に対して、結果の分布を計算
    for guess in candidates:
        # scoreごとに候補がいくつ残るか
        distribution = {}
        for candidate in candidates:
            r = score(candidate, guess)
            if r not in distribution:
                distribution[r] = 0
            distribution[r] += 1

        # この予想の最大グループサイズ
        worst_case = max(distribution.values())
        
        # worst_case が小さい予想を優先
        if worst_case < best_score:
            best_score = worst_case
            best_guess = guess

    return best_guess