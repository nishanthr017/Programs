print("ENTER STUDENT DETAILS:")
name=input("\nEnter name: ")
ph=input("\nEnter phone number:")
age=input("\nEnter age: ")
print("\nEnter marks:")
total=0
marks=[]
for i in range(5):
    s=input("\n Enter five marks (out of 50) :")
    marks.insert(i,s)
for i in range(5):
    total=total+marks[i]

print("\n STUDENT DETAILS ARE:")
print("\n Name: ",name)
print("\n Phone number: ",ph)
print("\n Age: ",age)
print("\n The marks are: ",marks)
print("\n Total marks is: ",total)
if total>125:
    print("\n Since total is greater than 125, student has passed!")
else:
    print("\n Since total is less than 125, student has failed!")


