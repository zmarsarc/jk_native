import tkinter
import tkinter.simpledialog
import tkinter.messagebox
import sqlite3

SIZE_XS = 30
SIZE_S = 31
SIZE_M = 32
SIZE_L = 33
SIZE_XL = 34

conn = sqlite3.connect('storage.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS jk(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, size SMALLINT NOT NULL, length INT NOT NULL DEFAULT(0), count INT NOT NULL DEFAULT(0));')
conn.commit()

def add_new():
    name = tkinter.simpledialog.askstring('add new jk', 'jk name:')
    size = tkinter.simpledialog.askstring('add new jk', 'jk size:')
    size_code = 0
    if size.upper() == 'XS':
        size_code = SIZE_XS
    elif size.upper() == 'S':
        size_code = SIZE_S
    elif size.upper() == 'M':
        size_code = SIZE_M
    elif size.upper() == 'L':
        size_code = SIZE_L
    elif size.upper() == 'XL':
        size_code = SIZE_XL
    else:
        tkinter.messagebox.showwarning('not allow size: ' + size)
        return
    length = tkinter.simpledialog.askinteger('add new jk', 'jk length:')
    count = tkinter.simpledialog.askinteger('add new jk', 'jk count:')

    conn.execute('INSERT INTO jk(name, size, length, count) VALUES(?,?,?,?);',(name, size_code, length,count))
    conn.commit()


top = tkinter.Tk()

row_index = 0
for row in c.execute('SELECT name, size, length, count FROM jk'):
    tkinter.Label(top, text=row[0]).grid(row=row_index, column=0)
    tkinter.Label(top, text=row[1]).grid(row=row_index, column=1)
    tkinter.Label(top, text=row[2]).grid(row=row_index, column=2)
    tkinter.Label(top, text=row[3]).grid(row=row_index, column=3)
    row_index += 1

tkinter.Button(top, text='add', command=add_new).grid(row=row_index, column=3)

top.mainloop()
conn.close()