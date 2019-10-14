import pandas as pd 

df = pd.read_csv("techrep.csv")

state_college = {}
state_college_list = []
state_college_list.append(["State", "Techrep Count"])

for i in df["State College"]:
	if i not in state_college.keys():
		state_college[str(i)] = 1
	else:
		state_college[str(i)] +=1

for key, value in state_college.items():
    temp = [str(key),int(value)]
    state_college_list.append(temp)

source = {}
source_list = []
source_list.append(["Source", "Count"])

for i in df["Source"]:
	if i not in source.keys():
		source[str(i)] = 1
	else:
		source[str(i)] +=1

for key, value in source.items():
    temp = [str(key),int(value)]
    source_list.append(temp)

month = {}
month_list = []
month_list.append(["Month", "Count"])
for i in df["Joined On"]:
	if i.split(" ")[0] not in month.keys():
		month[str(i.split(" ")[0])] = 1
	else:
		month[str(i.split(" ")[0])] += 1

for key, value in month.items():
    temp = [str(key),int(value)]
    month_list.append(temp)

print(state_college_list)
print(source_list)
print(df["College"].nunique())
print(month_list)
