#yummy Eeeish what will I eat
print ("Your wildest desire******enter your password",
            "origin_zero******press 0",
            "chicken_with_fish_salad******press 1",
            "roasted_turkey******press 2",
            "chicken_tail_with_akokomesa*****press 3")

             
            


w_desire = input("Enter anything you want to eat for the first time-Like Ever: ")
sussex = "Feeling like the luckiest man in the world!!!" + " Served with " + str(w_desire)  + ",eat the meat only, the rest is for the owner"
print (sussex)
food = [sussex, "0", "1", "2", "3"]

def think_tiree():
    while True:
        response = input ( "Do wanna choose food: yes or no")
        if response == "yes":
            choice_food = input("choose your food:  ")
            break
        else:
            print("I can't help you")
            break


                    

def call_c_food(think_tiree):
    if think_tiree == sussex:
        print ("You feeling like the luckiest man in the world")
    elif think_tiree == food[1]:
        print ("You healed your chest with bitter juice")
    elif think_tiree == food[2]:
        print ("Live happily after")
    elif think_tiree == food[3]:
        print ("You eat at Thanksgiving or once in a while")
    elif think_tiree == food[4]:
        print ("So you never change your taste")
    else:
        print ("Sorry try the next shop")


            
            
            
    

while True:
        choice = input ("you can try as many dishes as you want(Fill with Roma Numerals:......")#fill with roman numerals
        
        #print (sussex)
        
        
        if choice == "I":  
            colgate = input ("Fill food/with Integers: ")
            print("successful")
            call_c_food(colgate)
            
        else: 
            if choice == "II": 
                voltic = input ("Everything is possible/with Integers: ")
                print("Successful")
                call_c_food(voltic)
                break
            
            else:
                print ("You fools, tell the doctor to stop the program")
            




                

        

        
    
    
    

        
        


        

print ("You only had three choices")
        
        
        
    
                                
