from flet import *
import sqlite3
import datetime

def stokiew(page:Page,params=None): 
    coled=Column()
    tjfield= TextField("")
    thasilubah=Text("")       
    tn= Text("") 
    txttgl= Text("")
    txtalert= Text("")
    id= Text("")
    thrg=Text("")
    thasil=Text("")
    idubah=Text("")
    tanggal= datetime.datetime.now()
    tglini= tanggal.strftime("%d-%m-%Y")
    txttgl.value=str(tglini)

    #def dialogsimpan(e):
        #thasilubah.value= str(int(tjfield.value)*int(thrg.value)) 
        #db = sqlite3.connect("teadb.db")
        #cur= db.cursor()    
        #sql = f'update penjualan set jumlah={tjfield.value},hasil={thasilubah.value} where id ={idubah.value}'
        #cur.execute(sql)              
        #db.commit()
        #db.close    
        #coled.controls.clear()
        #lihat()         
        #page.close(botomshet)
        #page.update()

    
    #botomshet= Banner( content=Column(
                                     #[txtalert,tjfield ])                         
                                      #,actions=[ElevatedButton("simpan",on_click=dialogsimpan),ElevatedButton("batal",on_click=lambda _:page.close(botomshet))]
                                      #)
    
    

    def infohapus():
        snack_bar=SnackBar(content=Text("berhasil dihapus"),duration=500,bgcolor="red",open=True)
        page.overlay.append(snack_bar)
        
    def hapus(e):
        id.value= e.control.data[0]        
        db = sqlite3.connect("teadb.db")
        cur= db.cursor()    
        sql = f'delete from penjualan where id ={id.value}'
        cur.execute(sql)              
        db.commit()
        db.close
        coled.controls.clear()
        infohapus()
        lihat()
        page.update()
                 
    def bukadialog(e):
        id.value= e.control.data[0]
        idubah.value=id.value
        txtalert.value= e.control.data[1]
        tjfield.value=e.control.data[2]
        page.go(f'/edit/{idubah.value}')
        page.update()


    db = sqlite3.connect("teadb.db")
    cur= db.cursor()    
    sql = f'select * from penjualan where tanggal="{tglini}"'
    cur.execute(sql)
    res= cur.fetchall()        
    for x in res:                       
        coled.controls.append(
                Row(
                    [
                        Container(
                           margin=margin.only(top=10,left=10,right=10),border_radius=10, 
                           content= Image(f'{x[1]}.jpg',fit=ImageFit.CONTAIN,width=100,height=100)
                        ),Text(f'x{x[2]}',size=15,weight=FontWeight.BOLD),Text(f'Rp{x[4]}'),IconButton(icon=icons.DELETE,on_click=hapus,data=x),
                        IconButton(icon=icons.EDIT,on_click=bukadialog,data=x)

                    ]
                )

            )
       
    def lihat():        
        db = sqlite3.connect("teadb.db")
        cur= db.cursor()    
        sql = "select * from penjualan"
        cur.execute(sql)
        res= cur.fetchall()        
        for x in res:                       
            coled.controls.append(
                Row(
                    [
                        Container(
                           margin=margin.only(top=10,left=10,right=10),border_radius=10, 
                           content= Image(f'{x[1]}.jpg',fit=ImageFit.CONTAIN,width=100,height=100)
                        ),Text(f'x{x[2]}',size=15,weight=FontWeight.BOLD),Text(f'Rp{x[4]}'),IconButton(icon=icons.DELETE,on_click=hapus,data=x),
                        IconButton(icon=icons.EDIT,on_click=bukadialog,data=x)

                    ]
                )

            )
       
    #dialog= AlertDialog(modal=True,title=Text("update data"),
                        #content=Column(
                           # [
                           #     txtalert,tjfield
                           # ]
                        #),
                        #actions=[TextButton("simpan",on_click=dialogsimpan),TextButton("batal",on_click=lambda e:page.close(dialog))],actions_alignment=MainAxisAlignment.END)

   
    listminuman= Dropdown(width=100,hint_text="Pilih",border="None",fill_color="white")
    def dadrop(e):
        tn.value= e.control.data[1]
        thrg.value=e.control.data[3]              
        print(tn.value,thrg.value,type(thrg.value))
        page.update()

    def minuman():
        db = sqlite3.connect("teadb.db")
        cur= db.cursor()    
        sql = "select * from stok "
        cur.execute(sql)
        result= cur.fetchall()        
        for i in result:
            listminuman.options.append(
                dropdown.Option(i[1],on_click=dadrop,data=i)
            )
        return listminuman

    def simpandata(e):        
        thasil.value= int(inp2.value) * thrg.value       
        db = sqlite3.connect("teadb.db")
        cur= db.cursor()    
        sql = "insert into penjualan(nama,jumlah,harga,hasil,tanggal) values(?,?,?,?,?)"
        val=(tn.value,inp2.value,thrg.value,thasil.value,txttgl.value)
        cur.execute(sql,val)        
        db.commit()
        db.close() 
        coled.controls.clear()
        lihat()      
        page.update()

    def lihatdata(e):
        db = sqlite3.connect("teadb.db")
        db.commit()
        db.close()         
        lihat()
        print("lihat")
        page.update
       
    elv=ElevatedButton("Simpan",on_click=simpandata,bgcolor="blue",color="white")   
    inp2 = TextField(hint_text="jumlah",keyboard_type="NUMBER",border="None",text_size=12,text_align=TextAlign.CENTER)
                    
    return View(
            
            "/store/:id",
            controls=[
                #colom1 ==========================                      
                     #colom1 ========================== APPBAR =================================
                    AppBar(bgcolor="#D50000",toolbar_height=80
                           ,shape=RoundedRectangleBorder(radius=border_radius.only(bottom_left=20,bottom_right=20)),
                           title=Row(
                               controls= [
                                   Container(
                                                                                                                         
                                                 content=Text("PENJUALAN",color="white")
                                      
                               ), Icon(name=icons.STORE,color="white")
                             ],alignment=MainAxisAlignment.CENTER
                           )                      
                                                      
                           ),
                Column(
                    [
                        Row(
                            [
                            Container(
                            margin=margin.only(left=10),
                            content=Row(
                            [
                            Container(
                            margin=margin.only(top=10,left=10,right=0),height=50,
                            padding=padding.only(left=5,bottom=5,right=10),border=border.all(width=2,color="blue"),border_radius=10,
                            content=minuman()
                            ),
                           Container(padding=padding.only(left=5,bottom=10),width=80,margin=margin.only(top=7,bottom=0,right=10,left=2),
                            height=40,border_radius=20,border=border.all(width=2,color="blue"), 
                            content=inp2
                             ),                         
                               
                            ]
                        )
                        ),
                         Container( 
                             margin=margin.only(left=-15),
                             content=elv
                         )],MainAxisAlignment.CENTER
                        ),                     
                    ]
                )
                ,coled,#dialog,


#================ BOTTOM BAR ========================================================                             

           #  mod,
                        BottomAppBar(
                            bgcolor="#D50000",height=60,
                                         
                            padding=0,

                           content= Container(
                                padding=padding.symmetric(-20),
                                content=Stack(
                                   [
                                Container( 
                                    
                                    height=60,
                                    margin=0,    
                                   content=Row(
                                        controls=[                                        
                                        IconButton(icon=icons.MENU, icon_color=colors.WHITE),                                        
                                        IconButton(icon=icons.FAVORITE, selected_icon_color="red",selected=False,
                                                   style=ButtonStyle(color={"selected":colors.RED,"":colors.WHITE}),
                                                   ),
                                            ],alignment=MainAxisAlignment.SPACE_BETWEEN
                                )
                                ),
                               Container(
                                
                                 content= Row(
                                     [
                                    CircleAvatar(IconButton(icon=icons.SAVE),radius=30)],MainAxisAlignment.CENTER
                                  )  )
                              
                                   ]
                               )
                           )
                          
                                )

            ],bgcolor="white",padding=0,spacing=0,scroll="always",adaptive=True
            
    
    )
  
    
