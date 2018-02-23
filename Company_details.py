import json

location=[]
depname=[]
depid=[]

dic={}


cname=input("\n Enter company name: ")
nloc=int(input("\n Enter number of locations the company has: "))
for i in range(1,nloc+1):
    print("\n Enter location ",i," :")
    loci = input()
    location.insert(i,loci)
    ndep=int(input("\n Enter number of depts. in this location: "))
    dic1=dict({'Location':loci})
    for j in range(1,ndep+1):
        print("\n Enter dept. ",j,"name :")
        depnamei=input()
        depname.insert(j,depnamei)  
        print("\n Enter dept. ",j,"ID :")
        depidi=input()
        depid.insert(j,depidi)
        dic2=dict({'Department':{'Department name':depnamei,'Department ID':depidi}})
    dic1.update(dic2)
with open('data.json', 'w') as outfile:
        outfile.write("{\"%s\"" ": "%cname)
        json.dump(dic1,outfile,indent=4,separators=(',', ': '))
        outfile.write("\n }")
