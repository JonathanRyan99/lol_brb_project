from fuzzywuzzy import process

championsDict = {}


with open("champions.txt") as file:
	for line in file:
		data = line.split()
		championsDict[data[0]] = data[1]


def get_matches(query,options,limit):
	results = process.extract(query,options,limit=limit)
	return results


#this returned ashe as a 90% match 


sample = "Fizz"

try:
	mastery = championsDict[sample]
	
	print("champion found: ",sample,"mastery: ",mastery)
except:
	print("champion not found")
	matches = get_matches(sample,championsDict,2)
	print(matches)

