import random

# 数字から漢数字への変換辞書
kanji_digits = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九'}
kanji_to_digit = {v: k for k, v in kanji_digits.items()}

def convert_to_kanji(number):
    return ''.join(kanji_digits[int(digit)] for digit in str(number))

def generate_random_kanji(digits):
    number = random.randint(10**(digits-1), 10**digits - 1)
    return convert_to_kanji(number)

def extract_kanji(input_str):
    # 入力文字列から漢数字のみを抜き出して文字列として返す
    return ''.join(char for char in input_str if char in kanji_to_digit)

def kanji_to_number(kanji_str):
    return int(''.join(str(kanji_to_digit[char]) for char in kanji_str))

def reverse_counting():
    # ランダムな3桁の数字を生成
    number_3digit = generate_random_kanji(3)
    print(f"数字: {number_3digit}")
    number_ans = input(f"{number_3digit}を逆から言ってください: ")

    number_ans = extract_kanji(number_ans)
    if number_3digit == number_ans[::-1]:
        # ランダムな4桁の数字を生成
        number_4digit = generate_random_kanji(4)
        print(f"数字: {number_4digit}")
        number_ans2 = input(f"{number_4digit}を逆から言ってください: ")

        number_ans2 = extract_kanji(number_ans2)
        if number_4digit == number_ans2[::-1]:
            return 2  # 4桁逆唱成功
        else:
            return 1  # 4桁逆唱失敗
    else:
        return 0  # 3桁逆唱失敗

# テスト
point_5 = reverse_counting()
print(point_5)



def subtract_from_100():
    subtrahend = random.randint(1, 9)
    expected_first_answer = 100 - subtrahend
    print(f"百-{convert_to_kanji(subtrahend)} は？: ", end="")
    input_string = input()
    input_number = kanji_to_number(extract_kanji(input_string))
    
    if expected_first_answer == input_number:
        second_subtrahend = random.randint(1, 9)
        expected_second_answer = expected_first_answer - second_subtrahend
        print(f"それからまた{convert_to_kanji(second_subtrahend)}を引くと？: ", end="")
        input_string2 = input()
        input_number2 = kanji_to_number(extract_kanji(input_string2))
        
        if expected_second_answer == input_number2:
            return 2  # 両方の引き算が正解
        else:
            return 1  # 最初の引き算は正解、次は不正解
    else:
        return 0  # 最初の引き算が不正解

# テストの実行
point_6 = subtract_from_100()
print(point_6)
