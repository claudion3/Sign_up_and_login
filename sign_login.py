
username1=input("Create your usernamer:")
password1=input("Create your password:")
password2=input("Repete your password:")
if password1 != password2:
    print("your password is not match please try agian")
    password1=input("Create your password:")
    password2=input("Repete your password:")
else:
    print("Thank you for sign up")

print("Press y for login n for exit:")
massage="y"
massage=input("")
if massage=='y':
    username=input("Enter your usernamer:")
    password=input("Enter your password:")
    if username !=username1:
        print("Please Create account")

    while password1 != password:
         password=input("Please try again your password:")
    print("Thank you")
else:
    print("Thank you")
 

   

 

