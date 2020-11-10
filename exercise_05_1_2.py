def mul(*values):
    result = 1
    for value in values:
        # 가변 매개변수는 리스트처럼 사용!
        result *= value
    return result

# 함수를 호출합니다.
print(mul(5, 7, 9, 10))