# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the followng tasks to complete the election audit of a recent congressional election. 

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of cotes each candidate won. 
5. Determine the winner of the election based on popular vote. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.8, Visual Studio Code 1.57.1

## Pre-Challenge Summary
The Analysis of the election show that:
- There were "369,711" votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number votes.
- The winner of the election was:
  - Diana Degette, who received 73.8% of the vote and 272,892 number of votes. 

## Challenge Overview
The challenge was to add additional information to our election analysis. Tom and Seth needed to know which county's the votes came from and which county had the most votes on top of knowing which candidate won the election. We had to add to our exisiting code to identify the county data. 

## Challenge Summarry
Once the additional code was added, you can see the final outcome of the election below. 
- How many votes were cast in this congressional election?
Overall, there were 369,711 votes cast in the election 

![Total_Election_Votes](https://user-images.githubusercontent.com/84791455/124313122-47cfb680-db25-11eb-81ea-47f5416eaf9f.PNG)


- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
The county votes are as follows:
  - Jefferson: 38,555 votes (10.5%)
  - Denver: 306,055 votes (82.8%)
  - Arapahoe: 24,801 votes (6.7%)
  
![County_Votes](https://user-images.githubusercontent.com/84791455/124313362-a1d07c00-db25-11eb-8944-d52afe0bc6d6.PNG)


- Which county had the largest number of votes?
Denver had the largest number of votes with a total of 306,055

![Largest_County_Turnout](https://user-images.githubusercontent.com/84791455/124313488-c88eb280-db25-11eb-962f-27479d8a10ee.PNG)


- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
The breakdown of candidates are as follows:
  - Charles Casper Stockham: 85,213 votes (23.0%)
  - Diana DeGette: 272,892 votes (73.8%)
  - Raymon Anthony Doane; 11,606 votes (3.1%)
  
![Election_Candidates](https://user-images.githubusercontent.com/84791455/124313716-1d322d80-db26-11eb-9c01-5070f8cd7696.PNG)


- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
Diana DeGette was the winner of the election with 272,892 votes that counted for 73.8% of the total vote count. 

![Winning_Candidate](https://user-images.githubusercontent.com/84791455/124313838-4d79cc00-db26-11eb-8f02-f18d7ec9213a.PNG)


## Election-Audit Summary
This script can easily be used for other elections moving forward. First our file_to_load variable can be updated to load a file from a different CSV file with results from a different election. That will help to provide a list of other candidates and county's from other areas. 

![file_to_load](https://user-images.githubusercontent.com/84791455/124314409-338cb900-db27-11eb-9ba2-f4ee3474b780.PNG)


Another way this can be used again in the future is because we left our total vote counter, candidate option list, candidate votes dictionary, county list, county vote dictionary, and then the winning candidate and largest county variables open. This means, with the code we wrote to populate those variables can be used with any data set that has that information included and it will populate our emoty variables accordingly. 

![empty_variables](https://user-images.githubusercontent.com/84791455/124314484-50c18780-db27-11eb-92d3-e0527242a60c.PNG)





