from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mydb2 import *
#===================GUI=====================
win = Tk()
win.geometry('800x470')
win.resizable(0,0)
win.title('Contact List')
win.config(bg = '#6C45BB')

d1 = Database('C:/Phonebook/Contacts2.db')

#====================Functions=========================
def Insert_To_ListBox():
    listbox.delete(0,END)
    for row in d1.Fetch():
        listbox.insert(END,row)

def Add():
    if ent_name.get() == '' or ent_fname.get() == '' or ent_address.get() == '' or ent_phone.get() == '':
        messagebox.showinfo('Caution' ,'Enter the all field!!!!')
        return
    d1.Insert( ent_name.get() , ent_fname.get( ) , ent_address.get() , ent_phone.get())
    Clear()
    Insert_To_ListBox()
    
    
def Delete():
    Show_List()
    x = messagebox.askquestion('Warning' ,'Are you sure?')
    if x == 'yes':
        d1.delete(lst[0])
        
def Clear():
    ent_name.delete(0,END)
    ent_fname.delete(0,END)
    ent_address.delete(0,END)
    ent_phone.delete(0,END)
    
def Show_List():
    x = listbox.curselection()
    lst = (listbox.get(x))
    Clear()
    ent_name.insert(0, lst[1])
    ent_fname.insert(0, lst[2])
    ent_address.insert(0, lst[3])
    ent_phone.insert(0, lst[4])
    
def select_item1(event):
    try:
        global select_item
        index = listbox.curselection()
        print(index)
        select_item = listbox.get(index)
        print(select_item)
        ent_name.delete(0,END)
        ent_name.insert(END , select_item[1])
        ent_fname.delete(0,END)
        ent_fname.insert(END , select_item[2])
        ent_address.delete(0,END)
        ent_address.insert(END , select_item[3])
        ent_phone.delete(0,END)
        ent_phone.insert(END , select_item[4])
    except IndexError:
        pass
    
def update():
    global select_item
    d1.Update(select_item[0] , ent_name.get() , ent_fname.get() , ent_address.get() , ent_phone.get())
    Insert_To_ListBox()
    
def Search():
    Clear()
    row = d1.Search(int(ent_search.get()))
    ent_name.insert(END , row[1])
    ent_fname.insert(END , row[2])
    ent_address.insert(END , row[3])
    ent_phone.insert(END , row[4])
    
    
    




#====================Widget==============================
#Name: 
lbl_name = Label(win , text='نام :' , bg = '#6C45BB' , font= 'arial 16')
lbl_name.place(x=50 , y=50)
ent_name = Entry(win , width= 24)
ent_name.place(x=160 , y =54)

#Family
lbl_fname = Label(win , text='نام خانوادگی :' , bg = '#6C45BB' , font= 'arial 16')
lbl_fname.place(x=400 , y=50)
ent_fname = Entry(win , width= 24)
ent_fname.place(x=600 , y =54)

#Address
lbl_address = Label(win , text='آدرس :' , bg = '#6C45BB' , font= 'arial 16')
lbl_address.place(x=50 , y=100)
ent_address = Entry(win , width= 24)
ent_address.place(x=160 , y =104)

#Telephone
lbl_phone = Label(win , text='تلفن :' , bg = '#6C45BB' , font= 'arial 16')
lbl_phone.place(x=400 , y=100)
ent_phone = Entry(win , width= 24)
ent_phone.place(x=600 , y =100)


#Search
ent_search = Entry(win , width= 35)
ent_search.place(x=430 , y =251)

#Button
btn_add = ttk.Button(win , text= 'اضافه کردن' , width= 18 , command= Add)
btn_add.place(x=50 , y = 200)
btn_delete = ttk.Button(win , text= 'حذف کردن' , width= 18 , command= Delete)
btn_delete.place(x=240 , y = 200)
btn_update = ttk.Button(win , text= 'بروزرسانی' , width= 18 , command = update)
btn_update.place(x=430 , y = 200)
btn_clear = ttk.Button(win , text= 'پاک کردن ورودی ها' , width= 18 )
btn_clear.place(x=620 , y = 200)
btn_show = ttk.Button(win , text= 'نمایش لیست' , width= 18 , command = Insert_To_ListBox)
btn_show.place(x=50 , y = 250)
btn_search = ttk.Button(win , text= 'جستجو' , width= 18 , command= Search)
btn_search.place(x=240 , y = 250)

#Listbox
listbox = Listbox(win , width= 130)
listbox.place(x=10 , y=290)

#Binding list: 
listbox.bind('<<ListboxSelect>>' , select_item1)


win.mainloop()


















