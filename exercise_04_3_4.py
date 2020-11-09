max_value = 0
a = 0
b = 0

for i in range(99+1):
    j = 100 - i
    if(max_value<=i*j):
        max_value = i*j
        a = i
        b = j

    #최댓값 구하기


print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))