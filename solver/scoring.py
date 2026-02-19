# ヒットとブローのスコアを計算する関数
def score(secret: str, guess: str) -> int:
    hits = sum(s == g for s, g in zip(secret, guess))
    blows = sum(min(secret.count(c), guess.count(c)) for c in set(guess)) - hits
    
    return hits * 10 + blows