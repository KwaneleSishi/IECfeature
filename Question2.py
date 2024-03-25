#Question 2: Data structures and algorithms

"""Write a python function named “register_party” that takes a list of parties. Each party
must be presented by key value pairs. The keys should be “party_name”, “reg_number”,
“member_count”). The function should check if the new party has acceptable number of
members for it to be registered as per the requirements narrated in the scenario."""

parties=[]
def register_party(party_name, reg_number,member_count):
     parties.append({
        "party_name": party_name,
        "reg_number": reg_number,
        "member_count": member_count,
    })



def update_voter_info(voter_id, name, voting_district, has_voted=False):
    voter_info = {}

    if voter_id not in voter_info:
        voter_info[voter_id] = {
            'name': name,
            'voting_district': voting_district,
            'has_voted': False,
        }

    # Updating the voter's information
    voter_info[voter_id]['name'] = name
    voter_info[voter_id]['voting_district'] = voting_district

    if has_voted:
        print("Voter has already voted!")

    # Update the voter's has_voted status if the voter has voted
    if not has_voted and voter_info[voter_id]['has_voted']:
        voter_info[voter_id]['has_voted'] = True

    return voter_info[voter_id] 

#2.4 Using list comprehension and the filter function, write a piece of code that filters out all
#parties from a given list that have less than 1,000 members
my_list=[ "ASD", "ATM", "AASD", "ANC", "AGANGSA", "ALJAMA", "ATA", "AZAPO", "APC","BRA", "BLF", "ZACP", "CPM", "CSA", "COPE", "DA", "DLC", "ECOFORUM", "EFF", "F4SD", "FREE DEMS"]

# Adding a dictionary representation of each party to my_list
my_list = [{"name": name, "members": members} for name, members in zip(my_list, [5000, 1200, 1500, 2000, 800, 750, 1200, 1000, 900, 1200, 1000, 1250, 1500, 1600, 2200, 3300, 1200, 1500, 4500, 1000, 2000])]

# Filtering out parties with less than 1,000 members
acceptable_parties_with_members = [party for party in filter(lambda x: x["members"] >= 1000, my_list)]

print(acceptable_parties_with_members)

#2.5 Rewrite the list comprehension in question 2.4 into a normal list data structure
my_list=[ "ASD", "ATM", "AASD", "ANC", "AGANGSA", "ALJAMA", "ATA", "AZAPO", "APC","BRA", "BLF", "ZACP", "CPM", "CSA", "COPE", "DA", "DLC", "ECOFORUM", "EFF", "F4SD", "FREE DEMS"]

# Add a dictionary representation of each party to my_list
party_dicts = []
for name, members in zip(my_list, [5000, 1200, 1500, 2000, 800, 750, 1200, 1000, 900, 1200, 1000, 1250, 1500, 1600, 2200, 3300, 1200, 1500, 4500, 1000, 2000]):
    party_dicts.append({
        "name": name,
        "members": members,
    })

# Filter out parties with less than 1,000 members
acceptable_parties = []
for party in filter(lambda x: x["members"] >= 1000, party_dicts):
    acceptable_parties.append(party)

print(acceptable_parties)








