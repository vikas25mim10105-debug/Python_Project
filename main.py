import login as l
import modify_Book as add
import issue_return as issue
import view

def login(book):
    for i in range(4,0,-1):
        login1={}
        a=int(input("\t\t\tenter your id: "))
        b=input("\t\t\tenter your pass: ")
        login1[a]=b
        w=l.administrative_login(login1)
        if i==1 or w==1:
            break
        elif i>1:
            print("Worng Password or User ID")
            print(f"you have {i-1} chance left ")
            print("__"*40)
            continue
        else:
            print("try another time ")
    if w==1:
        while True:
            ch=input("\t\t\tif you want to add new book enter add \n \t\t\tif you want to search a book enter search \n \t\t\tif you want to view the books enter view \n\t\t\tif you want to end the the take enter end: ")
            if ch=='add':
                global x
                x=add.add_book(book)
                print('books got added')
                print("__"*40)
            elif ch=='search':
                add.search_book(book)
                print("__"*40)
            elif ch=='view': 
                view.view(book)
                print("__"*40)
            elif ch=='end':
                print("Thank you")
                print("__"*40)
                break
            else:
                print("Wrong option chosen | Try other option ")
                print("__"*40)
        
def login_user():
    for i in range(4,0,-1):
        w=l.user_login()
        if i==1 or w==1:
            break
        elif i>1:
            print(f"you have {i-1}chance left ")
            print("__"*40)
            continue
        else:
            print("try another time ")
            print("__"*40)
    if w==1:
        while True:
            ch=input("\t\t\tif you want to issue book type issue \n \t\t\tif you want to return type return \n \t\t\tif you want end type end: ")
            if ch=='issue':
                issue.issue_book(book)
                print("__"*40)
            elif ch=='return':
                issue.return_book()
                print("__"*40)
            elif ch=='end':
                print("Thakyou")
                print("__"*40)
                break
            else:
                print("Wrong option chosen | Try other option ")
                print("__"*40)


book={123: ['Cosmos', 'Carl Sagan', 3,500,7], 234:['A Brief History of Time', 'Stephen Hawking',4,300,8], 345:['A Brief History of Humankind','Yuval Noah Harari',7,450,5] }
while True:
    ch=input("\t\t\tif you want Administrative Login type adm and \n\t\t\tif you want user login as user type user \n\t\t\tif you want to exd the program enter end: ")
    if ch=='adm':   
        login(book)
        print("__"*40)
    elif ch=='user':
        login_user()
    elif ch=="end":
        print("Thankyou for Using ")
        print("__"*40)
        break
    else:
        print("Wrong option chosen | Try Other option")
        print("__"*40)