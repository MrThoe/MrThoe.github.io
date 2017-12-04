#My Python Story

def greeting():
    print("Hello.....")
    response=input('Do you want to play? (yes/no)')
    return response

def second_choice():
    print ("Great.....")
    response=input('Do you open it?...')
    return response

def haters():  #exits the game
    print ("Lame, bye then!")

def opened():
    #Enter your code here
def not_opened():
    #Enter your code here
x = greeting()

if x=="yes":
    y = second_choice()
    if y=="yes":
        opened()
    else:
        not_opened()
else:
    haters()


    

