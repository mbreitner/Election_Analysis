# Add our dependencies. 
import csv
import os
# Assign a variable to load a file from a path. 
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate options
candidate_options = []

#candidate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file. 
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # read the header row.
    headers = next(file_reader)
    #print each row in the CSV file.
    for row in file_reader:
        # 2. add to the total vote count.
        total_votes += 1
    # print the candidate name from each row
        candidate_name = row[2]
    # If the candidate does not match an existing candidate...
        if candidate_name not in candidate_options:
        # add it to the list of candidates.
            candidate_options.append(candidate_name)
        # begin tracking the candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1
#save the results to our text file. 
with open(file_to_save, "w") as txt_file:
    #print the final vote count to the terminal
    election_results = (
        f"Election Results\n"
        f"----------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    #print each candidate, their voter count, and percentage to the terminal 
    
    #Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #print the candidate name and percecntage of votes.
        

        #determine winning vote count and candidate
        #deterime if the votes are greater than the winning count.
        if (votes>winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
    # to do: print out each candidate's name, vote count, and percentage of votes to the terminal
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #print each candidate, their voter count, and percentage to the terminal 
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results, end="")
    # save the candidate results to our text file
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"----------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------\n")
    print(winning_candidate_summary)
    #save the winning candidates name to the text file
    txt_file.write(winning_candidate_summary)
        


    

# The data we need to retrieve

# 1. The total number of votes cast
        # 369711
# 2. A complete list of candidates who reveived votes
        # ['Raymon Anthony Doane', 'Diana DeGette', 'Charles Casper Stockham']
# 3. The percentage of votes each candidate won
        #Charles Casper Stockham: received 23.05% of the vote.
        #Diana DeGette: received 73.81% of the vote.
        #Raymon Anthony Doane: received 3.14% of the vote.
# 4. The total number of votes each candidate won
        #'Charles Casper Stockham': 85213, 'Raymon Anthony Doane': 11606, 'Diana DeGette': 272892
# 5. The winner of the election based popular vote. 

