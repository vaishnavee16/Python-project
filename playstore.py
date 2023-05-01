print("Welcome to the Playstore!")
signUp_details = {"Name": [], "Username": [], "Password":[]}
def sign_up():
    name = input("Enter your name: ")
    signUp_details["Name"].append(name)
    username = input("Enter email-id: ")
    signUp_details["Username"].append(username)
    password = input("Enter password: ")
    signUp_details["Password"].append(password)
    print("Login")
    sign_in()
def sign_in():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
   
    if username in signUp_details["Username"]:
        index = signUp_details["Username"].index(username)
        if signUp_details["Password"][index] == password:
            print("Login Successful")
            game()
        else:
            print("Invalid Password")
    else:
        print("Username not found")


def game():
    
    print("1:Stone Paper and Scissior:")
    print("2-Scrapping")
    print("3-quiz")
    print("4-hangman")
    print("5-tic tac toe")
    print("6-snake-leader")
    print("7-blackjack")
    choose=int(input("Choose the game you want to play "))
    while True:
        if choose==1:
        
            import random 
            #import string
            user_chance=input('Enter your option from [rock,paper,scissor]:')
            entrys=['rock','paper','scissor']
            computer_chance=random.choice(entrys)
            print(f"\nI chose {user_chance}, computer chose {computer_chance}\n")
            
            if user_chance==computer_chance:
                print("Game is tie")
            elif user_chance=='rock' and computer_chance=='paper':
                print("computer's win")
            elif user_chance=='paper' and computer_chance=='scissor':
                print("computer's win")
            elif user_chance=='scissor' and computer_chance=='rock':
                print("computer's win")
            else:
                if user_chance=='paper' and computer_chance=='rock':
                    print('you win')
                elif user_chance=='scissor' and computer_chance=='paper':
                    print('you win')
                elif user_chance=='rock' and computer_chance=='scissor':
                    print('you win')
            play_again = input("Do you want to play again? (y/n) ").lower()
            if play_again != "y":
                break
        if choose==2:
            import pandas as pd
            url ='https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
            data=pd.read_html(url)
            type(data)
            len(data)
            
            print(data[1].loc[:,["State","Administrative/Executive capital"]])
            play_again = input("Do you want to play again? (y/n) ").lower()
            if play_again != "y":
                break
        if choose==3:
            import quiz
            quiz.quiz()
        if choose==4:
            import Hangman
            Hangman.hang_man()
        if choose==5:
            import Tic_tac_toe
            Tic_tac_toe.tic_tac_toe()
        if choose==6:
            import Snake_ladder
            Snake_ladder.snake_ladder()
        if choose==7:
            import Blackjack
            Blackjack.black_jack()
            break
print("\nMENU")
print("1. Sign in")
print("2. Sign up")
print("3. Exit!")
choice = int(input("Enter your choice: "))
if choice == 1:
    while True:
        sign_in()
elif choice == 2:

        sign_up()
elif choice == 3:
    print("Goodbye!")
else:
    print("Invalid choice")