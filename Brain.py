import sys
# reading files from dedicated paths
#sys.argv[1] path for '/etc/group'
#sys.argv[2] path for '/etc/passwd'

#creating custom error if file not found
try:
    groupFile=open(sys.argv[1])
except IOError as e:
    print ("I/O error- could not find the path({0}): error: {1}".format(sys.argv[1], e.strerror))
    sys.exit()

except:
    print ("Unexpected error:", sys.exc_info()[0])
    sys.exit()
    raise

try:
    passwdFile=open(sys.argv[2])
except IOError as e:
    print ("I/O error- could not find the path({0}): error: {1}".format(sys.argv[2], e.strerror))
    sys.exit()

except:
    print ("Unexpected error:", sys.exc_info()[0])
    sys.exit()
    raise

groupFileRead=groupFile.readlines()

passwdFileRead=passwdFile.readlines()

i=0
#moving the counter to skip initial comments from group file
while groupFileRead[i][0]=='#':
    i+=1
start=i
groupFileDict={}
#creating a dictionary where group id maps to group name
for i in range(start,len(groupFileRead)):
    l=groupFileRead[i].split(":")
    groupFileDict[l[2]]=l[0]

i=0
#moving the counter to skip initial comments from passwd file
while passwdFileRead[i][0]=='#':
    i+=1

start=i
finalJson={}
for i in range(start,len(passwdFileRead)):
    l=passwdFileRead[i].split(":")
    t={}
    t["uid"]=l[3]
    t["full name"]=l[4]
    if l[3] in groupFileDict:
        t["groups"]=[groupFileDict[l[3]]]
    else:
        t["groups"]=[]
    finalJson[l[0]]=t
print(finalJson)
