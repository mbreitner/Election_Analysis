print("Hello World")
## math Equations
5+2*3
8//5-3
8+22*2-4
16-3/2+7-1
3**3%5
5+9*3/2-4

(5+2)*3
(8//5)-3
8+(22*(2-4))
16-3/(2+7)-1
3**(3%5)
5+(9*3/2-4)
5+(9*3/(2-4))

##Lists
counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)
print(counties[0])
print(counties[2])
print(counties[-1])
print(len(counties))
print(counties[0:2])
print(counties[0:1])
print(counties[:2])
print(counties[1:])
counties.append("El Paso")
print(counties)
counties.insert(2,"El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
counties.pop(3)
print(counties)
counties[2] = "El Paso"
print(counties)
counties.remove("El Paso")
counties.append("Jefferson")
counties[2] = "El Paso"
counties[2] = "Jefferson"
counties.insert(1,"El Paso")
counties.remove("Arapahoe")
counties.insert(2, "Denver")
counties.remove("Denver")
counties.insert(3,"Denver")
counties.remove("Denver")
counties.append("Arapahoe")
print(counties)


# Import the datetime class from the datetime module.
import datetime as dt
#use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
#print the present time.
print("The time right now is ", now)

#import a csv file
import csv
dir(csv)

#finding fuctions in a dictionary
dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})

#finding functions in a string
dir(str)



# Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file. 
with open(file_to_load) as election_data:
# Print the file object
    print(election_data)

#create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Using the open () function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
#using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
#write some data to the filte.
outfile.write("Hello World")
# close the file
outfile.close()

# using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

#write some data to the file. 
    txt_file.write("Counties in the election\n-----------------\nArapahoe\nDenver\nJefferson")
# to do it comma separate do variabale.write("x, x, x")
#to put it on a new line do variable.write("x\nx\nx\n")