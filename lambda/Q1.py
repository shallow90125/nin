import re

def normalize_input(input_string):
    # 入力を正規化する: 不要なスペースを削除し、数字だけに絞る
    normalized = re.sub(r'\s+', '', input_string)  # スペースを削除
    normalized = re.sub(r'[^\d]', '', normalized)  # 数字以外を削除
    return normalized

def score_age_guess(user_input, correct_age=65):
    # ユーザーの入力を正規化
    normalized_input = normalize_input(user_input)
    
    # 正規化した入力が数字かどうかをチェックし、数字なら年齢を比較
    if normalized_input.isdigit():
        guessed_age = int(normalized_input)
        if guessed_age == correct_age:
            return 1  # 正解の場合は1点
        else:
            return 0  # 不正解の場合は0点
    else:
        return 0  # 入力が数字でない場合も0点

# テストケース
test_inputs = [
    "私は65歳です。",
    "私の年齢は64です",
    "68",
    "sixty-five",
    " 65 "
]

# テスト実行
test_scores = {input_text: score_age_guess(input_text) for input_text in test_inputs}

# 結果表示
test_scores
