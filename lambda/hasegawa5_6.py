import random

# 数字から漢数字への変換辞書
kanji_digits = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九'}

def convert_to_kanji(number):
    return ''.join(kanji_digits[int(digit)] for digit in str(number))

def generate_random_kanji(digits):
    number = random.randint(10**(digits-1), 10**digits - 1)
    return convert_to_kanji(number)

def extract_kanji(input_str):
    # 入力文字列から漢数字のみを抜き出して文字列として返す
    return ''.join(char for char in input_str if char.isdigit() or char in ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十'])

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


import random

def subtract_from_100(number, subtrahend):
    expected_first_answer = str(100 - subtrahend)
    first_ans = number if expected_first_answer in number else None
    if first_ans:
        second_subtrahend = random.randint(1, 9)
        expected_second_answer = str(100 - subtrahend - second_subtrahend)
        input_string2 = input(f"それからまた{second_subtrahend}を引くと？: ")
        second_ans = input_string2 if expected_second_answer in input_string2 else None
        if second_ans:
            return 2
        else:
            return 1
    else:
        return 0

subtrahend = random.randint(1, 9)
input_string = input(f"100-{subtrahend} は？: ")
point_6 = subtract_from_100(input_string, subtrahend)
print(point_6)
