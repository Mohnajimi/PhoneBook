from sqlite3 import *
class Database():
    def __init__(self,db):
        self.con = connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('''
                         CREATE TABLE  IF NOT EXISTS contacts (id integer primary key, name text,
                         fname test,address text,  phone text)
                         ''')
        self.con.commit()
    
    def Insert (self , name , fname , address , phone):
        self.cur.execute('INSERT INTO contacts VALUES (null, ?, ?, ?, ?)', (name, fname, address, phone))
        self.con.commit()
        print(self.cur.rowcount , "Record Inserted!")
        print('Last ID is :' , self.cur.lastrowid)
        
    def Fetch(self):
        self.cur.execute('select * from contacts')
        rows = self.cur.fetchall()
        return rows
    
    def Remove(self,id):
        self.cur.execute('DELETE FROM contacts WHERE id = ?', [id])
        self.con.commit()
        print("Record delete!!")
    
    def Update(self , id , name , fname , address , phone):
        self.cur.execute('''
                         UPDATE contacts set name = ? , fname = ? , address = ? , phone = ?
                         WHERE id = ? ''' , (name , fname , address , phone , id))
        self.con.commit()
        
    def Search(self , id):
        self.cur.execute('SELECT * FROM contacts WHERE id = ? ' , (id,))
        row = self.cur.fetchone()
        return row
        
# d1 = Database('d:/table.db')
# for i in range (3):
#     name= input('Enter a name :')
#     fname = input('Enter a family:')
#     address = input('Enter the address:')
#     phone = input('Enter the phone:')
#     d1.Insert(name, fname, address, phone)

# records = d1.Fetch()
# print(records)