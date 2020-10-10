#import
import os
import csv

#make path
csvpath='/Users/kimkockenmeister/Desktop/hw3/python_HW3/PyPoll/Resources/election_data.csv'
#open file
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    if csv.Sniffer().has_header:
        next(csvreader)


    #initialize variables
    votes = 0    
    candidate_votes = []
    vote_counter={}

    for row in csvreader:
        #count up all the votes
        votes+=1

        #tell them where to look for candidates
        candidates=row[2]
        #list comprehension to find votes per candidate
        if candidates not in candidate_votes:
        #candidate index becomes the index of whereever they are in the list
            candidate_votes.append(candidates)

            # track that candidate's voter count
            vote_counter[candidates] = 0
            
        # Then add a vote to that candidate's count
        vote_counter[candidates] = vote_counter[candidates] + 1
print("Election Results")
print("----------------")
print("Total Votes: "+ str(votes))



#loop through the list of candidates votes

most_votes=0
percent=[]
for i in candidate_votes:
    votecount=vote_counter.get(i)
    perc=round(float(votecount)/float(votes)*100,2)
    percent.append(perc)
    if vote_counter.get(i) > most_votes:
        most_votes=vote_counter.get(i)
        winner=i   
    #print(f" {i} {perc} {votecount} ")
    print(f"{i}: {perc}% ({vote_counter[i]})")
    #print(i+ "%"+ str(perc) +vote_counter.get(i))
    
   # print(f"hello world")
print("----------------")
print("winner: "+ winner)
print("-----------------")

txt_file= open("analysis.txt", "w")
txt_file.write("Election Results\n")
txt_file.write("Election Results\n")
txt_file.write("----------------\n")
txt_file.write("Total Votes: "+ str(votes)+"\n")
txt_file.write(f"{i}: {perc}% ({vote_counter[i]})")
txt_file.write("----------------" + "\n")
txt_file.write("winner: "+ winner+"\n")
txt_file.write("-----------------"+ "\n")