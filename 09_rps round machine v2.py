# Function used to check input is valid 


def check_rounds():
    while True: 
        response = input ("How mnay rounds: ")

        round_error = "please type either <enter> or an integer that is more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue 

            except ValueError:
                print(round_error)
                continue 

        return response


# Main routine goes here...

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
        heading = "Round {} of".format(rounds_played + 1)  

    print(heading) 
    choose = input("{} or 'xxx' to""end: ".format(choose_instruction))

    # End game if exit code is typed 
    if choose == "xxx":
        break 

    # **** rest of loop / game ****