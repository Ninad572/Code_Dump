class library:
    books=[]
    lended=[]
    n=int(input("Enter Number Of Books-"))
    for i in range(n):
        a=str(input(f"Enter Name Of Book Number {i+1}-"))
        books.append(a)

    def lend(self):
        name=str(input("Please Enter Your Name-"))
        v=str(input("Please Enter The Name Of Book Which You Want Take From The Available Books-"))

        if v in self.books:
            self.books.pop(self.books.index(v))
            self.lended.append(name)
            self.lended.append(v)
        else:
            if v not in self.books and v in self.lended:
                print(f"Sorry The Book Is Already Lended To-{self.lended[self.lended.index(v)-1]}")
            else:
                print(f"Sorry The Book Is Not Available In Our Library :(")


    def addbook(self):
        n1=int(input("Enter Number Of Books You Want To Add To Library-"))
        for i in range(n1):
            r=str(input(f"Enter Name Of Book Number {i+1}-"))
            self.books.append(r)
    def returnbook(self):
        y=str(input("Enter The Name Of Book Which You Want To Return-"))
        if y not in self.books and y in self.lended:
            self.books.append(y)
        elif y in self.books:
            print("The Book Is Already Returned!")
obj=library
print("Main Menu- \n1.Lend A Book. \n2.Add A Book. \n3.Return A Book.")

while True:
    e=int(input("Enter Your Choice-"))
    if e==1:
        print(f"The Available Books In Our Library Are-{obj.books}")
        obj.lend(obj)

        y=str(input("Do You Want To Continue?(y/n)-"))
        if y=='y':
            continue
        else:
            break
    if e==2:
        print(f"The Available Books In Our Library Are-{obj.books}")
        obj.addbook(obj)


        y=str(input("Do You Want To Continue?(y/n)-"))
        if y=='y':
            continue
        else:
            break
    if e==3:
        print(f"The Available Books In Our Library Are-{obj.books}")
        obj.returnbook(obj)


        y=str(input("Do You Want To Continue?(y/n)-"))
        if y=='y':
            continue
        else:
            break