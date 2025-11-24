def view(book):
    print("__"*40)
    while True:
        ch=input("\t\t\tif you want to view books on self enetr self  \n\t\t\tif you want to view books whose price is between the given ranage type price \n\t\t\tif you want to end enetr end: ")
        if ch=='self':
            self_no=int(input("enetr self number"))
            for i in book:
                if book[i][4]==self_no:
                    print(book[i])
            print("__"*40)
        elif ch=='price':
            up_l=int(input("enetr upper limit"))
            l_l=int(input("enetr lower limit"))
            for i in book:
                if book[i][3]>=l_l and book[i][3]<=up_l:
                    print(book[i])
            print("__"*40)
        elif ch=='end':
            print("thankyou for using")
            print("__"*40)
            break
        else:
            print("Wrong option chosen | Try other option ")
            print("__"*40)