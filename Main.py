a= "Welcome to the game"
b= a.center(75)
c= "\n\n\tDefeat your enemy by reducing their life to 0 or they cannot draw. \n\t\t\tEnter a number to move to phase\n"
print("\n" + b + c)

print("Player 1 Begin")

print("\n1: Deployment \n2: Combat \n3: Deployment 2 \n4: End Turn \n5: Show board \n6: Show hand")

player_choice= int(input("Pick the phase you would like to go to "))

player1_hand = ["Rathalos", "Ruby", "Emerald"]

player1_creature_zone = ["Rathian"]
player1_resource_zone = ["Ruby", "Ruby", "Ruby", "Ruby", "Emerald", "Emerald", "Emerald"]
player1_used_resources = ["Ruby"]
player1_unused_resources = ["Ruby", "Ruby", "Ruby", "Emerald", "Emerald", "Emerald"]

player2_hand = ["Frozen Bite", "Hurl Snow-Boulder", "Barioth"]

player2_creature_zone = ["Barioth"]
player2_resource_zone = ["Sapphire", "Sapphire", "Sapphire", "Sapphire", "Sapphire"]
player2_used_resources = ["Sapphire", "Sapphire", "Sapphire"]
player2_unused_resources = ["Sapphire", "Sapphire"]

def loop_player():
    print("\n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn")
    player_choice= int(input("Pick the phase you would like to go to "))
    deployment1_passed = False
    combat_passed = False
    deployment2_passed = False
    end_turn = False
    while player_choice > 6 or player_choice < 1:
        print("Invalid Selection, please select one of the following options \n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn")
        player_choice= int(input("Pick the phase you would like to go to "))

    while player_choice <= 6 and player_choice >= 1:
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
            deployment2_passed = False
            deployment1_passed = False
            combat_passed = False
            break
        elif player_choice == 5:
            print("Here is the board")
            print("Your creatures: " + str(player1_creature_zone))
            print("Your total resources are: " + str(player1_resource_zone))
            print("Unused resources: " + str(player1_unused_resources))
            print("Your used resources are: " + str(player1_used_resources))
        
            print("\n\nHere is you opponents board")
            print("Your opponent has " + str(len(player2_hand)) + " cards in hand")
            print("Your opponents creatures: " + str(player2_creature_zone))
            print("Your opponents total resources are: " + str(player2_resource_zone))
            print("Your opponents unused resources: " + str(player2_unused_resources))
            print("Your opponents used resources are: " + str(player2_used_resources))

        elif player_choice == 6:
            print("Here is/are the card/cards in your hand")
            print(player1_hand)
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

        if player_choice > 6 or player_choice < 1:
            while player_choice > 6 or player_choice < 1:
                print("Invalid Selection, please select one of the following options \n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn")
                player_choice= int(input("Pick the phase you would like to go to "))



loop_player()
