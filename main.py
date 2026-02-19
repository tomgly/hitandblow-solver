from solver.config import COLORS, CODE_LEN
from solver.generator import generate_all_codes
from solver.filter import filter_candidates
from solver.strategy import suggest_best_guess

def main():
    # すべてのコードを生成  
    candidates = generate_all_codes()

    while True:
        # 残り候補数を表示
        print(f"残り候補数: {len(candidates)}")

        # ユーザーからの入力を受け取る
        while True:
            guess = input("guess (例: BRYG): ").strip().upper()
            if len(guess) != CODE_LEN or any(c not in COLORS for c in guess):
                print(f"入力は {CODE_LEN} 文字で {COLORS} のみを使ってください")
                continue
            break

        while True:
            try:
                result = input("result (例: 21): ").strip()
                if len(result) != 2 or not result.isdigit():
                    raise ValueError
                hit, blow = int(result[0]), int(result[1])
                if hit + blow > CODE_LEN:
                    raise ValueError
                break
            except ValueError:
                print(f"入力は2桁の数字で、{hit} + {blow} <= {CODE_LEN} にしてください")

        # 候補をフィルタリング
        candidates = filter_candidates(candidates, guess, result)
        if len(candidates) == 0:
            print("矛盾する入力があり、候補がなくなりました。最初からやり直してください。")
            break

        # 候補が1つ以下になったら終了
        if len(candidates) == 1:
            print("正解:", candidates[0])
            break
        else:
            # 次の推測を提案
            guess = suggest_best_guess(candidates)
            print(f"次の推測: {guess}")

if __name__ == "__main__":
    main()