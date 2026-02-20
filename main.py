from solver.config import COLORS, CODE_LEN, MANUAL_INPUT
from solver.generator import generate_all_codes
from solver.filter import filter_candidates
from solver.strategy import suggest_best_guess

def main():
    # すべてのコードを生成  
    candidates = generate_all_codes()

    guess = None

    while True:
        try:
            # 残り候補数を表示
            print(f"残り候補数: {len(candidates)}")

            # ユーザーからの入力を受け取る
            if guess is None:
                while True:
                    guess = input("推測: ").strip().upper()
                    if len(guess) != CODE_LEN or any(c not in COLORS for c in guess):
                        print(f"入力は {CODE_LEN} 文字で {COLORS} のみを使ってください")
                        continue
                    break

            while True:
                try:
                    hit = input("ヒット: ").strip()
                    blow = input("ブロー: ").strip()
                    if len(hit) != 1 or not hit.isdigit() or len(blow) != 1 or not blow.isdigit():
                        raise ValueError
                    hit, blow = int(hit), int(blow)
                    if hit + blow > CODE_LEN:
                        raise ValueError
                    break
                except ValueError:
                    print(f"ヒットとブローは0-{CODE_LEN}の数字で、合計{CODE_LEN}以下で入力してください")

            # 候補をフィルタリング
            candidates = filter_candidates(candidates, guess, hit, blow)
            if len(candidates) == 0:
                print("矛盾する入力があり、候補がなくなりました。")
                break

            # 候補が1つ以下になったら終了
            if len(candidates) == 1:
                print("正解: ", candidates[0])
                break

            # 次の推測を提案
            suggest = suggest_best_guess(candidates)
            print(f"次の推測: {suggest}\n")
            if not MANUAL_INPUT:
                guess = suggest
            else:
                guess = None

        except KeyboardInterrupt:
            print("\n終了します。")
            break

if __name__ == "__main__":
    main()