num1 = (4, 3, 9 ,8)
num2 = (4, 3, 9, 8)

result = 0
for i in range(4):
    if num1[i] == num2[i]:
        result += 1
    else:
        continue
if result == 4:
    print("정답!")
else:
    print("Bulls : ", result)

result2 = 0
for i in range(4):
    if num2[i] in num1:
        result2 += 1
    else:
        continue
print("Cows : ", result2-result)
