class book:
    def __init__(self, title, genre: list[str], author):
        self.title = title
        self.genre = genre
        self.author = author

class library:
    def __init__(self, name: str, address: str, books: list[book]):
        self.name = name
        self.address = address
        self.books = books
      

class person:
    def init(self, name, SSN: int, phone: int, email: str):
        self.name = name
        self.SSN = SSN
        self.phone = phone
        self.email = email

class patron(person):
    def __init__(self, name, SSN, phone, email):
        super().__init__()
        self.libnum = 69420
        self.books: list[book] = []

class librarian(person):
    def __init__(self, name, SSN, phone, email):
        super().__init__()
        self.password = "bigchungus"
        self.work: list[library] = [library("the book sniffer", "N Gay st. Auburn, AL 36830", [
                book("The Adventures of Smelvin", ["action", "adventure"], "Sir Fodulus Gregory Snooble III"),
                book("Digulus Gary's erudite observations", ["Non-Fiction", "Academic"], "Dr. Dingulus Gary P.H.D.")
        ])]
    
    def Checkout(self, pat: patron, bname):
        self.pname = pat
        if len(self.work[0].books) < 2:
                self.shorthand[bname] = self.work[0].books[0].title
                exist = True
        else:
            self.shorthand = {
                "smelvin": self.work[0].books[0].title,
                "Dingulus": self.work[0].books[1].title
                            }
            exist = False
            for key in self.shorthand:
                if key == bname:
                    exist = True
        if exist == True:
            exist2 = False
            bname = self.shorthand[bname]
            for item in self.work[0].books:
                if item.title == bname:
                    exist2 = True

                if exist2 == True:
                    self.pname.books.append(item)
                    self.work[0].books.remove(item)
                    print("BOOK HAS BEEN CHECKED OUT")
                    print("checked out books:")
                    for item in self.pname.books:
                        print(item.title)
                    print(f"remaining books in {self.work[0].name}:")
                    for item in self.work[0].books:
                        print(item.title)
                else:
                    print("BOOK IS NOT IN THE LIBRARY")

    def bookreturn(self, pat: patron, bname):
        self.pname = pat
        exist = False
        for key in self.shorthand:
            if key == bname:
                exist = True
        if exist == True:
            exist2 = False
            bname = self.shorthand[bname]
            for item in self.pname.books:
                if item.title == bname:
                    exist2 = True
                
                if exist2 == True:
                    self.work[0].books.append(item)
                    self.pname.books.remove(item)
                    print("BOOK RETURNED")
                    print(f"remaining books in {self.work[0].name}:")
                    for item in self.work[0].books:
                        print(item.title)
                else: 
                    print("PATRON DOES NOT HAVE BOOK")
    
    def addnewbook(self, bname):
       self.booklist = [
           book("dickballs amogus: the book", ["comedy"], "john funnyman"),
           book("epic memes to show your friends", ["comedy"], "candice ligma")
       ]
       if len(self.booklist) < 2:
           self.shorthand2[bname] = self.booklist[0].title
           exist = True
       else:
            self.shorthand2 = {
                "amogus": self.booklist[0].title,
                "memes": self.booklist[1].title
            }
            exist = False
            for key in self.shorthand2:
                if key == bname:
                    exist = True
       if exist == True:
           exist2 = False
           bname = self.shorthand2[bname]
           for item in self.booklist:
               if item.title == bname:
                   exist2 = True

               if exist2 == True:
                   self.work[0].books.append(item)
                   self.booklist.remove(item)
                   print(f"book added!: {item.title}")
                   
           

librobj = librarian("betha woodward", 666-99-4200, 666-999-4200, "Booksniffersanonymous@gaymail.com")
patobj = patron("Dick Dastardly", 999-66-2400, 999-666-2400, "bookman69@homomail.org")

while True:
    com = input()
    fcom = com.split(" ")
    if fcom[0] == "checkout":
        librobj.Checkout(patobj, fcom[1])
    if fcom[0] == "return":
        librobj.bookreturn(patobj, fcom[1])
    if fcom[0] == "add":
        librobj.addnewbook(fcom[1])






                    




