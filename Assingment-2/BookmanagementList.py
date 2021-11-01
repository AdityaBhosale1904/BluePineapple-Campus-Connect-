#Book Management System Menu Driven Program(Linked List)

class Book:
    # constructor to add book in list
    def __init__(self,name):
        self.bname=name
        self.next=None

    # add book in list
    def insertBook(self,name):
        curr=self
        new=Book(name)
        while curr.next != None:
            curr=curr.next
        curr.next=new

    # display all the books
    def displayList(self):
        curr=self   
        print("Books Available: ")
        while curr:
            print(curr.bname,end=" ")
            curr=curr.next

    # search any book
    def searchBook(self,name):
        curr=self

        while curr:
            if curr.bname == name:
                return True
            curr=curr.next 
        return False       

    # remove any book from list
    def delBook(self,name):
        flag=False
        if self.searchBook(name) is False:
            flag=False

        elif self.bname == name:
            new=self
            self=self.next
            del new
            flag=True
        else:
            
            curr,back=self,self 

            while curr:
                if curr.bname == name:
                    back.next=curr.next
                    flag=True
                back=curr
                curr=curr.next    
        if flag:
            print(name," Book Is Available")
        else:
            print(name," Book Is Not Available")  
        return self                       

# Main function
if __name__=='__main__':
    head=None
    
    while True:
        print("\n\tBook Management System")
        print("1.Insert  2.Search  3.Delete  4.Display  5.Exit  ")
        ch=int(input("\nEnter your choice:"))

        # accept book 
        if ch == 1:
            name=input("Enter the Book Name: ")
            if head == None:
                head = Book(name)
            else:        
                head.insertBook(name)
            continue
        
        # accept book name and search
        if ch == 2:
            if head == None:
                print("Book List is Empty")
                continue
            
            name=input("Enter the Book Name to Search: ")
            if head.searchBook(name):
                print(name," Book Is Available")
            else:
                print(name," Book Is Not Available")     
            continue
        
        # accept book name which u want to delete
        if ch == 3:
            if head == None:
                print("Book List is Empty")
                continue

            name=input("Enter the Book Name to delete: ")

            head= head.delBook(name)
            continue       
        # display books available
        if ch == 4:
            if head == None:
                print("Book List is Empty")
                continue
            head.displayList()
            continue    
        # exit 
        if ch == 5:
            print("Thanks for visiting...!")
            exit(0)