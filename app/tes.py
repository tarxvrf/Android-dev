import sqlite3

def tabel3():   
    db = sqlite3.connect("teadb.db")
    cur= db.cursor()
    #cur.execute("DROP TABLE IF EXISTS stok")
    sql = "create table minuman(idminuman int primary key, foreign key(idminuman) references stok(id) not null,nama_minuman varchar(50),harga int) "
    cur.execute(sql)
    db.commit()
    db.close

#tabel3()

def tabel():   
    db = sqlite3.connect("teadb.db")
    cur= db.cursor()
    cur.execute("DROP TABLE IF EXISTS stok")
    sql = "create table stok(id integer primary key autoincrement,nama varchar(50),jumlah integer,harga integer) "
    cur.execute(sql)
    db.commit()
    db.close

tabel()
def tabel2():   
    db = sqlite3.connect("teadb.db")
    cur= db.cursor()
    #cur.execute("DROP TABLE IF EXISTS stok")
    sql = "alter table stok add foreign key(idminuman(id integer primary key autoincrement,nama varchar(50),jumlah integer,harga integer) "
    cur.execute(sql)
    db.commit()
    db.close

#tabel2()

     
def tambah():
    db = sqlite3.connect("teadb.db")
    cur= db.cursor()    
    sql = "insert into stok (nama,jumlah,harga) values('merah',2,2000) "
    cur.execute(sql)
    db.commit()
    db.close
#tambah()

def hasil():
    db = sqlite3.connect("teadb.db")
    cur= db.cursor()    
    sql = "select * from stok "
    cur.execute(sql)
    result= cur.fetchall()
    for x in result:
        print(x)
    db.commit()
    db.close
#hasil()

def updatedata():
    db = sqlite3.connect("teadb.db")
    cur= db.cursor()    
    sql = "update stok set jumlah=5 where id=1"
    cur.execute(sql)
    db.commit()
    db.close
    

#updatedata()

    