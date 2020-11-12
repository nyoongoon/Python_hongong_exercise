count = 0
datas = []

def flatten(data):

    while(data):
        if type(data[0]) is list:
            flatten(data[0])
        else:
            del data[0]
            datas.append(data[0])
    return datas





example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))