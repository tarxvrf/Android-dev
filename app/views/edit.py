from flet import *
import sqlite3

def editview(page:Page,params=None):
    print(params)
    id=Text("")
    coled= Column()
    ambilx=Text("")
    thrg=Text("")
    thasil=Text("")
    def simpan(e):  
        id.value=params  
        thasil.value=str(int(tfield.value)*int(thrg.value))    
        db = sqlite3.connect("teadb.db")
        cur= db.cursor()    
        sql = f'update penjualan set jumlah={tfield.value},hasil={thasil.value} where id ={id.value}'
        cur.execute(sql)              
        db.commit()
        db.close
        infoubah() 
        page.update()
        
    def balik(e):
        page.go("/stok/:id")
        
    def ubah(e):      
        db = sqlite3.connect("teadb.db")
        cur= db.cursor()    
        sql = f'select * from penjualan where id={params}'
        cur.execute(sql)
        res= cur.fetchall()
        for y in res:                  
            datax=y[3]    
        thrg.value=datax 
        db.commit()
        db.close()  

    def infoubah():
        snackbar= SnackBar(content=Text("Data berhasil diubah"),duration=500,open=True,bgcolor="blue")
        page.overlay.append(snackbar)

    

    tfield=TextField(hint_text="0",on_focus=ubah)   

           
    db = sqlite3.connect("teadb.db")
    cur= db.cursor()    
    sql = f'select * from penjualan where id={params}'
    cur.execute(sql)
    res= cur.fetchall()        
    for x in res:                       
        coled.controls.append(
                
                 Row(
                    [
                        Container(
                           border_radius=10,margin=10,
                           content= Image(f'{x[1]}.jpg',fit=ImageFit.CONTAIN,width=100,height=100)
                        ),Container(width=50,height=40,content=tfield)
                        ,ElevatedButton("Update",on_click=simpan),
                        ElevatedButton("Kembali",on_click=balik)

                    ],MainAxisAlignment.CENTER
                )
         
            )    
    db.commit()
    db.close()
    return View(
        "/edit/:id",
        controls=[
             AppBar(bgcolor="#D50000",toolbar_height=80
                           ,shape=RoundedRectangleBorder(radius=border_radius.only(bottom_left=20,bottom_right=20)),
                           title=Row(
                               controls= [
                                   Container(                                                                          
                                     content=Text("EDIT MENU",color="white")
                                      
                               ), Icon(name=icons.STORE,color="white")
                             ],alignment=MainAxisAlignment.CENTER
                           )                      
                                                      
                           ),
            coled,
#================ BOTTOM BAR ========================================================                             

           #  mod,
                        BottomAppBar(
                            bgcolor="#D50000",height=60,                                        
                            padding=0,)       
            ],bgcolor="white",padding=0,spacing=0,scroll="always",adaptive=True
            
    
    )
  

