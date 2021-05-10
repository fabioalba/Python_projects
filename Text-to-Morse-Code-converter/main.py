from alphabet import dict, inverted_dict, logo
from functions import encode, decode
import time
import os


## Encode a message
play = True
while play == True:
    print(logo)
    print("\nWelcome to the morse encoder / decoder. \n ")
    msg = input("Enter the message you want to encode: ").lower()
    print(f"inserted message: {msg}")

    morse_msg = encode(message=msg, alphabet=dict)


    ## Choose whether to decode the message
    proceed = False
    while proceed == False:
        want_decode = input("Do you want to decode the message? yes or no:").lower()
        if want_decode == "yes":
            decode(message=morse_msg, alphabet=inverted_dict)
            proceed = True
        elif want_decode == "no":
            proceed = True
        else:
            print('\nInvalid answer: please enter "yes" or "no"')


    ## Choose whether to play again or not
    choose_next_step = False
    while choose_next_step == False:
        play_again = input("Do you want to encode another message? Yes or no:").lower()
        if play_again == "yes":
            choose_next_step = True
            continue
        elif play_again == "no":
            play = False
            choose_next_step = True
            print("\nGoodbye!")
            time.sleep(2)

            ## clear screen:
            os.system("cls")
        else:
            print('\nInvalid answer: please enter "yes" or "no"')


