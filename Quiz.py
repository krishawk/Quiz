# We have to first think of questions to ask the user
# we ask the user to select YES or No

question_1 = input("Does a dog bark?" + " " "Select YES or NO: ")

question_2 = input("Does a chicken lay eggs?" + " " "Select YES or NO: ")

question_3 = input("Can all birds fly?" + " " "Select YES or NO: ")

# Now the computer lets you know how you did
if question_1 == 'NO':
    print("You got question 1 WRONG!")
if question_2 == 'NO':
    print("You got question 2 WRONG!")
if question_3 == 'YES':
    print("You got question 3 WRONG!")
else:
    print("YOU GOT THEM ALL RIGHT!! CONGRATS!!!!")

