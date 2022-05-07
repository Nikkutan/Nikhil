import re

def register():
    db=open('registration.txt','r')
    pattern='^[a-z 0-9]+[\.]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
    Username= input("enter the Emnail_ID:")
    if re.search(pattern, Username):
        print("username valid")
    else:
        print("Invalid username")
        register()
    Password= input("create password:")
    d= []
    f= []
    for i in db:
        a,b= i.split(",")
        b= b.strip()
        d.append(a)
        f.append(b)
        data = dict(zip(d, f))
    if len(Password)<6:
        print("password is too short")
        register()
    elif re.search(r'[A-Z]',Password) is None:
        print("password doesn't contain an uppercase letter")
        register()
    elif re.search(r'[a-z]',Password) is None:
        print("password doesn't contain an lowercase letter")
        register()
    elif re.search(r'\d',Password) is None:
        print("password doesn't contain an digit")
        register()
    elif re.search(r'[!@#$%^&*]', Password) is None:
        print("password doesn't contain special character")
        register()
    elif Username in d:
        print("username exists")
        register()
    else:
        db= open("registration.txt","a")
        db.write(Username+","+Password+"\n")
        print("success")
def access():
    db = open('registration.txt', 'r')
    Username= input("enter the Emnail_ID:")
    Password = input("Enter password:")
    if not len(Username or Password)<1:
        d= []
        f= []
        for i in db:
            a,b=i.split(",")
            b=b.strip()
            d.append(a)
            f.append(b)
        data= dict(zip(d,f))
        try:
            if data[Username]:
                try:
                    if Password==data[Username]:
                        print("login success")
                        print("Hi,",Username)
                    else:
                        print("password or username wrong")
                except:
                    print("password and username doen't match")
            else:
                print("username doesn't exist")
        except:
            print("Login Error")
def home(option=None):
    option=input("Login:| Register:")
    if option=="Register":
        register()
    elif option=="Login":
        access()
    else:
        print("Enter an option")
home()



