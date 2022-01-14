import sys
#class named euro_table
class euro_table():
    nations=""
    
    #initializing nations
    def __init__(self,nations):
        self.nations=nations
    
    #points, goal difference calculations 
    def calculation(self):
        win=loss=draw=match_played=for_team=against_team=diff=points=0
        for place in range(len(all_datas)):
            if self.nations in all_datas[place]:
                #indexing to see the position of final goals.
                nations_goal_index=all_datas[place].index(self.nations)+1
                rival_goal_index=4-nations_goal_index
                
                team_goal_scored=int(all_datas[place][nations_goal_index])
                team_goal_conceded=int(all_datas[place][rival_goal_index]) 
                match_played=match_played+1

                if team_goal_scored>team_goal_conceded:
                    win=win+1
                    points=points+3
                elif team_goal_scored<team_goal_conceded:
                    loss=loss+1
                else:
                    draw=draw+1
                    points=points+1
                
                for_team=for_team+team_goal_scored
                against_team=against_team+team_goal_conceded
                diff=for_team-against_team

   
        return[self.nations,match_played,win,draw,loss,for_team,against_team,diff,points]

value=sys.argv[1:]
for i in value:
    print(i.center(60),end="")
print("\n")

#opening and reading data from csv file
file=open("result.csv","r")
all_datas=file.readlines()
all_datas=[i.split(",") for i in all_datas]

#Obtaining countries from all datas
all_countries=list()
for i in all_datas:
    for a in range(0,4,2):
        all_countries.append(i[a])

#removing duplicate of countries
all_countries=list(set(all_countries))

#making table having datas
table=[]
for nations in all_countries:
    statistic=euro_table(nations)
    # print(stats.calculation())
    table.append(statistic.calculation())

#sorting the table according to goal difference 
for i in range(len(table)):
    for j in range(len(table)):
        if table[i][7]>table[j][7]:
            tmp=table[i]
            table[i]=table[j]
            table[j]=tmp
            
#sorting the table according to points
for i in range(len(table)):
    for j in range(len(table)):
        if table[i][8]>table[j][8]:
            tmp=table[i]
            table[i]=table[j]
            table[j]=tmp

print("P    W    D    L    F    A    DIFF PTS".center(78))
for details in table: 
    print(f"{details[0]:<20}{details[1]:<5}{details[2]:<5}{details[3]:<5}{details[4]:<5}{details[5]:<5}{details[6]:<5}{details[7]:<5}{details[8]:<5}")
