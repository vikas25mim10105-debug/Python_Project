#login Module
def administrative_login(login1):
    login={2345:"pass@pass"}
    if login1 == login:
        print("Administrative login successful")
        print("__"*40)
        w=1
        return w  
    


def user_login():
    print("__"*40)
    ch=input("\t\t\tif you want to login enter login \n\t\t\tif you want to regester enter register: ")
    login={2343:"shayam"}
    if ch=='login':
        login1={}
        a=int(input("\t\t\tenetr your id: "))
        b=input("\t\t\tenter your pass: ")
        login1={a:b}
        
        if login1==login:
            print("user login successful")
            print("__"*40)
            w=1
            return w  
    elif ch=='register':
        us_name=int(input("\t\t\tenter user name (it will be in numbers only): "))
        u_pass=input("\t\t\tenter password: ")
        login[us_name]=u_pass
        print("User Register")
        print("__"*40)
        w=1
        return w


