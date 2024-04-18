import re

def normalize_input(input_string):
    # 文字列を正規化するために、全角スペースを半角に変換し、不要なスペースを削除します。
    normalized = re.sub(r'\s+', ' ', input_string.strip())
    # 日本語の表記ゆれをなるべく排除するため、カンマやピリオドなども削除します。
    normalized = re.sub(r'[,.、。]', '', normalized)
    return normalized

def score_response_flexible(user_input):
    # ユーザーの入力を正規化
    normalized_input = normalize_input(user_input)
    # 各キーワードの可能な表記を含むパターン
    sakura_patterns = r'(桜|さくら|サクラ)'
    neko_patterns = r'(猫|ねこ|ネコ)'
    densha_patterns = r'(電車|でんしゃ|デンシャ)'
    
    # 正しい順序で単語が含まれているかをチェックするためのパターン
    full_pattern = f'{sakura_patterns}.*{neko_patterns}.*{densha_patterns}'
    
    # パターンに一致すればそれぞれの単語につき1点ずつ計算
    if re.search(full_pattern, normalized_input):
        return 3  # 全ての単語が正しい順序であれば3点
    else:
        # それぞれの単語が存在するかチェックして点数を計算
        score = 0
        patterns = [sakura_patterns, neko_patterns, densha_patterns]
        for pattern in patterns:
            if re.search(pattern, normalized_input):
                score += 1
        return score

# テスト入力例
test_input_13 = "さくら、ねこ、デンシャ"
test_input_14 = "サクラを見た後、ネコと遊んだ。最後にでんしゃを見た。"
test_input_15 = "電車と桜"
test_input_16 = "さくらと猫"

# テスト実行
test_scores_flexible = {
    "test_input_13": score_response_flexible(test_input_13),
    "test_input_14": score_response_flexible(test_input_14),
    "test_input_15": score_response_flexible(test_input_15),
    "test_input_16": score_response_flexible(test_input_16)
}

test_scores_flexible
