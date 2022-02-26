
'''          Bank Management System
   Made By: Kartikay patni & harsh singh kharayat
                  2021-2022'''

from ast import Pass
import ctypes
import sys
from time import sleep
import mysql.connector
from datetime import date

def delete_last_line():

    #cursor up one line
  sys.stdout.write('\x1b[1A')

    #delete last line
  sys.stdout.write('\x1b[2K')

def clear():
  for _ in range(65):
     print()

def customer_record():
  conct = mysql.connector.connect(host='localhost', database='bank_management_system', user='root', password='1234') #Connection for mysql Database
      
  cursor = conct.cursor()
  sql ="select * from customer;"
  cursor.execute(sql)
  results = cursor.fetchall()
  clear()
  print('Customer Records')
  print('-'*120)
  for result in results:
    print(result[0], result[1], result[2], result[3], result[4], result[5],result[6], result[7], result[8])
  print('-'*120)
  conct.close()
  wait = input('\nPress any key to continue....')

def account_status(acno):
  conct = mysql.connector.connect(
      host='localhost', database='bank_management_system', user='root', password='1234')
  cursor = conct.cursor()
  sql ="select status,balance from customer where acno ='"+acno+"'"
  result = cursor.execute(sql)
  result = cursor.fetchone()
  conct.close()
  return result

def deposit_amount(): #creating a function for depositing amount
    conct = mysql.connector.connect(
        host='localhost', database='bank_management_system', user='root', password='1234')
    cursor = conct.cursor()
    clear()
    acno = input('Enter account No :')
    amount = input('Enter amount :')
    today = date.today()
    result = account_status(acno)
    if result [0]== 'active':
      sql1 ="update customer set balance = balance+"+amount + ' where acno = '+acno+' and status="active";'
      sql2 = 'insert into transaction(amount,type,acno,dot) values(' + amount +',"deposit",'+acno+',"'+str(today)+'");'
      cursor.execute(sql2)
      cursor.execute(sql1)
      #print(sql1)
      #print(sql2)
      print('\n\namount deposited')

    else:
      print('\nClosed or Suspended Account....')
    
    wait= input('\n Press any key to continue....')
    conct.close()


def withdraw_amount(): #crearing a funtion for withdraw money 
    conct = mysql.connector.connect(
        host='localhost', database='bank_management_system', user='root', password='1234')
    cursor = conct.cursor()
    clear()
    acno = input('Enter account No :')
    amount = input('Enter amount :')
    today = date.today()
    result = account_status(acno)
    if result[0] == 'active' and int(result[1])>=int(amount):
      sql1 = "update customer set balance = balance-" + \
          amount + ' where acno = '+acno+' and status="active";'
      sql2 = 'insert into transaction(amount,type,acno,dot) values(' + \
          amount + ',"withdraw",'+acno+',"'+str(today)+'");'

      cursor.execute(sql2)
      cursor.execute(sql1)
      #print(sql1)
      #print(sql2)
      print('\n\namount Withdrawn')

    else:
      print('\nClosed or Suspended Account.Or Insufficient amount')

    wait = input('\nPress any key to continue....')
    conct.close()

def transaction_menu():# creating a function for transaction menu
    while True:
      clear()
      print(' Trasaction Menu')
      print("\n1.  Deposit Amount")
      print('\n2.  WithDraw Amount')
      print('\n3.  Back to Main Menu')
      print('\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        deposit_amount()   #using the above fuction   
      if choice == 2:
        withdraw_amount()    
      if choice == 3:
        break

def search_menu(): # creating search menu
    conct = mysql.connector.connect(
       host='localhost', database='bank_management_system', user='root', password='1234')
    cursor = conct.cursor()
    while True:
      clear()
      print(' Search Menu')
      print("\n1.  Account No")
      print('\n2.  Aadhar Card')
      print('\n3.  Phone No')
      print('\n4.  Email')
      print('\n5.  Names')
      print('\n6.  Back to Main Menu')
      print('\n')
      choice = int(input('Enter your choice ...: '))
      field_name=''
   
      if choice == 1:
        field_name ='acno'
  
      if choice == 2:
        field_name ='aadhar_no'
   
      if choice == 3:
        field_name = 'phone'
      
      if choice == 4:
        field_name = 'email'

      if choice == 5:
        field_name = 'name'
      
      if choice == 6:
        break
      msg ='Enter '+field_name+': '
      value = input(msg)
      if field_name=='acno':
        sql = 'select * from customer where '+field_name + ' = '+value+';'
      else:
        sql = 'select * from customer where '+field_name +' like "%'+value+'%";'
      #print(sql)
      cursor.execute(sql)
      records = cursor.fetchall()
      n = len(records)
      clear()
      print('Search Result for ', field_name, ' ',value)
      print('-'*80)
      for record in records:
       print(record[0],",", record[1],",", record[2],",", record[3],",",
             record[4],",", record[5],",", record[6],",", record[7],",", record[8])
      if(n <= 0):
        print(field_name, ' ', value, ' does not exist')
      wait = input('\n Press any key to continue....')

    conct.close()
    wait=input('\n Press any key to continue....')

def daily_report():
   clear()
   
   conct = mysql.connector.connect(
       host='localhost', database='bank_management_system', user='root', password='1234')
   today = date.today()
   cursor = conct.cursor()
   sql = 'select tid,dot,amount,type,acno from transaction t where dot="'+ str(today)+'";'
   cursor.execute(sql)
   records = cursor.fetchall()
   clear()
   print('Daily Report :',today)
   print('-'*120)
   for record in records:
       print(record[0], record[1], record[2], record[3], record[4])
   print('-'*120)

   conct.close()
   wait = input('\n Press any key to continue....')


def monthly_report():
   clear()

   conct = mysql.connector.connect(
       host='localhost', database='bank_management_system', user='root', password='1234')
   today = date.today()
   cursor = conct.cursor()
   sql = 'select tid,dot,amount,type,acno from transaction t where month(dot)="' + \
       str(today).split('-')[1]+'";'
   cursor.execute(sql)
   records = cursor.fetchall()
   clear()
   print(sql)
   print('Monthly Report :', str(today).split(
       '-')[1], '-,', str(today).split('-')[0])
   print('-'*120)
   for record in records:
       print(record[0], record[1], record[2], record[3], record[4])
   print('-'*120)

   conct.close()
   wait = input('\n Press any key to continue....')

def account_details():
    clear()
    acno = input('Enter account no :')
    conct = mysql.connector.connect(
        host='localhost', database='bank_management_system', user='root', password='1234')
    cursor = conct.cursor()
    sql ='select * from customer where acno ='+acno+';'
    sql1 = 'select tid,dot,amount,type from transaction t where t.acno='+acno+';'
    cursor.execute(sql)
    result = cursor.fetchone()
    clear()
    print('Account Details')
    print('-'*120)
    print('Account No :',result[0],'\n')
    print('Customer Name :',result[1],'\n')
    print('Address :',result[2],'\n')
    print('Phone NO :',result[3],'\n')
    print('Email ID :',result[4],'\n')
    print('Aadhar No :',result[5],'\n')
    print('Account Type :',result[6],'\n')
    print('Account Status :',result[7],'\n')
    print('Current Balance :',result[8],'\n')
    print('-'*120)
    cursor.execute(sql1)
    results = cursor.fetchall()
    for result in results:
        print(result[0], result[1], result[2], result[3])

    conct.close()
    wait=input('\nPress any key to continue.....')

def report_menu():
    while True:
      clear()
      print(' Report Menu')
      print("\n1.  Daily Report")
      print('\n2.  Monthly Report')
      print('\n3.  Account Details')
      print('\n4.  Customer Records')
      print('\n5.  Back to Main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        daily_report()
      if choice == 2:
        monthly_report()
      if choice == 3:
        account_details()
      if choice == 4:
        customer_record()
      if choice == 5:
        break
def add_account():
    conct = mysql.connector.connect(
        host='localhost', database='bank_management_system', user='root', password='1234')
    cursor = conct.cursor()
   
    name = input('Enter Name : ')
    addr = input('Enter address : ')
    
    phone = (input('Enter Phone no : '))
    while len(phone) != 10 or not phone.isdigit():
     print('You have not entered a 10 digit value! Please try again.')
     phone = input('Please input your 10 digit phone number no. : ')
    email = input('Enter Email : ')
    while "@" not in email:      # this will check if email id is correct or not
      email = input("Your email address must have '@' in it\nPlease write your email address again: ")
      if len(email) <= 6 :
        email = input("Your email address is too short\nPlease write your email address again: ")
      if "." not in email:
        email = input("Your email address must have '.' in it\nPlease write your email address again: ")
    while "." not in email:
      email = input("Your email address must have '.' in it\nPlease write your email address again: ")
      if len(email) <= 6 :
        email = input("Your email address is too short\nPlease write your email address again: ")
      if "@" not in email:
        email = input("Your email address must have '@' in it\nPlease write your email address again: ")
     
    
    adr = input('Enter AAdhar no :')
    while len(adr) != 12 or not adr.isdigit():
      print('You have not entered a 12 digit value! Please try again.')
      adr = input('Please input your 12 digit AAdhar no. : ')
    aadhar = (adr[:4]+"-"+adr[4:8]+"-"+adr[8:12])
    actype = input('Account Type (saving/current ) :') 
      
    balance =(input('Enter opening balance , min = 5000/- : '))
  
    sql = 'insert into customer(name,address,phone,email,aadhar_no,acc_type,balance,status) values ( "' + name +'","'+ addr+'","'+phone+'","'+email+'","'+aadhar+'","'+actype+'",'+balance+',"active" );'
    print(sql)
    delete_last_line()
    delete_last_line()
    cursor.execute(sql)
    conct.close()

    crt_wrd="creating your account please wait......\n"
    for char in crt_wrd:
      sleep(0.1)
      sys.stdout.write(char)
      sys.stdout.flush()
    sleep(1)
    delete_last_line()

    crt_wrd="adding account details to bank database....\n"
    for char in crt_wrd:
      sleep(0.1)
      sys.stdout.write(char)
      sys.stdout.flush()
    sleep(1)
    delete_last_line()

    crt_wrd="creating your account space....\n"
    for char in crt_wrd:
      sleep(0.1)
      sys.stdout.write(char)
      sys.stdout.flush()
    sleep(1)
    delete_last_line()
    print("5 seconds left")
    sleep(4)
    delete_last_line()

    def Mbox(title, text, style):
      return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    Mbox('Account Created', 'Your account has been sucessfully created\nThank you for working with us', 0)
    print('\n\nNew customer added successfully')
    print("Account Holder's Name : ", name,"\nAddress\t\t      : ", addr,"\nEmail Address\t      : ",email,"\nContact Number \t      : ",phone,"\nAadhar Number\t      : ",aadhar,"\n")
    wait= input('\n Press any key to continue....')


def modify_account():
    conct = mysql.connector.connect(
        host='localhost', database='bank_management_system', user='root', password='1234')
    cursor = conct.cursor()
    clear()
    acno = input('Enter customer Account No :')
    print('Modify screen ')
    print('\n 1.  Customer Name')
    print('\n 2.  Customer Address')
    print('\n 3.  Customer Phone No')
    print('\n 4.  Customer Email ID')
    choice = int(input('What do you want to change ? '))
    new_data  = input('Enter New value :')
    field_name=''
    if choice == 1:
       field_name ='name'
    if choice == 2:
       field_name = 'address'
    if choice == 3:
       field_name = 'phone'
    if choice == 4:
       field_name = 'email'
    sql ='update customer set ' + field_name + '="'+ new_data +'" where acno='+acno+';' 
    print(sql)
    cursor.execute(sql)
    print('\nCustomer Information modified..')
    wait = input('\n Press any key to continue....')

def close_account():
    conct = mysql.connector.connect(
        host='localhost', database='bank_management_system', user='root', password='1234')
    cursor = conct.cursor()
    clear()
    acno = input('Enter customer Account No :')
    sql ='update customer set status="close" where acno ='+acno+';'
    cursor.execute(sql)
    print('\nAccount closed')
    wait = input('\n Press any key to continue....')


def activate_account():
    conct = mysql.connector.connect(
        host='localhost', database='bank_management_system', user='root', password='1234')
    cursor = conct.cursor()
    clear()
    acno = input('Enter customer Account No :')
    sql = 'update customer set status="active" where acno ='+acno+';'
    cursor.execute(sql)
    print('\nAccount Activated')
    wait = input('\n Press any key to continue....')

def main_menu():
    while True:
      clear()
      print(' \n \nMain Menu')
      print("\n1.  Add Account")
      print('\n2.  Modify Account')
      print('\n3.  Close Account')
      print('\n4.  Activate Account')
      print('\n5.  Transaction Menu')
      print('\n6.  Search Menu')
      print('\n7.  Report Menu')
      print('\n8.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        add_account()
      if choice == 2:
        modify_account()
      if choice == 3:
        close_account()

      if choice == 4:
        activate_account()

      if choice ==5 :
        transaction_menu()
      if choice ==6 :
        search_menu()
      if choice == 7:
        report_menu()
      if choice ==8:
        break

if __name__ == "__main__":
    main_menu()