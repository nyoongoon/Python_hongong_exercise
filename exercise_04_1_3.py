numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number / 2 == 0:
        print("{}는 짝수입니다".format(number))
    else:
        print("{}는 홀수입니다".format(number))

    # if 1000 > number >= 100:
    #     print("{}는 3자릿수입니다".format(number))
    # elif number >= 10:
    #     print("{}는 2자릿수입니다".format(number))
    # elif number > 0:
    #     print("{}는 1자릿수입니다".format(number))

for number in numbers:
    print(number, "는", len(str(number)), "자릿수입니다")
    # str()로 문자열 변환 후, len()로 길이 계산