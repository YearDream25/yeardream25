def User_Input():
 a, b, c, d = map(int, input("사용자 입력(ex. 1,2,3,4):").split(',')) 
 return a, b, c, d

def Random_Input():
 print("랜덤")

def Process():
 print("처리")

if __name__ == "__main__":
 User_Input()
 Random_Input()
 Process()


