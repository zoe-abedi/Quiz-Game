print("Welcome to my Computer Quiz!")
playing = input("Do you want to play?\n")

if playing.lower() != "yes":
    quit()
print("Okay! Lets Start Playing :) ")  



while(True):
    answer = input("What does CPU stands for\n")
    if answer.lower() == "central processing unit":
        print("Correct!") 
        break
    else:
        print("Oops! Try Again, I'm sure you'll get it right this time")
        continue



while(True):
    answer = input("What is the port number for http\n")
    if answer.lower() == "80":
        print("Correct!") 
        break
    else:
        print("Oops! Try Again, I'm sure you'll get it right this time")
        continue



while(True):
    answer = input("Is Python a Static or a Dynamic Language\n")
    if answer.lower() == "dynamic":
        print("Correct!") 
        break
    else:
        print("Oops! Try Again, I'm sure you'll get it right this time")
        continue




while(True):
    answer = input("Does Pyhton uses a compiler or an interpretator\n")
    if answer.lower() == "both":
        print("Correct!") 
        break
    else:
        print("Oops! Try Again, I'm sure you'll get it right this time")
        continue


while(True):
    answer = input("Who designs the brain of a webpage\n")
    if answer.lower() == "java script":
        print("Correct!") 
        break
    else:
        print("Oops! Try Again, I'm sure you'll get it right this time")
        continue


while(True):
    answer = input("What does CSS stands for\n")
    if answer.lower() == "cascading style sheets":
        print("Correct!") 
        break
    else:
        print("Oops! Try Again, I'm sure you'll get it right this time")
        continue 
    
           
print("Congratulations! You aced the Quiz")     
