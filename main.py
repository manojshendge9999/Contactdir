'''
Main File
=========
'''
def searchname():
        print("Search Contact by Name")
        ns=input("Enter Name: ")
        fp=open('data.txt','r')
        data=fp.readlines()
        #print(data)
        for x in data:
             flag=0
        for x in data:
            #print(x)
            l=x.split(":")
            #print(l)
            #print(l[0])
            if ns.upper()==(l[0]).upper():
                print(x)
                flag=1
        if flag==0:
            print("Contact Not Found")
            

        else:
            print("Not Found")
                
            
        fp.close()

def searchmob(n):
        fp=open('data.txt','r')
        data=fp.readlines()
        for x in data:
            l=x.split(":")
            if int(n)==int(l[1]):
                #print("Contact Found:")
                #print(x)

                return x,1
        else:
                return '',0



def display():
    fp= open ("data.txt","r")
    d=fp.read()
    print("Contact Directory")
    print(d)
    print()
    fp.close()
    

def create_contact():
    fp = open("data.txt","a")
    n=input("Enter Name:")
    mn=input("Enter The Mobile Number:")
    res=validate_mob(mn)
    if res==1:
        a,b=searchmob(mn)
        if b==1:
            print("Number Already Exist")
        else:
            d=n+":"+mn+"\n"
            fp.write(d)
            fp.close()
            print("Contact Created sucessfully")
            
    else:
        print("Enter The Valid Mobile Number")


def validate_mob(x):
    if x.isdigit() and len(x)==10:
        return 1
    else:
        return 0
    
    

print("Welcome to Contact Directory Console Application")
print()
while True:
    print("1.Create Contact")
    print("2.View Contact")
    print("3.Search Contact by Name")
    print("4.Search Contact by Mobile Number")
    print("5.Exit")
    ch=int(input("Enter Your Choice:"))

    if ch==1:
        create_contact()
    elif ch==2:
        display()
    elif ch==3:
        searchname()
        pass
    elif ch==4:
        ms=input("Enter Mobile Number to be Search:")
        a,b=searchmob(ms)
        print(a)
        print(b)
        if b==1:
            print("Contact Found:")
            print(a)
        else:
            print("NOT FOUND")
        pass
    elif ch==5:
        break
    else:
        print("Please Enter Valid Option!!!")
print("Thank You For Using Application")
