import random

def User_Input():
  while True:
   a, b, c, d = map(int, input("사용자 입력(ex. 1,2,3,4):").split(','))
   if len(set([a,b,c,d])) == 4:
     break
   print("중복된 값이 있습니다. 다시 입력해주세요") 
  return [a, b, c, d]

def Random_Input():
 random_list = random.sample(range(0, 10),4)
 return random_list

# print("랜덤")

def Process():
    while (not end) and (count != 10):
        display = []
        for position in range(4):
            user_choice = int(input(" "))
            if com_choice.count(user_choice) > 0 and (com_choice[position] == user_choice):
                display.append("B")
            elif com_choice.count(user_choice) > 0:
                display.append("C")
        count += 1

        print("B",display.count("B"), "\nC",display.count("C"))
        if display == ['B', 'B', 'B', 'B']:
            end = True

if __name__ == "__main__":
 User_Input()
 Random_Input()
 Process()


