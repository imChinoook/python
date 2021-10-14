import time
import sys
import random
from time import sleep

def main():

    # Shows a very nice welcome screen!

    print(
        "\033[1;32m======================================================================================"
    )

    print(
        "\n\033[3;34m                             Welcome to the number guesser!"
    )
    print(
        "\n\033[3;34m                            1. Start 2. How to play 3. Exit"
    )
    print(
        "\n\033[0;32m======================================================================================"
    )
    #Asks what the user wants to click on
    ans = input("")
    # Exits the progam
    if ans == '3':

        def exit():
            print("Closing now...")
            time.sleep(3)
            sys.exit()

        exit()

    if ans == '1':




      life = 5
      number = random.randrange(1, 10)
      while life > 0:

  # Generating Number


          #Loading menu

          # Starts the guessing
        ans = int(input("\n\n\nWhat is the number I'm thinking of? "))
              # Shows if correct
        if ans == number:

                  print(
                      "\n\n\nThats correct!\n\n\n You get 1 gold medal! Well done!\n\n\nYou finished with",life,"lives remaining"
                  )
                  return main()



              # This shows if number is too low
        elif ans < number:
                  print("\n\n\nYour too low! Total lifes remaining",life,)
                  life -= 1

              # This shows if number is too high
        if ans > number:
                  print("\n\n\nYour too high! Total lifes remaining",life,)
                  life -= 1
    if ans == '2':

        # This starts a page that can be referred back to without looping

        def start1():
            print(
                "\n\033[0;32m======================================================================================"
            )
            print(
                "\n                                              How to play!")
            print(
                "\n  I think of a number between 1 and 10, if you can guess it correctly, you get a prize, \nhowever if you fail thats okay because you get another turn"
            )
            print(
                "\n                                       Press 1 to return to menu"
            )
            print(
                "\n\033[0;32m======================================================================================"
            )

            # This is asking the user if they want to leave

            ans1 = input("")

            # This returns them to menu() if they press 1 (leave)

            if ans1 == '1':
                return main()

            # This shows if they put an invalid input (Not 1)

            else:
                print("Invalid Input!")
                time.sleep(3)
                return start1()

        # This shows the help page
        start1()


# This shows the main menu
main()





