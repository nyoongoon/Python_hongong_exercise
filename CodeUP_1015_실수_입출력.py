# a = float(input())
# print(round("%f" % a, 3)) # 끝자리가 0이면 출력을 하지 않는다.

# format()함수 사용!
a = float(input())
print(format(a, ".2f"))