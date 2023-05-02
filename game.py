import random

def User_Input():
 #사용자 입력
 print("사용자 입력")


def Random_Input():
 random_list = random.sample(range(0, 10),4)
 return random_list
 return random_list

# print("랜덤")

def Process():
 print("처리")

if __name__ == "__main__":
 User_Input()
 Random_Input()
 Process()


