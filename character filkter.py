#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      ronan.rodulfo
#
# Created:     21/06/2021
# Copyright:   (c) ronan.rodulfo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#character filter
def characterFilter():
    userInput = input("type something: ")
    if "?" or "." or "!" in userInput:
        userInput = userInput.replace("?","")
        userInput = userInput.replace("!","")
        userInput = userInput.replace(".","")
        userInput = userInput.replace("?","")
        userInput = userInput.replace("!","")
        userInput = userInput.replace(".","")

        print(userInput)



characterFilter()
