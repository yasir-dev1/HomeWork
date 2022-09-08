import csv

students={}
isom230Students=[]
acc200Students=[]
mkt110Students=[]
isomGrades=[]
accGrades=[]
mkttGrades=[]
StudentsClass={}
#Read The Students ids And Names
with open("students.csv") as file :
	myfile=csv.reader(file)
	for row in myfile:
		students.update({int(row[0]):row[1]})
		StudentsClass.update({int(row[0]):[]})
	print("Students List")
	print("ID\tName")
	for ID,Name in students.items():
		print(ID,"\t",Name)
	print("*-----------------------------------------------------------*")
def get_rsults(classlist,greadeslist,classname):
	print("list students in class")
	print("ID\tGrade\tName")
	for r in exam:
		classlist.append(int(r[0]))
		greadeslist.append(int(r[1]))
		StudentsClass[int(r[0])]+=[classname]
		print(int(r[0]),"\t",int(r[1]),"\t",students.get(int(r[0])))	
	print("*-----------------------------------------------------------*")

	print(len(classlist),"Students in class")
	print("The Max Grade is ",max(greadeslist))	
	print("The Min Grade is ",min(greadeslist))
	total=0
	for grade in greadeslist:
		total+=grade
	print("The Grades Averge is",total/len(greadeslist))
	print("*-----------------------------------------------------------*")
#Read The Results form files
with open("isom230.csv") as isom230:
	exam=csv.reader(isom230)
	print("The Results of isom230:")		
	get_rsults(isom230Students,isomGrades,"isom230")
with open("acc200.csv") as acc200:
	exam=csv.reader(acc200)
	print("The Results  of acc200:")	
	get_rsults(acc200Students,accGrades,"acc200")
with open("mkt110.csv") as mkt110:
	exam=csv.reader(mkt110)
	print("The Results  of mkt110:")
	get_rsults(mkt110Students,mkttGrades,"mkt110")		
print("List The Students Take All Courses:")
print("ID\tName")
for Student in acc200Students:
	if Student in isom230Students and Student in  mkt110Students:
		print(Student,students.get(Student))
print("*-----------------------------------------------------------*")

print("List The Students registered in  both isom230 and mkt110 :")
print("ID\tName")
for Student in isom230Students:
	if  Student in  mkt110Students:
		print(Student,students.get(Student))
print("*-----------------------------------------------------------*")

print("List The Students registered in acc200 but not in isom230 :")
print("ID\tName")
for Student in acc200Students:
	if  Student not in isom230Students:
		print(Student,students.get(Student))
print("*-----------------------------------------------------------*")


print("List The Students not  registered in Any Class :")
print("ID\tName")
for Student in students.keys():
	if  Student not in mkt110Students and acc200Students and isom230Students:
		print(Student,students.get(Student))
print("*-----------------------------------------------------------*")
def setLength(s, max_length):
    return (s + " " * max_length) [:max_length]
max_len=0
for ID,Classes in StudentsClass.items():
    StudentName=students.get(ID)
    for StudentID in StudentsClass.keys():
        if len(StudentName)>max_len:
            max_len=len(StudentName)
name=setLength("Name",max_len)
print("ID\t",name,"\tClasses")
for ID,Classes in StudentsClass.items():
    StudentName=students.get(ID)
    StudentName=setLength(StudentName,max_len)
    Classes=str(Classes).replace("[","").replace("]","").replace("'"," ",6).replace(" ","")
    print(ID,"\t",StudentName,"\t",Classes)