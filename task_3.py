if __name__=="__main__":
    import random
    def domain(addr,para="pop.ac.uk"):
        '''Function to check the domain of the E-mail address'''
        if "@" in addr:
            splited_email=addr.split("@")
            if splited_email[1]==para:
                return True
            else:
                return False

    names=["Alexa","Siri","Harry","Rice","Lux","Jenny","Rose"]
    response=["Hmm","Oh, yes I see","Tell me more","um","well","err","uh"]
    nerwork_error=[1,1,1,1,1,1,1,1,1,0]
    exit_1=["bye","quit","exit","goodbye","end"]
    
    
    email_address=input("Please enter your Poppleton email address : ")
    checking_email=domain(email_address)

    if checking_email:
        operator_name=random.choice(names)
        tmp_name=email_address.split("@")
        user_name=tmp_name[0]

        print(f"Hi,{user_name} ! Thank you, and Welcome to PopChat !\n My name is {operator_name}, and it will be my pleasure to help you.")
        flag=False
        
        while True:
            question=input("--->").lower()
            
            if random.choice(nerwork_error)==0:
                print(f"***Network Error***\nThank you, {user_name} for using PopChat. See you again soon!")
                break
            
            if "library" in question:
                print("The libary is closed today.")
            elif "wifi" in question:
                print("WiFi is excellent across the campus.")
            elif "deadline" in question:
                print("Your deadline has been extended by two working days.")
            elif "food" in question:
                print("The canteen closes at 7pm")
            elif "roof" in question:
                print("The rooftop is offlimits")
            elif "study" in question:
                print("Garden is one of the best place to study alone")
            else:
                for i in exit_1:
                    if(i in question):
                        print(f"Thank you, {user_name} for using PopChat. See you again soon!")
                        flag=True
                        break
                else:
                    reply_choices=random.choice(response)
                    print(reply_choices)
                    
            if flag==True:
                break    
    else:
        print("This email is invalid. Domain must be pop.ac.uk")