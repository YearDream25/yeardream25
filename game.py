def User_Input():
 #사용자 입력
 print("사용자 입력")


def Random_Input():
 print("랜덤")

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

        print(display)
        print("B",display.count("B"), "\nC",display.count("C"))
        if display == ['B', 'B', 'B', 'B']:
            end = True

if __name__ == "__main__":
 User_Input()
 Random_Input()
 Process()


