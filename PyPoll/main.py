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




#loop through the list of candidates votes

most_votes=0
percent=[]
for i in candidate_votes:
      perc=round(vote_counter.get(i)/votes*100, 2)
      percent.append(perc)
      if vote_counter.get(i) > most_votes:
       most_votes=vote_counter.get(i)
       winner=i   



print("Election Results")
print("----------------")
print("Total Votes: "+ str(votes))
for i in range(len(candidate_votes)):
    print(f"{candidate_vote[i]}: {percent[i]}% {vote_counter.get(i)}")
print("----------------")
print("winner: "+ winner)
print("-----------------")
