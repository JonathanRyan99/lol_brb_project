championsDict = {}


with open("champions.txt") as file:
	for line in file:
		data = line.split()
		championsDict[data[0]] = data[1]

print(championsDict["Poppy"])
print(len(championsDict))