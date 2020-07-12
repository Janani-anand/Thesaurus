import json
from difflib import get_close_matches
# used to compare strings
# https://towardsdatascience.com/sequencematcher-in-python-6b1e6f3915fc
# https://medium.com/boring-tech/python-programming-the-standard-library-difflib-28ffaf5c1155

data = json.load(open("data/data.json"))

def printdef(word):
    for i,defintion in enumerate(data[word]):
        print(str(i+1)+") " + defintion)

def defintions(word):
    word=word.lower()
    if word in data:
        printdef(word)
    elif len(get_close_matches(word,data.keys())) > 0:
        correct_word=get_close_matches(word,data.keys())[0]
        print("Did you mean %s instead?" %(correct_word))
        print("Press Y/y for yes and N/n for no: ")
        key=input().lower()
        if(key=='y'):
            printdef(correct_word)
        elif(key == 'n'):
            print("The word doesn't exist, please double check it")
        else:
            print("We didn't understand your entry! :(")
    else:
        print("The word doesn't exist, please enter a valid word.")

word=input("Enter word: ")
defintions(word)
#%s is a format specifier
