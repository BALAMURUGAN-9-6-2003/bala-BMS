import pyttsx3 as pyt
import speech_recognition as sr
from database import Database
import datetime as dt
def tell(Input):
    ind=pyt.init()
    ind.say(Input)
    ind.runAndWait()
def inputvoice():
    recg=sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening You : ",end=" ")
        recg.energy_threshold=1000
        recg.adjust_for_ambient_noise(mic,1)
        audio=recg.listen(mic)
        text=recg.recognize_google(audio)
        print(text)
        text=str(text).lower()
    return text

tell(f"This is an Bank management voice assicent used to communicate information using voice")
tell("if you want to continue tell yes or no to exit")
ans=inputvoice()
if "yes" in ans.split():  
    tell("please tell your name")
    name=inputvoice()
    tell(f'welcome {name} ')
    tell('select any one option to continue the process like')
    tell("create account or existing account")
    userinput=inputvoice().split()

    if  "create" in userinput:
        tell("Please Enter your Full name sir.")
        name=input("Please Enter Your Full Name sir : ").strip()
        tell("Please enter your initial deposit sir.")
        amount=int(input("Please Enter Your Initial Deposit Sir : "))
        tell("Please enter your date of birth sir. example was given their down")
        print("Eg:12/2/22")
        dateofbirth=list(input("Please Enter Your Date Of Birth Sir : " ).strip().split("/"))
        tell("Please enter your mobile number sir")            
        phno=int(input("Please enter your mobile number sir : "))
        tell("Thank you for giving all the details sir and your accountnumber was generated")
        account=name[:3]+str(dateofbirth[0])+str(dateofbirth[1])+str(phno)
        print(f"your account number sir {account}")          
        # want Connection with database for creating account name
        data=Database(account+".db")
        data.deposit(dt.datetime.today,amount,amount)
        print("Thank you for choose our bank sir")           
        print("If you want to continue please start again")            

    elif  "existing" in userinput :
        tell("Please enter you account number sir")
        accountno=input("Please enter you account number sir : ")
         # want Connection with database weather the account in our database
        tell("What type of procee you want to do like deposit or withdraw or close your account or bank statement")
        need=inputvoice().split()
        
        if "deposit" in need:
            tell("Please enter your amount to deposit greater than 0")
            amount=int(input("Please enter the amount to deposit greater than 0 : "))
            # want Connection with database to deposit the amount
            data=Database(accountno+".db")
            l=data.last()
            data.deposit(dt.datetime.today,amount,str(int(l[-1][-1])+amount))
            tell("Your current balance is : ")
            print("Your current balance is : ")
            
        elif "withdraw" in need:
            tell("Please enter your amount to withdraw greater than 0")
            amount=int(input("Please enter the amount to withdraw greater than 0 : "))
            # want Connection with database to withdraw the amount
            data=Database(accountno+".db")
            l=data.last()
            data.withdraw(dt.datetime.today,amount,str(int(l[-1][-1])-amount))
            tell("Your current balance is : ")
            print("Your current balance is : ")
            
        elif "close your account" in need:
            tell("Are you intrested to close your account")
            print("Are you intrested to close your account")
            ans=inputvoice()
            if "yes" in ans:
                tell("Your approvel was accepted")
                print("Your Approvel Was Accepted")
                # want Connection with database to drop the database

            else:
                tell("Your approvel was rejected")
                print("Your approvel was rejected")
                
        elif "bank statement" in ans:
            # want Connection with database to display bank statement
            data=Database(accountno+".db")
            data.fetch()
            

        else:
            tell("Sorry I can't reach you please start again")
    else:
        print("program break")


else:
    if "no" in ans:
        tell("thank you for visiting our bank please visit again ")
    else:
        tell("Sorry I can't reach you please start again")
    