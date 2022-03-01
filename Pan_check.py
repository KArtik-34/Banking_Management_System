
first_name=input("frst: ")
last_name=input("last: ")
first_name=first_name.rstrip()
first_name=first_name.lstrip()
first_name=first_name.capitalize()
last_name=last_name.capitalize()
name = first_name+" "+last_name
print(name)
pan = input("Enter your pan no.: ")

while pan.isupper()==False:
    pan=input("Pan no. should be in uppercase'CAPITALIZED'\nEnter your pan no.")

while len(pan)!=10:
    pan = input("pan not of correct length\nEnter your pan no.: ")

pan2=(pan[5:9])
while pan2.isnumeric()==False:
    pan = input("Invalid pan no.\nEnter your pan no.: ")
    pan2=(pan[5:9])
pan_nm=str(last_name[:1])
pan1=str(pan[4:5])
while pan_nm not in pan1:
    pan = input("invalid\nEnter your pan no.: ")
    pan1=str(pan[4:5])
pan_=["P","C","A","F","H","T"]

pan0=str(pan[3:4])
while pan0 not in pan_:
    pan = input("invalid Pan no. \nEnter the name of a pan no.: ")
    pan0=str(pan[3:4])

pan3=str(pan[9:10])
while pan3.isalpha()==False:
    pan=(input("Invalid Pan\n Enter your pan no.:"))
    pan3=str(pan[9:10])