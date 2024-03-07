# File    :CS112_A1_T2_1_20231019.py
# Purpose :The game is very simple,
#          it is that each player we have the turn comes to him to choose between the number 1 to 10,
#          and then record this number in the total that reaches the number 100 the first is the winner.
# Autor   :Eslam Adel Bayoumi Said
# ID      :20231019


def main():
    
    total =  0
    # welcoming message and displaying status
    print('welcome in game "100 game"')
    
    # Game playing
    while total < 100 :
        # Pleyer 1 gameplay
        while True :
            try:
                move =int(input("player 1 please select number between 1-10 :"))
                 
                if total + move > 100:
                    print("Error: The final total exceeded the maximum 100, please enter a smaller number.")
                    continue
                break
            except ValueError :
                print("please enter a valid number")
                print()

        while move < 1 or move > 10 :
            move =int(input("plarer 1 please select number between 1-10 : "))
            print()
        total += move
        print(f'Now we have   {total}')
        print()
        if total==100:
            print("player 1 is winner")
            break


        # Pleyer 2 gameplay
        while True :
            try :
                move =int(input("player 2 please select number between 1-10 : "))
                
                if total + move > 100:
                    print("Error: The final total exceeded the maximum 100, please enter a smaller number.")
                    print()
                    continue
                break
            except ValueError :
                print("please enter a valid number")
                print()
                
        while move < 1 or move > 10 :
            move =int(input("plarer 2 please select number between 1-10 : "))
            print()
        total += move
        print(f'Now we have   {total}')
        print()
        if total==100:
            print("player 2 is winner")
            break

main()

