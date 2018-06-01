import sqlite3 as sq

def connect():
    con = sq.connect('jobs.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS job(id INTEGER PRIMARY KEY,jobtitle text,company text,date integer,through text,salary integer,status text)")
    con.commit()
    con.close()

def insert(jobtitle,company,date,through,salary,status):
    con = sq.connect('jobs.db')
    cur = con.cursor()
    cur.execute("INSERT INTO job VALUES(NULL,?,?,?,?,?,?)",(jobtitle,company,date,through,salary,status))
    con.commit()
    con.close()

def view():
    con = sq.connect('jobs.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM job")
    rows = cur.fetchall()
    con.close()
    return rows

def search(jobtitle="",company="",date="",through="",salary="",status=""):
    con = sq.connect('jobs.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM job WHERE jobtitle=? OR company=? OR date=? OR through=? OR salary=? OR status=?",(jobtitle,company,date,through,salary,status))
    rows = cur.fetchall()
    con.close()
    return rows

def delete(id):
    con = sq.connect('jobs.db')
    cur = con.cursor()
    cur.execute("DELETE FROM job WHERE id=?", (id,))
    con.commit()
    con.close()

def update(jobtitle,company,date,through,salary,status):
    con = sq.connect('jobs.db')
    cur = con.cursor()
    cur.execute("UPDATE job SET jobtitle=? OR company=? OR date=? OR through=? OR salary=? OR status=? WHERE id=?",(jobtitle,company,date,through,salary,status))
    con.commit()
    con.close()


connect()
