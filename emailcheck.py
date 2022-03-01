import re   
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
def check(email):   
  
    while bool(re.search(regex,email))==False:   
        print("Invalid Email")
        email=input("enter your email again")
        print (email)
      
if __name__ == '__main__' :   
      
    email = input("enter an email") 
    check(email)  