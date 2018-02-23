import json

location=[]
depname=[]
depid=[]


name=input("\n Enter name: ")
age=int(input("\n Enter age: "))
gender=input("\n Enter gender: ")
school= input ("\n Enter school name: ")
college=input("\n Enter college name: ")
company=input("\n Enter company name: ")
print("\n Reward is granted for performance above 50%")
pr=int(input("\n Enter performance rating (out of 100): "))

if pr<50:
    dist=False
else:
    dist=True


dic=dict({'Age':age,'Gender':gender,'Education':{'School':school,'College':college},'Company':company,'Rewardzzzz':dist})
with open('program1.json', 'w') as outfile:
    json.dump(dic,outfile,indent=4,separators=(',', ': '))
    outfile.write("\n }")
  
