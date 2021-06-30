counties_dict = {
    "Arapahoe": 422829,
    "Denver": 463353,
    "Jefferson": 432438}
print(counties_dict)

print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
print(counties_dict["Arapahoe"])

voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"County":"Jefferson", "registered_voters": 432438})
print(voting_data)
print(len(voting_data))
voting_data.insert(0,{"county":"El Paso", "registered_voters": 461149})
print(voting_data)
voting_data.remove({"county": "Arapahoe", "registered_voters": 422829})
print(voting_data)
voting_data.insert(1,{"county": "Jefferson", "registered_voters": 432438})
voting_data.insert(2,{"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.remove({"county": "Denver", "registered_voters": 463353})
voting_data.pop(3)
print(voting_data)

## You can append a dictionary to a list