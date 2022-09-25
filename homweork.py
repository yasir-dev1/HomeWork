import csv

students={}
isom230students=[]
acc200students=[]
mkt110students=[]
isomGrades=[]
accGrades=[]
mkttGrades=[]
studentsclass={}
#Read The students idss And Names
with open("students.csv") as file :
	myfile=csv.reader(file)
	for row in myfile:
		students.update({row[0]:row[1]})
		studentsclass.update({row[0]:[]})
	print("students List")
	print("id\tName")
	for ids,Name in students.items():
		print(ids,"\t",Name)
	print("*-----------------------------------------------------------*")
def get_rsults(classlist,greadeslist,classname):
	print("list students in class")
	print("id\tGrade\tName")
	for r in exam:
		classlist.append(r[0])
		greadeslist.append(int(r[1]))
		studentsclass[r[0]]+=[classname]
		print(int(r[0]),"\t",int(r[1]),"\t",students.get(r[0]))	
	print("*-----------------------------------------------------------*")

	print(len(classlist),"students in class")
	print("The Max Grade is ",max(greadeslist))	
	print("The Min Grade is ",min(greadeslist))
	total=sum(greadeslist)
	print("The Grades Averge is",total/len(greadeslist))
	print("*-----------------------------------------------------------*")
#Read The Results form files
with open("isom230.csv") as isom230:
	exam=csv.reader(isom230)
	print("The Results of isom230:")		
	get_rsults(isom230students,isomGrades,"isom230")
with open("acc200.csv") as acc200:
	exam=csv.reader(acc200)
	print("The Results  of acc200:")	
	get_rsults(acc200students,accGrades,"acc200")
with open("mkt110.csv") as mkt110:
	exam=csv.reader(mkt110)
	print("The Results  of mkt110:")
	get_rsults(mkt110students,mkttGrades,"mkt110")		
print("List The students Take All courses:")
print("id\tName")
for student in acc200students:
	if student in isom230students and student in  mkt110students:
		print(student,students.get(student))
print("*-----------------------------------------------------------*")

print("List The students registered in  both isom230 and mkt110 :")
print("id\tName")
for student in isom230students:
	if  student in  mkt110students:
		print(student,students.get(student))
print("*-----------------------------------------------------------*")

print("List The students registered in acc200 but not in isom230 :")
print("id\tName")
resultid="".join(set(acc200students)-set(isom230students))
print(resultid,"\t",students.get(resultid))
print("*-----------------------------------------------------------*")

print("List The students not  registered in Any class :")
print("id\tName")
result=list(set(students.keys())-set(set(acc200students) and set(isom230students) and set(mkt110students)))
ids="\n".join(result)
names=[]
for name in result:
	names.append(name)
names="\n".join(names)
print(ids,"\t",names)

print("id\tName\tclasses")
for ids,classes in studentsclass.items():
    studentName=students.get(ids)
    classes=",".join(classes)
    print(ids,"\t",studentName,"\t",classes)
