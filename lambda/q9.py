import re
import openai

def count_vegetables_in_text(user_input_text):
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

def count_vegetable_gpt(user_input_text):
    
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

    print(response['choices'][0]['text'].strip())
