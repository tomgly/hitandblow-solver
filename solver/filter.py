from .scoring import score

# 候補をフィルタリングする関数
def filter_candidates(candidates, guess, result):
    filtered = []

    # 各候補に対してスコアを計算し、結果と一致するものだけを残す
    for candidate in candidates:
        if score(candidate, guess) == result:
            filtered.append(candidate)

    return filtered