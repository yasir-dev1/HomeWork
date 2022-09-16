import csv 

skyscrapers={}
with open("skyscrapers.csv") as file :
	reader=csv.reader(file)
	for row in reader:
		skyscrapers.update({row[0]:int(row[1])})

print("The count of  Skyscrapers in kuwait is:",skyscrapers.get("Kuwait"))

print("The count of  Skyscrapers in Bahrain is:",skyscrapers.get("Bahrain"))

total=sum(list(skyscrapers.values()))
avarge=total/len([skyscrapers.values()])

print("The Avarge of Skyscrapers in all countries is:",avarge)	
print("--------------------------------------------------------")

print("Country \t Number")
for c,s in skyscrapers.items():
	print(c,":",s)
print("-------------------------------------------------------")
all_values = skyscrapers.values()
least_num=min(all_values)
least_country=min(skyscrapers,key=skyscrapers.get)
print("The Country With  Least Skyscrpaers number is:")
print("Country:",least_country)
print("Number:",least_num)
