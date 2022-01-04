import sys 
team=list()
tmp_list=list()
result=open("result.csv","r")
tmp=result.readlines()
result.seek(0)

for i in range(len(tmp)):
    split=result.readline().strip().split(",")
    tmp_list.extend(split)

nations = [tmp_list[i] for i in range(len(tmp_list)) if i%2==0]
print(list(set(nations)))
result.close()
# class euro_table:
#     def __init__(self,nations):
#         self.nations=nations
#     def score():
#         match_played=win=draw=lose=goal_for=goal_against=goal_difference=0
        


