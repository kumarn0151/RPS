import random 

# Function go here 
def check_rounds():
    while True: 
        response = input ("How mnay rounds: ")

        round_error = "please type either <enter> or an integer that is more than 0"

        # If infinite mode not chosen, check response 
        # is an integer that is more than 0 
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to 
                # start of loop 
                if response < 1:
                    print(round_error)
                    continue 

            except ValueError:
                print(round_error)
                continue 

        return response

def choice_checker(question, valid_list, error): 

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase) 
        response = input (question).lower()
 
        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the 
        # full item name is returned

        for item in valid_list:        
            if response == item[0] or response == item: 
                return item

            # output error if item not in list 
        print(error)
        print()


# main routine

# Lists of vaild responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before 
# If 'yes', show instructions


# ask user for # of rounds then loop...
rounds_played = 0 
choose_instruction = "please choose rock (r), paper (p) or scissors (s)"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds ()

end_game="no"
while end_game == "no":

    # start of Game play loop 

    # Round Heading 
    print()
    if rounds == "": 
        heading = "continues Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)  

    print(heading) 
    choose_instruction =  ("Please choose from rock / paper /scissors (or xxx to quit)")

    
    choose_error = "Please choose from rock " \
                   "Paper / scissors (or xxx to quit)"

        # Ask user for choice and check it's vaild 
    user_choice = choice_checker (choose_instruction, rps_list, choose_error) 

    # End game if exit code is typed 
    if user_choice == "xxx" or rounds_played +1 == rounds:
        break 

    feedback = "You chose {}".format(user_choice)
    print(feedback)

    rounds_played += 1


# Ask user if they want to see their game history
# If 'yes' show game history 

# show game statistics 
