def User_Input():
 #사용자 입력
 print("사용자 입력")


def Random_Input():
 print("랜덤")

def Process():
 print("처리")
 import random

 random_list = [1, 2, 4, 3]
 user_num = [0, 1, 7 , 3]

 bull_num = 0
 cow_num = 0
 for i in range(0, 4):
     if random_list.count(user_num[i]):
         cow_num += 1

     if random_list[i] == user_num[i]:
         bull_num += 1
 print('cow_num = ',cow_num)
 print('bull_num = ',bull_num)

if __name__ == "__main__":
 User_Input()
 Random_Input()
 Process()


