import re
import openai

# 正規表現を使って日付の情報を抽出しやすくするための関数
def normalize_input(input_string):
    # 入力を正規化する: 不要なスペースと句読点を削除
    normalized = re.sub(r'\s+', ' ', input_string.strip())
    normalized = re.sub(r'[,.、。]', '', normalized)
    return normalized

# 日付情報を受け取り、それに基づいてユーザーの回答を評価する関数
def quiz_date_info(correct_date):
    year, month, day, weekday = correct_date
    score = 0

    # ユーザーに年を尋ねる
    user_response_year = normalize_input(input(f"何年ですか？"))
    if user_response_year.isdigit() and int(user_response_year) == year:
        score += 1

    # ユーザーに月を尋ねる
    user_response_month = normalize_input(input(f"何月ですか？"))
    if user_response_month.isdigit() and int(user_response_month) == month:
        score += 1

    # ユーザーに日を尋ねる
    user_response_day = normalize_input(input(f"何日ですか？"))
    if user_response_day.isdigit() and int(user_response_day) == day:
        score += 1

    # ユーザーに曜日を尋ねる
    user_response_weekday = normalize_input(input(f"何曜日ですか？"))
    if user_response_weekday.lower() == weekday.lower():
        score += 1

    return score

# 正しい日付をタプル形式で設定
correct_date = (2024, 4, 15, "月曜日")  # 例として2024年4月15日月曜日を使用

# クイズを実行し、スコアを得る
total_score = quiz_date_info(correct_date)
print(f"あなたのスコアは {total_score} 点です。")
