from selectors import SelectSelector
# INPUT INTEGER VALUES OF VOTER REGISTRATION SUMMARY
Voters= [1029, 20192, 39402, 83013, 29448]


# COMPUTATIONS
Total= sum(Voters)
Maximum= max(Voters)
Minimum= min(Voters)
Average= Total/len(Voters)
# FORMATTED STRING
print(
    f'VOTERS REGISTRATION SUMMARY \n'
    f'Total Registered Voters: {Total} \n'
    f'Maximum Registered was {Maximum} \n'
    f'Minimum Registered was {Minimum} \n'
    f'Average Registation: {Average}'
)

# BOOLEAN: THRESHOLD CONDITIONAL STATEMENT
Threshold = 30000
if Average >= Threshold:
    print('STATUS ABOVE')
else:
    print('STATUS BELOW')
# LISTS: and modifications
Names = ['Kigali', 'North', 'South', 'East', 'West']
print("Before Modification" , Names)
Names.append("Western Province")
if "West" in Names:
    Names.remove("West")
Names.sort()
print("After Modification" , Names)

# ARRAYS QUESTION
import array
subset_counts = array.array('i', Voters[:3])
array_sum = sum(subset_counts)
print(f"Array subset values: {subset_counts.tolist()}")
print(f"Sum of array subset: {array_sum}")
print(f"Comparison with list total: {Total}")
# DICTIONARIES

voter_records = [
    {"id": 0, "name": "Kigali", "value": 1029},
    {"id": 1, "name": "North", "value": 20192},
    {"id": 2, "name": "South", "value": 39402},
    {"id": 3, "name": "East", "value": 29448}, ]


voter_records[0]["value"] = 50000 # FOR KIGALI

voter_records = [record for record in voter_records if record["name"] != "West"]

total_record_voters = sum(record["value"] for record in voter_records)

print("Updated Voter Records:")
for record in voter_records:
    print(record)

print(f"Total voters across updated records: {total_record_voters}")

