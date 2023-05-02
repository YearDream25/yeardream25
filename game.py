def User_Input():
 a, b, c, d = map(int, input("사용자 입력(ex. 1,2,3,4):").split(',')) 
 return a, b, c, d

def Random_Input():
 print("랜덤")

 
def Process():
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



if __name__ == "__main__":
 User_Input()
 Random_Input()
 Process()


