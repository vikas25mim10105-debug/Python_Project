def add_book(book):
    print("__"*40)
    # book={23: ['abc', 'def', 3, 245,7]}
    n=int(input("\t\t\tenter how many books you want to add: "))
    for i in range(n):
        # l=[]
        s_no=int(input("\t\t\tenter serial number "))
        b_name=input("\t\t\tenetr Name of book")
        b_au=input("\t\t\tenter the author of book")
        b_number=int(input("\t\t\tenetr no of copies "))
        b_price=int(input("\t\t\tenetr the price of book"))
        b_self=int(input("\t\t\tenetr the self no.. "))
        l=[b_name,b_au,b_number,b_price,b_self]
        book[s_no]=l
    return book
def search_book(x):
    print("__"*40)
    while True:
        ch=input("\t\t\tenetr by which want to search \n \t\t\tif you want to search by serial number enter ser \n \t\t\tif you want to search by book name enter name \n \t\t\tif you want to search by author name enetr author \n \t\t\tif you want to seach from self number enter self \n \t\t\tif you want to seach by price enetr price \n \t\t\tenetr end to end: ")
        if ch=='ser':
            serial=int(input("\t\t\tenetr the serial no you want to seach:"))
            for i in x:
                if i==serial:
                    print(x[i])
                    print("__"*40)
        elif ch=='name':
            name1=input("\t\t\tenter the name you want to search: ")
            for i in x:
                if x[i][0]==name1:
                    print(x[i])
                    print("__"*40)
                
        elif ch=="author":
            author1=input("\t\t\tenter the name of author: ")
            for i in x:
                if x[i][1]==author1:
                    print(x[i])
                    print("__"*40)
        elif ch=='price':
            price1=int(input("\t\t\tenter price you want to seach: "))
            for i in x:
                if x[i][3]==price1:
                    print(x[i])
                    print("__"*40)
        elif ch=='self':
            self1=int(input("\t\t\tenetr the self number: "))
            for i in x:
                if x[i][4]==self1:
                    print(x[i])
                    print("__"*40)
        elif ch=="end":
            print("Thnak you")
            print("__"*40)
            break
        else:
            print("Wrong option chosen | Try other option ")
            print("__"*40)