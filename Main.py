import sys

a = "Welcome to the game"
b = a.center(75)
c = "\n\n\tDefeat your enemy by reducing their life to 0 or they cannot draw. \n\t\t\tEnter a number to move to phase\n"
print("\n" + b + c)

print("Player 1 Begin")

player1_hand = ["Rathalos", "Ruby", "Emerald"]
player1_creature_zone = ["Rathian", "Rathalos"]
player1_resource_zone = ["Ruby", "Ruby", "Ruby", "Ruby", "Emerald", "Emerald", "Emerald"]
player1_used_resources = ["Ruby"]
player1_unused_resources = ["Ruby", "Ruby", "Ruby", "Emerald", "Emerald", "Emerald"]

player2_hand = ["Frozen Bite", "Hurl Snow-Boulder", "Barioth"]
player2_creature_zone = ["Barioth"]
player2_resource_zone = ["Sapphire", "Sapphire", "Sapphire", "Sapphire", "Sapphire"]
player2_used_resources = ["Sapphire", "Sapphire", "Sapphire"]
player2_unused_resources = ["Sapphire", "Sapphire"]

def valid_entry():
    test = 0
    phase_choice = input()

    while test == 0:
        if phase_choice.isalpha() == True:
            print("You must select a number to take action")
            phase_choice = input("Pick the phase you would like to go to ")
        elif phase_choice.isdigit() == True:
            phase_choice = int(phase_choice)
            test = 1
            return phase_choice
        else:
            print("You have selected nothing, Please make a choice:")
            print("You must select a number to take action")
            phase_choice = input("Please select one of the above options: ")

def deployment_actions_menu():
    print("Here are the actions you can perform in this phase: ")

    print("1: Play a creature")
    print("2: Play a resource")
    print("3: Play a spell")
    print("4: Proceed to Next Phase")
    print("5: Show Hand")

    print("Please select an action you would like to take: ")

def show_board():
    print("\nHere is the board")
    print("Your creatures: " + str(player1_creature_zone))
    print("Your total resources are: " + str(player1_resource_zone))
    print("Unused resources: " + str(player1_unused_resources))
    print("Your used resources are: " + str(player1_used_resources))

    print("\n\nHere is you opponents board")
    print("Your opponent has " +
          str(len(player2_hand)) + " cards in hand")
    print("Your opponents creatures: " + str(player2_creature_zone))
    print("Your opponents total resources are: " +
          str(player2_resource_zone))
    print("Your opponents unused resources: " +
          str(player2_unused_resources))
    print("Your opponents used resources are: " +
          str(player2_used_resources))

def inner_options(phase_number):
    if phase_number == 1:
        print("Here is/are the card/cards in your hand")
        print(player1_hand)
        print()
        
        deployment_actions_menu()

        inner_phase_choice = valid_entry()

        while True:
            if inner_phase_choice == 1:
                print("Select a creature from your hand that you would like to play")
                deployment_actions_menu()
                inner_phase_choice = valid_entry()

            elif inner_phase_choice == 2:
                print("Select a resource from your hand that you would like to play")
                deployment_actions_menu()
                inner_phase_choice = valid_entry()

            elif inner_phase_choice == 3:
                print("Select a spell from your hand that you would like to play")
                deployment_actions_menu()
                inner_phase_choice = valid_entry()

            elif inner_phase_choice == 4:
                break

            elif inner_phase_choice == 5:
                print("Here is your hand")
                print(player1_hand)
                
                deployment_actions_menu()
                inner_phase_choice = valid_entry()

            else:
                print("That is not a valid choice!")

                deployment_actions_menu()

                inner_phase_choice = valid_entry()
    elif phase_number == 2:
        print("Here are your creatures: " + str(player1_creature_zone))
        print("Here are your opponents creatures: " + str(player2_creature_zone))

        print("1: Select creatures you want to attack with")
        print("2: Skip attacking")
        print("3: Show boards")

        inner_phase_choice = int(input("Please select an action you would like to take: "))
        
        while True:
            if inner_phase_choice == 1:
                print("Here are your creatures: " + str(player1_creature_zone) + "\n")
                print("Here are your opponents creatures: " + str(player2_creature_zone) + "\n")
                print("Please select which creature you want to attack with")
                
                for x in range(0, len(player1_creature_zone)):
                    print(str(x + 1) + ": " + player1_creature_zone[x])
                    
                break

            elif inner_phase_choice == 2:
                print("Attack phase skipped")
                break

            elif inner_phase_choice == 3:
                show_board()
                inner_phase_choice = int(input("Select one of the above actions to take: "))

            else:
                print("That is not a valid choice. Please select one of the following: ")
                print("1: Select creatures you want to attack with")
                print("2: Skip attacking")
                print("3: Show boards")
                inner_phase_choice = int(input("Select one of the above actions to take: "))
    elif phase_number == 3:
        print("Here is/are the card/cards in your hand")
        print(player1_hand)
        
        print("1: Play a creature")
        print("2: Play a resource")
        print("3: Play a spell")
        print("4: Proceed to Next Phase")
        print("5: Show Hand")
        
        inner_phase_choice = int(input("Please select an action you would like to take: "))

        while True:
            if inner_phase_choice == 1:
                print("Select a creature from your hand that you would like to play")
                inner_phase_choice = int(input("Select one of the above actions to take: "))

            elif inner_phase_choice == 2:
                print("Select a resource from your hand that you would like to play")
                inner_phase_choice = int(input("Select one of the above actions to take: "))

            elif inner_phase_choice == 3:
                print("Select a spell from your hand that you would like to play")
                inner_phase_choice = int(input("Select one of the above actions to take: "))

            elif inner_phase_choice == 4:
                break

            elif inner_phase_choice == 5:
                print("Here is your hand")
                print(player1_hand)

                inner_phase_choice = int(input("Select one of the above actions to take: "))

            else:
                print("That is not a valid choice. Please select one of the following: ")
                print("1: Play a creature")
                print("2: Play a resource")
                print("3: Play a spell")
                print("4: Proceed to Next Phase")
                print("5: Show Hand")
                inner_phase_choice = int(input("Select one of the above actions to take: "))
    elif phase_number == 4:
        print("You are about to end your turn")

        print("1: Show board")
        print("2: Show hand")
        print("3: Proceed to end")

        inner_phase_choice = int(input("Please select an action you would like to take: "))

        if inner_phase_choice == 1:
            show_board()
            inner_phase_choice = int(input("Please select an action you would like to take: "))

        elif inner_phase_choice == 2:
            print(player1_hand)
            inner_phase_choice = int(input("Please select an action you would like to take: "))

        elif inner_phase_choice == 3:
            print("About to end turn")

        else:
            print("That is not a valid choice. Please select one of the following: ")
            print("1: Show board")
            print("2: Show hand")
            print("3: Proceed to end")
            inner_phase_choice = int(
                input("Select one of the above actions to take: "))

def loop_player():
    print("\n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn \n5 Show Board \n6 Show Hand")
    deployment1_passed = False
    combat_passed = False
    deployment2_passed = False

    phase_choice = valid_entry()

    while phase_choice > 6 or phase_choice < 1:
        print("Invalid Selection, please select one of the following options \n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn \n5 Show Board \n6 Show Hand")
        phase_choice= valid_entry()

    while phase_choice <= 6 and phase_choice >= 1:
        if phase_choice == 1 and deployment1_passed == False:
            print("You are now in Deployment 1")
            """Deployment stuff"""
            inner_options(phase_choice)
            deployment1_passed = True
        elif phase_choice == 2 and combat_passed == False:
            print("You are now in the combat step")
            """Combat Stuff"""
            combat_passed = True
            deployment1_passed = True
        elif phase_choice == 3 and deployment2_passed == False:
            """Deployment 2 Stuff"""
            print("You are now in Deployment 2")
            deployment2_passed = True
            deployment1_passed = True
            combat_passed = True
        elif phase_choice == 4:
            """End Turn"""
            print("You have ended your turn")
            deployment2_passed = False
            deployment1_passed = False
            combat_passed = False
            break
        elif phase_choice == 5:
            show_board()
        elif phase_choice == 6:
            print("Here is/are the card/cards in your hand")
            print(player1_hand)
        else:
            if deployment1_passed == False and combat_passed == False and deployment2_passed == False:
               print("Invalid Selection, please select one of the following options \n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn \n5 Show Board \n6 Show Hand")
            elif deployment1_passed == True and combat_passed == False and deployment2_passed == False:
               print("Invalid Selection, please select one of the following options \n2 Combat \n3 Deployment 2 \n4 End Turn \n5 Show Board \n6 Show Hand")
            elif deployment1_passed == True and combat_passed == True and deployment2_passed == False:
                print("Invalid Selection, please select one of the following options \n3 Deployment 2 \n4 End Turn \n5 Show Board \n6 Show Hand")
            elif deployment1_passed == True and combat_passed == True and deployment2_passed == True:
                print("Invalid Selection, you must select \n4 End Turn")
            else:
                print("Invalid Selection, please select one of the following options \n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn \n5 Show Board \n6 Show Hand")
            
        phase_choice = valid_entry()

        if phase_choice > 6 or phase_choice < 1:
            while phase_choice > 6 or phase_choice < 1:
                print("Invalid Selection, please select one of the following options \n1 Deployment \n2 Combat \n3 Deployment 2 \n4 End Turn \n5 Show Board \n6 Show Hand")
                phase_choice = valid_entry()

loop_player()
