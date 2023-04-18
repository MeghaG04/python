a = input("Enter the username ")
credentials = {"Alice" : "alice123","Bob" : "bob123"}
if a in credentials:
        b = input("enter your password")
        if b == credentials[a]:
            print("login success")
        else:
            print("invalid credentials ")
        
else:
    print("user not found")
