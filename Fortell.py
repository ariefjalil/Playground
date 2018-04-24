"""
A simple program that will answer
your yes and no questions.
@author Arief Jalil
@version 1510.2017d
"""

import random

#class fortell_main: class

def main():

   print "I can tell your future!"

   replies = ["I don't think so","Definitely yes!","It's hard to say.",
               "Yes all the way!", "Hmmm...maybe?","Not really",
               "Ask something else"]


    while True:
           question = raw_input("Enter a yes/no question: ")

                    #Random number that translates to response
                    rand_val= int(random.random() * len(replies))
                    print(replies[rand_val])

                    #Ask if they want to try again
                    again = raw_input("Would you like to ask another question? y/n?: ")
                    if again[0].lower() == "n":
                        break
        print "Goodbye!"


if __name__ == "__main__":
    main()
