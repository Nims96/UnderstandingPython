from Player import player_class

player1 = player_class(True,2)
player2 = player_class(False,2)

a = "Welcome to the game"
b = a.center(75)
c = "\n\n\tDefeat your enemy by reducing their life to 0 or they cannot draw. \n\t\t\tEnter a number to move to phase\n"
print("\n" + b + c)

print("Player 1 Begin")

player1.hand = ["Rathalos", "Ruby", "Emerald"]
player1_creature_zone = ["Rathian", "Rathalos"]
player1_resource_zone = ["Ruby", "Ruby", "Ruby", "Ruby", "Emerald", "Emerald", "Emerald"]
player1_used_resources = ["Ruby"]
player1_unused_resources = ["Ruby", "Ruby", "Ruby", "Emerald", "Emerald", "Emerald"]
player1.deck = ["Rathalos", "Rathian", "Ruby", "Emerald","Rathalos", "Rathian", "Ruby", "Emerald"]
player1.discard = ["Rathalos", "Rathian"]
player1.banished = ["Rathalos", "Rathian"]

player2.hand = ["Frozen Bite", "Hurl Snow-Boulder", "Barioth"]
player2_creature_zone = ["Barioth"]
player2_resource_zone = ["Sapphire", "Sapphire", "Sapphire", "Sapphire", "Sapphire"]
player2_used_resources = ["Sapphire", "Sapphire", "Sapphire"]
player2_unused_resources = ["Sapphire", "Sapphire"]
player2.deck = ["Barioth", "Barioth", "Sapphire", "Sapphire", "Frozen Bite", "Hurl Snow-Boulder", "Sapphire", "Sapphire"]
player2.discard = ["Barioth", "Frozen Bite"]
player2.banished = ["Barioth", "Frozen Bite"]

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

def inner_actions_menu(phase):
    print("\nHere are the actions you can perform in this phase:\n")

    if phase == 1 or phase == 3:
        print("1: Play a creature")
        print("2: Play a resource")
        print("3: Play a spell")
        print("4: Proceed to Next Phase")
        print("5: Show Hand\n")
    elif phase == 2:
        print("1: Select creatures you want to attack with")
        print("2: Skip attacking")
        print("3: Show boards\n")
    else:
        print("1: Show board")
        print("2: Show hand")
        print("3: Proceed to end\n")

    print("Please select an action you would like to take: ")


def outer_actions_menu(phase, dep1, combat, dep2):
    print("\nHere are the actions you can perform in this phase:\n")

    if phase == 1:
        print("2: Combat Phase")
        print("3: Deployment Phase 2")
        print("4: End Phase")
        print("5: Show board")
        print("6: Show Hand")
    elif phase == 2:
        print("3: Deployment Phase 2")
        print("4: End Turn")
        print("5: Show board")
        print("6: Show Hand")
    elif phase == 3:
        print("4: End Turn")
        print("5: Show board")
        print("6: Show Hand")
    elif phase == 5:
        if  dep1 == False and combat == False and dep2 == False:
            print("1: Deployment Phase 1")
            print("2: Combat Phase")
            print("3: Deployment Phase 2")
            print("4: End Phase")
            print("5: Show board")
            print("6: Show Hand")
        elif dep1 == True and combat == False and dep2 == False:
            print("2: Combat Phase")
            print("3: Deployment Phase 2")
            print("4: End Phase")
            print("5: Show board")
            print("6: Show Hand")
        elif dep1 == True and combat == True and dep2 == False:
            print("3: Deployment Phase 2")
            print("4: End Turn")
            print("5: Show board")
            print("6: Show Hand")
        else:
            print("4: End Turn")
            print("5: Show board")
            print("6: Show Hand")
    elif phase == 6:
        if  dep1 == False and combat == False and dep2 == False:
            print("1: Deployment Phase 1")
            print("2: Combat Phase")
            print("3: Deployment Phase 2")
            print("4: End Phase")
            print("5: Show board")
            print("6: Show Hand")
        elif dep1 == True and combat == False and dep2 == False:
            print("2: Combat Phase")
            print("3: Deployment Phase 2")
            print("4: End Phase")
            print("5: Show board")
            print("6: Show Hand")
        elif dep1 == True and combat == True and dep2 == False:
            print("3: Deployment Phase 2")
            print("4: End Turn")
            print("5: Show board")
            print("6: Show Hand")
        else:
            print("4: End Turn")
            print("5: Show board")
            print("6: Show Hand")

    print("Please select an action you would like to take: ")

def show_board():
    print("\nHere is the board")
    print("Your creatures: " + str(player1_creature_zone))
    print("Your total resources are: " + str(player1_resource_zone))
    print("Unused resources: " + str(player1_unused_resources))
    print("Your used resources are: " + str(player1_used_resources))

    print("\n\nHere is you opponents board")
    print("Your opponent has " +
          str(len(player2.hand)) + " cards in hand")
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
        print(player1.hand)

        inner_actions_menu(phase_number)

        inner_phase_choice = valid_entry()

        while True:
            if inner_phase_choice == 1:
                print("Select a creature from your hand that you would like to play")
                inner_actions_menu(phase_number)
                inner_phase_choice = valid_entry()

            elif inner_phase_choice == 2:
                print("Select a resource from your hand that you would like to play")
                inner_actions_menu(phase_number)
                inner_phase_choice = valid_entry()

            elif inner_phase_choice == 3:
                print("Select a spell from your hand that you would like to play")
                inner_actions_menu(phase_number)
                inner_phase_choice = valid_entry()

            elif inner_phase_choice == 4:
                break

            elif inner_phase_choice == 5:
                print("Here is your hand")
                print(player1.hand)
                
                inner_actions_menu(phase_number)
                inner_phase_choice = valid_entry()

            else:
                print("That is not a valid choice!")

                inner_actions_menu(phase_number)

                inner_phase_choice = valid_entry()
    elif phase_number == 2:
        print("Here are your creatures: " + str(player1_creature_zone))
        print("Here are your opponents creatures: " + str(player2_creature_zone))

        inner_actions_menu(phase_number)

        inner_phase_choice = valid_entry()
        
        while True:
            if inner_phase_choice == 1:
                print("Here are your creatures: " + str(player1_creature_zone) + "\n")
                print("Here are your opponents creatures: " + str(player2_creature_zone) + "\n")
                print("Please select which creature you want to attack with")
                
                for x in range(0, len(player1_creature_zone)):
                    print(str(x + 1) + ": " + player1_creature_zone[x])
                    
                inner_phase_choice = valid_entry()

            elif inner_phase_choice == 2:
                print("Attack phase skipped")
                break

            elif inner_phase_choice == 3:
                show_board()
                inner_actions_menu(phase_number)

                inner_phase_choice = valid_entry()

            else:
                print("That is not a valid choice. Please select one of the following: ")
                inner_actions_menu(phase_number)

                inner_phase_choice = valid_entry()
    elif phase_number == 3:
        print("Here is/are the card/cards in your hand")
        print(player1.hand)
        
        inner_actions_menu(phase_number)

        
        inner_phase_choice = valid_entry()

        while True:
            if inner_phase_choice == 1:
                print("Select a creature from your hand that you would like to play")
                inner_actions_menu(phase_number)
                inner_phase_choice = valid_entry()

            elif inner_phase_choice == 2:
                print("Select a resource from your hand that you would like to play")
                inner_actions_menu(phase_number)
                inner_phase_choice = valid_entry()
            elif inner_phase_choice == 3:
                print("Select a spell from your hand that you would like to play")
                inner_actions_menu(phase_number)
                inner_phase_choice = valid_entry()
            elif inner_phase_choice == 4:
                break

            elif inner_phase_choice == 5:
                print("Here is your hand")
                print(player1.hand)

                inner_actions_menu(phase_number)

                inner_phase_choice = valid_entry()

            else:
                print("That is not a valid choice. Please select one of the following: ")
                inner_actions_menu(phase_number)
                inner_phase_choice = valid_entry()
    elif phase_number == 4:
        print("You are about to end your turn")

        inner_actions_menu(phase_number)

        inner_phase_choice = valid_entry()
        while True:
            if inner_phase_choice == 1:
                show_board()
                inner_actions_menu(phase_number)
                inner_phase_choice = valid_entry()

            elif inner_phase_choice == 2:
                print("Here is your hand: ")
                print(player1.hand)
                inner_actions_menu(phase_number)
                inner_phase_choice = valid_entry()

            elif inner_phase_choice == 3:
                break

            else:
                print("That is not a valid choice. Please select one of the following: ")
                inner_actions_menu(phase_number)
                inner_phase_choice = valid_entry()

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
            outer_actions_menu(phase_choice, deployment1_passed, combat_passed, deployment2_passed)
            deployment1_passed = True
        elif phase_choice == 2 and combat_passed == False:
            print("You are now in the combat step")
            """Combat Stuff"""
            inner_options(phase_choice)
            outer_actions_menu(phase_choice, deployment1_passed, combat_passed, deployment2_passed)
            combat_passed = True
            deployment1_passed = True
        elif phase_choice == 3 and deployment2_passed == False:
            """Deployment 2 Stuff"""
            print("You are now in Deployment 2")
            inner_options(phase_choice)
            outer_actions_menu(phase_choice, deployment1_passed, combat_passed, deployment2_passed)
            deployment2_passed = True
            deployment1_passed = True
            combat_passed = True
        elif phase_choice == 4:
            """End Turn"""
            inner_options(phase_choice)
            print("You have ended your turn")
            deployment2_passed = False
            deployment1_passed = False
            combat_passed = False
            break
        elif phase_choice == 5:
            show_board()
            outer_actions_menu(phase_choice, deployment1_passed, combat_passed, deployment2_passed)
        elif phase_choice == 6:
            print("Here is/are the card/cards in your hand")
            print(player1.hand)

            outer_actions_menu(phase_choice, deployment1_passed, combat_passed, deployment2_passed)
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

while player1.health > 0 and player2.health > 0:
    loop_player()
    if player1.player_turn == True:
        player1.health -= 1
        player1.player_turn = False
        player2.player_turn = True
        if player1.health <= 0:
            print("Player 2 Victory!")
        elif player2.health <= 0:
            print("Player 1 Victory!")
        elif player1.health > 0 and player2.health > 0:
            print("Player 2's Turn")
    elif player2.player_turn == True:
        player2.health -= 1
        player1.player_turn = True
        player2.player_turn = False
        if player1.health <= 0:
            print("Player 2 Victory!")
        elif player2.health <= 0:
            print("Player 1 Victory!")
        elif player1.health > 0 and player2.health > 0:
            print("Player 1's Turn")
