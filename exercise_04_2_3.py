# 다음 빈칸을 채워서 numbers 내부에 들어 있는 숫자가 몇 번 등장하는지를 출력하는 코드를 작성.
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

# 나의 답: 딕셔너리.get(키)로 접근.
# for number in numbers:
#     if counter.get(number) == None:
#         counter[number] = 1
#     else:
#         counter[number] += 1

# 해답: if ~ in으로 접근.
for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
    else:
        counter[number] = 1

print(counter)