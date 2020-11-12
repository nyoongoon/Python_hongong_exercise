def flatten(data):
    output = [] # flatten함수를 호출할 때 output 함수 재선언 하는것이 아님!
    for item in data:
        if type(item) == list:
            output += flatten(data) # 리스트간의 대입 연산자를 활용 !!!
        else:
            output.append(item)
    return output

example = [[1, 2, 3], [4,[5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))