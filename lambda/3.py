import re

# 正規表現を使って入力を正規化するための関数
def normalize_input(input_string):
    # 入力を正規化する: 不要なスペースと句読点を削除
    normalized = re.sub(r'\s+', ' ', input_string.strip())
    normalized = re.sub(r'[,.、。]', '', normalized)
    return normalized

# 現在地情報を受け取り、それに基づいてユーザーの回答を評価する関数
def quiz_location_info(correct_location):
    prefecture, city = correct_location
    score = 0

    # ユーザーに都道府県を尋ねる
    user_response_prefecture = normalize_input(input(f"都道府県はどこですか？"))
    if user_response_prefecture == prefecture:
        score += 1

    # ユーザーに市町村を尋ねる
    user_response_city = normalize_input(input(f"市町村はどこですか？"))
    if user_response_city == city:
        score += 1

    return score

# 正しい場所をタプル形式で設定
correct_location = ("大阪府", "大阪市")  # 例として大阪府大阪市を使用

# クイズを実行し、スコアを得る
total_score = quiz_location_info(correct_location)
print(f"あなたのスコアは {total_score} 点です。")
