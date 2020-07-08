a= "Welcome to the game"
b= a.center(75)
c= "\n\n\tDefeat your enemy by reducing their life to 0 or they cannot draw. \n\t\t\tEnter a number to move to phase\n"
print("\n" + b + c)

print("Player 1 Begin")

print("\n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn")

player_choice= int(input("Pick the phase you would like to go to "))

deployment1_passed = False
combat_passed = False
deployment2_passed = False
end_turn = False


while player_choice <= 4 and player_choice >= 1:
    if player_choice == 1 and deployment1_passed == False:
        """Deployment stuff"""
        deployment1_passed = True
    elif player_choice == 2 and combat_passed == False:
        """Combat Stuff"""
        combat_passed = True
        deployment1_passed = True
    elif player_choice == 3 and deployment2_passed == False:
        """Deployment 2 Stuff"""
        deployment2_passed = True
        deployment1_passed = True
        combat_passed = True
    elif player_choice == 4 and end_turn == False:
        """End Turn"""
        end_turn = True
        deployment2_passed = True
        deployment1_passed = True
        combat_passed = True
    else:
        if deployment1_passed == False:
            combat_passed == False
            deployment2_passed == False
            end_turn == False
            print("Invalid Selection, please select one of the following options \n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn")
        elif deployment1_passed == True:
            combat_passed == False
            deployment2_passed == False
            end_turn == False
            print("Invalid Selection, please select one of the following options \n2 Combat \n3 Deployment 2 \n4 End Turn") 
        elif deployment1_passed == True:
            combat_passed == True
            deployment2_passed == False
            end_turn == False
            print("Invalid Selection, please select one of the following options \n3 Deployment 2 \n4 End Turn")
        elif deployment1_passed == True:
            combat_passed == True
            deployment2_passed == True
            print("All phases complete, please enter 4 to end turn")            
            
    
    player_choice= int(input("Pick the phase you would like to go to "))


print("Testing the merger \n\n\t\t\t Testing the merger")