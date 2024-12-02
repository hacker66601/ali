import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("""
                         CREATE TABLE IF NOT EXISTS Contacts (
                         name text, family text, address text, phone text)
                         """)
        self.con.commit()
    

    def fetch(self):
        self.cur.execute("SELECT * FROM Contacts")
        rows = self.cur.fetchall()
        return rows
    
    def insert(self, name, family, address, phone):
        self.cur.execute("""
                         INSERT INTO Contacts VALUES(?,?,?,?)
                         """, (name, family, address, phone))
        self.con.commit()
    
    def remove(self, id):
        self.cur.execute("DELETE FROM Contacts WHERE id = ?")
        self.con.commit()
        
    def update(self, name, family, address, phone):
       self.cur.execute("""
                     UPDATE Contacts SET name = ?, family = ?, address = ?, phone = ?
                     """, (name, family, address, phone))  # ID در اینجا آخرین پارامتر است
       self.con.commit()

    def search(self,input_):
        self.cur.execute("""SELECT * FROM Contacts WHERE name = ? or family = ?
                          or address = ? or phone = ?
                          """, (input_, input_, input_, input_))
        return self.cur.fetchall()

db1 = Database('D:/test1/mydata7.db')