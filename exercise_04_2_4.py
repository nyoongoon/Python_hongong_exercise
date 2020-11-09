# 딕셔너리를 선언합니다.
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

# for 반복문을 사용합니다.
for key in character:
    if type(character[key]) is str:
        print(key , ":", character[key])
    elif type(character[key]) is int:
        print(key , ":", character[key])
    elif type(character[key]) is dict:
        for keys in character[key]:
            print(keys, ":", character[key][keys])
    elif type(character[key]) is list:
        for lists in character[key]:
            print(key, ":", lists)