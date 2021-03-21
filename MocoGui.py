#This imports the library tkinter what is used to make the GUI
import tkinter
#This creates the main window
ResourceMachine=tkinter.Tk()
#This is the name for the windows
ResourceMachine.title("VideoSearch Academy")
#This is what determines the window size
ResourceMachine.geometry("1000x600")
tkinter.Grid.rowconfigure(ResourceMachine, 0, weight=0)
tkinter.Grid.columnconfigure(ResourceMachine, 1, weight=4)

sRequest=tkinter.StringVar()

bPhoto1=tkinter.PhotoImage(file="customButton1.png")
bPhoto2=tkinter.PhotoImage(file="customButton2.png")
bPhoto3=tkinter.PhotoImage(file="customButton3.png")
bPhoto4=tkinter.PhotoImage(file="customButton4.png")
#This is the search bar
searchBar2 = tkinter.Entry(ResourceMachine,textvariable=sRequest, font=('calibre',10,'normal'))
searchBar2.grid(row=1, column=1, sticky="nsew")


#This is what prints what the user searched
def sQuery():

   sRequest = searchBar2.get()
   print("You Searched:",sRequest)
#This is the name for the search bar
searchBar1 = tkinter.Label(ResourceMachine, text="What Is Your Topic",font=("montserrat",17,"bold")).grid(row=0, column=1, sticky="nsew")
#searchBar1.pack()
#.grid(row=0, column=1)
#searchBar2 = tkinter.Entry(ResourceMachine,textvariable=sRequest, font=('calibre',10,'normal')).grid(row=0, column=1)
nRequest=tkinter.IntVar()

#searchButtom1 = tkinter.Button (ResourceMachine, text="Search",command=lambda:[sQuery(), nQuery()]).grid(column=1,row=2)
#This is the selector for number of results per page
searchNumberName=tkinter.Label(ResourceMachine,text="Results Per Page",font=("montserrat"))
searchNumber=tkinter.Spinbox( ResourceMachine, from_=5, to=20,textvariable=nRequest,width=2,font=("montserrat"))
searchNumber.grid(row=10,column=1, sticky="ns")
searchNumberName.grid(row=9,column=1, sticky="nsew")
#this is how many search results will be on the page at a time
def nQuery():

   nRequest = searchNumber.get()
   print(nRequest,"results")
#this shows what option of video length is picked
def lChoice():
   lenChoice= "U Picked " + str(choice1.get())
   #tkinter.Label(ResourceMachine, text=choice1)
   print(lenChoice)
choice1 = tkinter.StringVar()

# C1= tkinter.Radiobutton(ResourceMachine,text="Shorter Than 4 Minutes", variable=choice1, value="short",command=lChoice)
# C2= tkinter.Radiobutton(ResourceMachine,text="Between 4 and 20 Minutes", variable=choice1, value="medium",command=lChoice)
# C3= tkinter.Radiobutton(ResourceMachine,text="Longer Than 20 Minutes", variable=choice1, value="long",command=lChoice)
# C4= tkinter.Radiobutton(ResourceMachine,text="Any Length", variable=choice1, value="any",command=lChoice)
C1= tkinter.Radiobutton(ResourceMachine,text="Shorter Than 4 Minutes", variable=choice1, value="short",font=("montserrat"))
C2= tkinter.Radiobutton(ResourceMachine,text="Between 4 and 20 Minutes", variable=choice1, value="medium",font=("montserrat"))
C3= tkinter.Radiobutton(ResourceMachine,text="Longer Than 20 Minutes", variable=choice1, value="long",font=("montserrat"))
C4= tkinter.Radiobutton(ResourceMachine,text="Any Length", variable=choice1, value="any",font=("montserrat"))
C1.grid(row=5,column=1)
C2.grid(row=6,column=1)
C3.grid(row=7,column=1)
C4.grid(row=8,column=1)
#select does not simulate a click invoke does
C4.select()
#C4.invoke()
label = tkinter.Label(ResourceMachine)
#label=Label(ResourceMachine)
#add page numbers and pages

sSpace=tkinter.Label ( ResourceMachine, text="----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
sSpace.grid(row=14,column=1)
#this is the search button
def on_enter(e):
   bSwitcher2()


def on_leave(e):
   bSwitcher1()




def bSwitcher1():
   searchButton1.config(image=bPhoto1)
def bSwitcher2():
   searchButton1.config(image=bPhoto2)

searchButton1 = tkinter.Button (ResourceMachine,text="Search",image=bPhoto1,borderwidth=0,command=lambda:[sQuery(), nQuery(),lChoice()])
searchButton1.grid(column=1,row=2, sticky="ns")
searchButton1.bind("<Enter>",on_enter)
searchButton1.bind("<Leave>",on_leave)

#this checks if the selected page is a valid number
def pageMaker():
   pNumber = pNumMaker.get()

   #pNumber2= int(pNumber)
   if pNumber.isdigit()==True:

      print(pNumber)

   else:
      pass
#this is the name for the page selector
pNumName=tkinter.Label(ResourceMachine,text="Page #:",anchor="center",font=("montserrat"))
pNumName.grid(row=11,column=1, sticky="nsew")
pNumber=tkinter.IntVar()
#this is the text box for the page selector
pNumMaker = tkinter.Entry(ResourceMachine,textvariable=pNumber,font=("montserrat"))
pNumMaker.grid(row=12, column=1, sticky="ns")

#this is what checks for if the cursor is hovering over the button
def on_enter(e):
   bSwitcher4()


def on_leave(e):
   bSwitcher3()


#thios is the go to the selected page button

def bSwitcher3():
   pageButton1.config(image=bPhoto3)
def bSwitcher4():
   pageButton1.config(image=bPhoto4)
pageButton1 = tkinter.Button (ResourceMachine,text="Go",borderwidth=0,image=bPhoto3,command=pageMaker)
pageButton1.grid(column=1,row=13, sticky="ns")
pageButton1.bind("<Enter>",on_enter)
pageButton1.bind("<Leave>",on_leave)
#this is a function that gets the page number selected and prints it

def pNVal():

   sRequest = searchBar2.get()
   print(sRequest)
#This is what keeps the program constantly checking for new changes
print(pageButton1)
ResourceMachine.mainloop()
