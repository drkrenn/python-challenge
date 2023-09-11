import os
import csv
import pandas as pd

total_votes = 0
candidate_list=[]
votes1 = 0
votes2 = 0
votes3 = 0
with open("C:\\Users\\dkrenn\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv") as poll_data:
    reader = csv.reader(poll_data)    
    header = next(reader)      
    for row in reader:
        total_votes += 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])


candidate1 = candidate_list[0]
candidate2 = candidate_list[1]
candidate3 = candidate_list[2]

with open("C:\\Users\\dkrenn\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv") as poll_data:
    reader = csv.reader(poll_data)    
    header = next(reader)    
    for row in reader:
        if row[2] == (candidate1):
            votes1=votes1+1
        if row[2]==(candidate2):
            votes2 = votes2+1
        if row[2] == (candidate3):
            votes3 = votes3+1


percent1=round(votes1/total_votes*100,3)
percent2=round(votes2/total_votes*100,3)
percent3=round(votes3/total_votes*100,3)


if int(votes1)>int(votes2) & int(votes1)>int(votes3):
    winner=str(candidate1)

if int(votes3)>int(votes1) & int(votes3)>int(votes2):
    winner=str(candidate3)
    
else: 
    winner=str(candidate2)


print("Election Results")
print("___________________________")
print("Total Votes: " + str(total_votes))
print("___________________________")
print(candidate1+": "+str(percent1)+"% ("+str(votes1)+")")
print(candidate2+": "+str(percent2)+"% ("+str(votes2)+")")
print(candidate3+": "+str(percent3)+"% ("+str(votes3)+")")
print("___________________________")
print("Winner: "+str(winner))
print("___________________________")

with open("Polls", "w") as txt_file: 
    txt_file.write("Election Results\n")
    txt_file.write("___________________________\n")
    txt_file.write("Total Votes: " + str(total_votes)+"\n")
    txt_file.write("___________________________\n")
    txt_file.write(candidate1+": "+str(percent1)+"% ("+str(votes1)+")\n")
    txt_file.write(candidate2+": "+str(percent2)+"% ("+str(votes2)+")\n")
    txt_file.write(candidate3+": "+str(percent3)+"% ("+str(votes3)+")\n")
    txt_file.write("___________________________\n")
    txt_file.write("Winner: "+str(winner)+"\n")
    txt_file.write("___________________________")