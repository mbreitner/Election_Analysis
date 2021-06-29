#x = 0 
#while x<= 5:
    #print(x)
    #x=x+1

count = 7
while count < 1:
    print("Hello World!")

counties = ["Arapahoe", "Denver", "Jefferson"]
#for county in counties:
    #print(county)

numbers = [0, 1, 2, 3, 4]
#for num in numbers:
    #print(num)

#for num in range(5):
    #print(num)

#for i in range(len(counties)):
    #print(counties[i])

#counties dictionary that will be used for for loops
counties_dict = {
    "Arapahoe": 422829,
    "Denver": 463353,
    "Jefferson": 432438}

#different ways to write the for loop to get keys and values data
#for county in counties_dict:
    #print(county)

#for county in counties_dict.keys():
    #print(county)

#for voters in counties_dict.values():
    #print(voters)

#for county in counties_dict:
    #print(counties_dict[county])

#for county in counties_dict:
    #print(counties_dict.get(county))

#for key, value in counties_dict.items():
    #print(key,value)

#for county, voters in counties_dict.items():
    #print(county,voters)

#for county, voters in counties_dict.items():
    #print(county, str("county has"), value, str("registered voters."))

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
    #print(county_dict)

#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)

## find only the number of registered voters in each county
for county_dict in voting_data:
    print(county_dict['registered_voters'])
## to find the county only replace 'registered voters' with 'county in the last line
for county_dict in voting_data:
    print(county_dict['county'])
