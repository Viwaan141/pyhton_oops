class Library:
    def __init__(self):
        self.bookList = ["maths", "science" , "english" ,"physics"]
    def books(self):
        print("available books",self.bookList)
    def borrow(self,bookname):
        for i in self.bookList:
            if i == bookname:
                print("You borrow",i)
                self.booklist.remove(i)
                print("remaining book",self.booklist)
                break
        else:
            print(bookname,"is not availabe please select from",self.bookList)

library = Library()
library.books()
book=input("enter book name you want to borrow  " )
library.borrow(book)
