pets = [{"name": "구름", "age": 5},
        {"name": "초코", "age": 3},
        {"name": "아지", "age": 1},
        {"name": "호랑이", "age": 1}
        ]
print("# 우리 동네 애완 동물들")
# for number in pets:
#     for key in number:
#         print(key, ":", number[key])

for number in pets:
    print(number["name"], str(number["age"])+"살")
# 각 리스트의
# name의 값과 age의 값을 출력,
# age는 문자열로 변환해서 "살"과 문자열 연결 연산자(+) 사용
# 문자열 연결 연산자 사용하지 않으면 자동으로 띄여쓰기 됌!