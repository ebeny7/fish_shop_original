#yummy Eeeish what will I eat
print ("sussex_with_kokobene******press 1",
            "someone_you_would_want_hear&die******press 2",
            "your_amamin******press 3",
            "roasted_chicken******press 4",
            "kokobene_with_akokomesa*****press 5")

print ("sussex_with_kokobene******press 1",
            "someone_you_would_want_hear&die******press 2",
            "your_amamin******press 3",
            "roasted_chicken******press 4",
            "kokobene_with_akokomesa*****press 5")
while True:
    response = input ( "Do wanna eat in my room: yes or no")
    if response == "yes":
        choice_food = input("choose your food:  ")
        food = ["1", "2", "3", "4", "5", "6"]
        
    else:
            print("Try the next shop")
            break
        
            

def call_c_food(choice_food):
    if choice_food == food[0]:
        print ("You feeling like the luckiest man in the world")
    elif choice_food == food[1]:
        print ("Eat after you die")
    elif choice_food == food[2]:
        print ("Live happily after")
    elif choice_food == food[3]:
        print ("That's what is supposed to be")
    elif choice_food == food[4]:
        print ("It's worth the wait")
    elif choice_food == food[5]:
        print ("You are managing your taste")
    else:
        print ("Sorry try the next shop")





while True:
    choice = input ("you can try as dishes as you want: 1st,2nd, 3rd,......")
    repeat_choice = input ("which food do you want: ")
    
    if choice == "1st":
        call_c_food(repeat_choice)
        print ("Successful")
    else:
        if choice == "2nd":
            call_c_food(repeat_choice)
            print ("Successful")
        else:
            if choice == "3rd":
                call_c_food(repeat_choice)
                print ("Successful")
                break
            else:
                print ("You fools, tell the doctor to stop the program")
                

        

        
    
    
    

        
        


        

print ("You only had three choices")
        
        
        
    
                                
