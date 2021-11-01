#Book Managment System using HashMap

class Book:
    def __init__(self):
        self.SIZE=10
        self.arr=[[] for i in range(self.SIZE)]

    def getHash(self,key):
        val=0
        for i in key:
            val+=ord(i)
        return val%self.SIZE    

    def addBook(self,bname):
        hash=self.getHash(bname)
        self.arr[hash].append(bname)    
        print("Book added successfully...!\n")

    def getBook(self,bname):
        hash=self.getHash(bname)
        if len(self.arr[hash]) is 0:
            print("Book is not available.")
        else:
            for i in self.arr[hash]:
                if i == bname:
                    print(bname,' Book is available.')
                    break
                else:
                    print(bname," Book is not available")

    def delBook(self,bname):
        hash=self.getHash(bname)
        if len(self.arr[hash]) is 0:
            print("Book is not available.")
        else:
            for i in self.arr[hash]:
                if i == bname:
                    print(bname,' Book is Deleted.')  
                    self.arr[hash].remove(bname)
                    break
            else:
                print("Book is not Available")        

    def displayBook(self):
        print("Books Available: ")
        for i in self.arr:
            if len(i)>0:
                print(*i,end=" ")
        print()
if __name__=='__main__':
    hashTable=Book()
    while True:
        print("\t\tBook Management System")
        print("1.Add \t 2.Search \t 3.Delete \t 4.Display \t 5.Exit ")
        ch=int(input("\nEnter Your Choice:  "))
        if ch == 1:
            bookName=input("Enter the Book Name to Add: ")
            hashTable.addBook(bookName)
        if ch == 2:
            bookName=input("Enter the Book Name to Search: ")
            hashTable.getBook(bookName)
        if ch == 3:
            bookName=input("Enter the Book Name to Delete: ")
            hashTable.delBook(bookName)
        if ch == 4:
            hashTable.displayBook()
        if ch == 5:
            print("Thankyou!")
            exit(0)
