
def speed_analysis():
    '''Analyze speed and gives the maximum minimum and average output in both MPH and KPH '''
    print("\nSwallow Speed Analysis: Version 1.0\n")
    datas=list()

    while True: 
        reading_1=input("Enter the reading:")
        if (reading_1) == "":   #if no reading is given
            if (len(datas)) == 0:   #checking the length of datas
                print("No readings entered. Nothing to do.")
                break
            print("No readings entered. Nothing to do.\n")
            
            if len(datas)==1:  #if there is data 
                print("1 Result Analysed")
            elif len(datas)>=1: #print according to data given
                print(f"{len(datas)} Results Analysed")
            print("Result Summary\n")
            break
            
        elif reading_1:
            print("Reading Saved\n")
            if (reading_1[0].upper() == "E"):   #reading the first character of given input
                datas.append(float(reading_1[1:]))  #making the numeric data into float and adding it to list called datas 
                
            elif (reading_1[0].upper() == "U"):#mph
                datas.append(float(reading_1[1:])*1.609344) #converting into KPH, making the numeric data into float and adding it to list called datas
        
    if(datas):
        maximum=max(datas)  #finding maximum
        minumum=min(datas)  #finding manimum
        average=sum(datas)/len(datas)   #finding average
        
        print(f"Max Speed:{maximum/1.609344:.2f}MPH , {maximum:.2f}KPH")
        print(f"Min Speed:{minumum/1.609344:.2f}MPH , {minumum:.2f}KPH")
        print(f"Average speed:{average/1.609344:.2f}MPH , {average:.2f}KPH\n")


if __name__=="__main__":
    speed_analysis()