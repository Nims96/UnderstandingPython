a= "Welcome to the game"
b= a.center(75)
c= "\n\n\tDefeat your enemy by reducing their life to 0 or they cannot draw. \n\t\t\tEnter a number to move to phase\n"
print("\n" + b + c)

print("Player 1 Begin")





def loop_player():
    print("\n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn")
    player_choice= int(input("Pick the phase you would like to go to "))
    deployment1_passed = False
    combat_passed = False
    deployment2_passed = False
    end_turn = False
    while player_choice <= 4 and player_choice >= 1:
        if player_choice <= 4 and player_choice >= 1:
            while player_choice <= 4 and player_choice >= 1:
                if player_choice == 1 and deployment1_passed == False:
                    print("You are now in Deployment 1")
                    """Deployment stuff"""
                    deployment1_passed = True
                elif player_choice == 2 and combat_passed == False:
                    print("You are now in the combat step")
                    """Combat Stuff"""
                    combat_passed = True
                    deployment1_passed = True
                elif player_choice == 3 and deployment2_passed == False:
                    """Deployment 2 Stuff"""
                    print("You are now in Deployment 2")
                    deployment2_passed = True
                    deployment1_passed = True
                    combat_passed = True
                elif player_choice == 4:
                    """End Turn"""
                    print("You have ended your turn")
                    player_choice = 9
                    deployment2_passed = False
                    deployment1_passed = False
                    combat_passed = False
                    #break
                else:
                    if deployment1_passed == False and combat_passed == False and deployment2_passed == False and end_turn == False:
                        print("Invalid Selection, please select one of the following options \n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn")
                    elif deployment1_passed == True and combat_passed == False and deployment2_passed == False and end_turn == False:
                        print("Invalid Selection, please select one of the following options \n2 Combat \n3 Deployment 2 \n4 End Turn")
                    elif deployment1_passed == True and combat_passed == True and deployment2_passed == False and end_turn == False:
                        print("Invalid Selection, please select one of the following options \n3 Deployment 2 \n4 End Turn")
                    elif deployment1_passed == True and combat_passed == True and deployment2_passed == True and end_turn == False:
                        print("Invalid Selection, you must select \n4 End Turn")
                    else:
                        print("Invalid Selection, please select one of the following options \n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn")
                
                player_choice= int(input("Pick the phase you would like to go to "))
        else:
            print("Invalid Selection, please select one of the following options \n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn")
            player_choice= int(input("Pick the phase you would like to go to "))



loop_player()