#interger inputs
cred=0
credcom=0
credsem=0
semes=0


print("Please enter your name:")
name=input()
print(name, "how many credits have you completed?")
cred =int(input  ())
print(name, "how many credits do you need to complete your degree?")
credcom=int(input  ())
print(name, "how many credits do you typically take per semester?")
credsem=int(input  ())
semes=((credcom-cred)/credsem)
print(name,"you have", round(semes),"more semesters until you can graduate")



