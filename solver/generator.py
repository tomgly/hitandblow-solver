from .config import COLORS
from itertools import product

# すべてのコードを生成する関数
def generate_all_codes() -> list[str]:
    all_codes = []
    for code in product(COLORS, repeat=4):
        all_codes.append("".join(code))
    
    return all_codes