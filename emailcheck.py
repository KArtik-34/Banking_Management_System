import re   
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
def check(email):   
  
    if(re.search(regex,email)):   
        pass   
    else:   
        print("Invalid Email")
        n=input("enter your email again")
        print (n)   
      
if __name__ == '__main__' :   
      
    email = input("enter an email") 
    check(email)  