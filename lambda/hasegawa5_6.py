#長谷川式➄
def subtract_from_100(number):
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

input_string = input("100-7 は？: ")
point = subtract_from_100(input_string)
print(point)



#長谷川式➅
def extract_kanji(input_str):
    # 入力文字列から漢数字のみを抜き出して文字列として返す
    return ''.join(char for char in input_str if char.isdigit() or char in ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十'])

def reverse_counting():
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

# テスト
point = reverse_counting()
print(point)


# #長谷川式➅
# def reverse_counting():
#     # 3桁逆唱
#     number_3digit = [6,8,2]
#     number_ans = input("6-8-2桁の数字を逆から言ってください: ")
#     if number_3digit == number_ans[::-1]:
#         # 4桁逆唱
#         number_4digit = [3,5,2,9]
#         number_ans2 = input("3-5-2-9桁の数字を逆から言ってください: ")
#         if number_4digit == number_ans2[::-1]:
#             return 2  # 4桁逆唱成功
#         else:
#             return 1  # 4桁逆唱失敗
#     else:
#         return 0  # 3桁逆唱失敗

# # テスト
# reverse_counting()
