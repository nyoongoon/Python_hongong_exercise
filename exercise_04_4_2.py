output = [i for i in range(1, 101) if "{:b}".format(i).count("0") == 1]
# i를 2진수로 바꾸었다가 다시 10진수로 바꾸었었는데, 그냥 i사용하면 됌.
for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))

print("합계:", sum(output))