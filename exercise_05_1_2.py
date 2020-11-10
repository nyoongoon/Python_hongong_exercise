def mul(*values):
    result = 1
    for i in range(len(values)):
        result *= values[i]
    return result

# 함수를 호출합니다.
print(mul(5, 7, 9, 10))