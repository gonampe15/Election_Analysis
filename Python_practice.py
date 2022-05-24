counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
print(counties_dict)


for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)    

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))



voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


for i in range(len(voting_data)):

      print(voting_data[i]['county'])


for county_dict in voting_data:
    for value in county_dict.values():
        print(value)      


for county_dict in voting_data:

     print(county_dict['registered_voters'])


for county, registeredvoters in voting_data.items():
    print(f"{county} county has {registeredvoters} registered voters.")