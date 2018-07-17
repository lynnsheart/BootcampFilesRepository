# File to load
#Dependencies
import os
import csv

csvPath = os.path.join('PyPoll', 'election_data.csv')
print(csvPath)

#Track paramaters for calculations
total_votes = 0

#read the csv
with open("election_data.csv") as poll_data:
   reader = csv.reader(poll_data)

#Set Variables
#Total Vote Counter
total_votes = 0

#Candidate Options
candidate_options = []
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

#Read the CSV and convert to list of dictionaries
with open("election_data.csv") as election_data:
    reader = csv.reader(election_data)
    
    #Read the header row
    header = next(reader)
    #print(header)
    
    #For each row...
    for row in reader:
        #run the loader animation
        #print"", end = ""

        #Add to the total vote count
        total_votes = total_votes + 1
        
        #Pull the candidate name from each row and print row
        candidate_name = row[2]
        #print(candidate_name)
        
        #If candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #add to the list of candidates in the running
            candidate_options.append(candidate_name)
            
            #Begin tracking that candidates votor count
            candidate_votes[candidate_name] = 0
        
        #Then add a vote to that candidates count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        
        print(candidate_votes)
        print('------------------')

#Print the results and export the data to text file
with open (csvPath, "w") as txt_file:
    
    #Print the final vote count to terminal
    election_results = (
        f"\n\nElection Results\n"
        f"----------------------"
        f"Total Votes: {total_votes}\n"
        f"---------------------------\n")
    print(election_results, end="")
    
    
    #Save the final vote count to the text file
    txt_file.write(election_results)
    
    #Determine the winner by looping through the counts
    for candidate in canidate_votes:
        
        #Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        
    #Print each candidates voter count and percentage to terminal
    voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    print(voter_output, end="")
    
    #Save each candidate's voter count and percentage to text file
    txt_file.write(voter_output)
        
#Print the winning candidate to terminal 
winning_candidate_summary = (
    f"----------------------\n"
    f"Winner: {winning_candidate_summary}\n"
    f"----------------------\n")
print(winning_candidate_summary)
    
#Save the winning candidate's name to the text file
txt_file.write(winning_candidate_summary)    