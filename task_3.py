import random
def domain(addr,para="pop.ac.uk"):
    '''Function to check the domain of the E-mail address'''
    if "@" in addr:
        splited_email=addr.split("@")
        if splited_email[1]==para:
            return True
        else:
            return False

names=["Alexa","Siri","Harry","Rice","Lux","Jenny","Rose"]              #operator name
response=["Hmm","Oh, yes I see","Tell me more","um","well","err","uh"]  #response for random others
nerwork_error=[1,1,1,1,1,1,1,1,1,0]                                     #for network error
exit_1=["bye","quit","exit","goodbye","end"]                            #To exit pop chat

#responses 
response_1=["The library is closed","The library will open at 7 am","The library is southeast of collage"]
response_2=["wifi is down","wifi is available","wifi is fast"]
response_3=["The deadline is near","The deadline will not be extended","The deadline is close "]
response_4=["The roof is a great spot","The roof is nice","The roof has its story"]
response_5=["The garden is best place to study","Study materials are in 3rd floor"]
response_6=["The food is in canteen","Not food allowed in class"]
email_address=input("Please enter your Poppleton email address : ")     
checking_email=domain(email_address)

if checking_email:      #checking if email is valid
    operator_name=random.choice(names)
    tmp_name=email_address.split("@")       #Spliting from @ for user name
    user_name=tmp_name[0]

    print(f"Hi,{user_name} ! Thank you, and Welcome to PopChat !\n My name is {operator_name}, and it will be my pleasure to help you.")
    
    while True:
        question=input("--->").lower()
        if question in exit_1: #checking if input is for exiting
            print(f"Thank you, {user_name} for using PopChat. See you again soon!") 
            break
        
        simple_response={"library":response_1,"wifi":response_2,"deadline":response_3,"roof":response_4,"study":response_5,"food":response_6}#dictionary for responses
        try:    
            print(random.choice(simple_response[question])) 
        except:
            print(random.choice(response))
        if random.choice(nerwork_error)==0: #checking for network error
            print(f"***Network Error***\nThank you, {user_name} for using PopChat. See you again soon!")
            break  
              
else:
    print("This email is invalid. Domain must be pop.ac.uk")