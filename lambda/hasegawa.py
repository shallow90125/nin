import re

##############################
## 長谷川式認知症判定法　問１ ##
##############################

def normalize_input(input_string):
    # 入力を正規化する: 不要なスペースを削除し、数字だけに絞る
    normalized = re.sub(r'\s+', '', input_string)  # スペースを削除
    normalized = re.sub(r'[^\d]', '', normalized)  # 数字以外を削除
    return normalized

def q1(user_input, correct_age=65):
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
    
##############################
## 長谷川式認知症判定法　問2  ##
##############################

# 正規表現を使って日付の情報を抽出しやすくするための関数
def normalize_input(input_string):
    # 入力を正規化する: 不要なスペースと句読点を削除
    normalized = re.sub(r'\s+', ' ', input_string.strip())
    normalized = re.sub(r'[,.、。]', '', normalized)
    return normalized

# 日付情報を受け取り、それに基づいてユーザーの回答を評価する関数
def q2(correct_date):
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

###############################
## 長谷川式認知症判定法　問4&7 ##
###############################

def normalize_input(input_string):
    # 文字列を正規化するため、全角スペースを半角に変換し、不要なスペースを削除
    normalized = re.sub(r'\s+', ' ', input_string.strip())
    # 日本語の表記ゆれをなるべく排除するため、カンマやピリオドなども削除
    normalized = re.sub(r'[,.、。]', '', normalized)
    return normalized

def q4_7(user_input):
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
    
##############################
## 長谷川式認知症判定法　問5  ##
##############################

def q5(number):
    first_ans = number if '九十三' in number else None
    if first_ans:
        input_string2 = input("それからまた7を引くと？: ")
        second_ans = input_string2 if '八十六' in input_string2 else None
        if second_ans:
            return 2
        else:
            return 1
    else:
        return 0
    
##############################
## 長谷川式認知症判定法　問6  ##
##############################

def extract_kanji(input_str):
    # 入力文字列から漢数字のみを抜き出して文字列として返す
    return ''.join(char for char in input_str if char.isdigit() or char in ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十'])

def q6():
    # 3桁逆唱
    number_3digit = "六八二"
    number_ans = input("6-8-2を逆から言ってください: ")
    
   

    number_ans = extract_kanji(number_ans)
    if number_3digit == number_ans[::-1]:
        # 4桁逆唱
        number_4digit = "三五二九"
        number_ans2 = input("3-5-2-9を逆から言ってください: ")

        number_ans2 = extract_kanji(number_ans2)
        if number_4digit == number_ans2[::-1]:
            return 2  # 4桁逆唱成功
        else:
            return 1  # 4桁逆唱失敗
    else:
        return 0  # 3桁逆唱失敗
    
##############################
## 長谷川式認知症判定法　問9  ##
##############################

def q9(user_input_text):
    # 一般的な野菜のリスト（ひらがな、カタカナ、漢字で表記）
    vegetables = ['トマト', 'きゅうり', 'キュウリ', '胡瓜', 'にんじん', 'ニンジン', '人参',
                'じゃがいも', 'ジャガイモ', '馬鈴薯', 'ほうれん草', 'ホウレンソウ', '菠薐草',
                'なす', 'ナス', '茄子']
    
    # テキストを正規化（全角・半角、大文字・小文字）
    normalized_text = re.sub(r'\s+', ' ', user_input_text.strip().lower())
    
    # 野菜のカウント
    vegetable_count = 0
    for veg in vegetables:
        # 各野菜の出現回数をカウント（大文字・小文字を無視するために全て小文字に変換）
        veg_pattern = re.compile(re.escape(veg.lower()), re.IGNORECASE)
        vegetable_count += len(veg_pattern.findall(normalized_text))
    
    return vegetable_count

# テスト入力例
test_text = "今日の市場には新鮮なトマト、キュウリ、そしてジャガイモがたくさんありました。また、ホウレンソウとナスも買いました。"

# テスト実行
vegetable_count = count_vegetables_in_text(test_text)
vegetable_count

def q9_gpt(user_input_text):
    
    # APIキーを設定
    openai.api_key = 'your-api-key'

    # GPT-3を使用して文章中の野菜の数をカウント
    prompt = f"以下の文章に含まれる野菜の数を数えてください。数字だけで回答してください。\n'{user_input_text}'"
    response = openai.ChatCompletion.create(
                        model = "gpt-3.5-turbo-16k-0613",
                        messages = [
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0
                    )

    score = int(response['choices'][0]['text'].strip())
    return score