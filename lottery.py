'''
    Lottery
'''


print("#"*40)
print("Excercise 12")
lucky_num = 12
user_num = 0
user_num = input("Give it first try: ")
iterator = 0
while iterator < 5:
    if abs(int(lucky_num) -  int(user_num)) < 3 and int(lucky_num) !=  int(user_num) :
        user_num = input("Dood . Yo Almost There !!. Just Try Once Again: ")

    elif int(lucky_num) > int(user_num):
        user_num = input("Hmm :( Too Low ! Try Again: ")

    elif int(lucky_num) < int(user_num):
        user_num = input("Woah ! That's too high. Try again: ")

    else:
        print("Bingo !! Yo Got it right !! There you go. IT IS - ",lucky_num)
        break

    iterator += 1

else:
    print("You missed chances")
        


