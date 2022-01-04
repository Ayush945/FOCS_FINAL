print("\nStop! Who would cross the Bridge of Death\nMust answer me these question three, 'ere the other side he see.\n")

name=input("What is your name? ")
king_name="arthur"

if name.lower()==king_name: #Checking the king's name
    print("My liege! You may pass!")
else:
    quest=input("What is your quest? ")
    quest_goal="grail"

    if quest_goal in quest.lower(): #Checking the quest
        color=input("What is your favourite colour? ")

        if color[0]==name[0]: #Checking the first character of color and name 
            print("You may pass")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")

    else:
        print("Only those who seek the Grail may pass\nYou must now face the Gorge of Eternal Peril." )