from flet import *
import sqlite3

def stokiew(page:Page,params=None):
    
    inp2 =TextField(hint_text="msukan jumlah",keyboard_type="NUMBER",border="None",text_size=12,text_align=TextAlign.CENTER,
                        )
    t = Text("")  
    #mod= AlertDialog(modal=True,title=Text("input penjualan") )
    def lihat(e):
        tk= e.control.data[0]           
        t.value= str(tk)
        print(t.value)
        page.update()

    def inputan(e):
        db = sqlite3.connect("teadb.db")
        cur= db.cursor()    
        sql = "insert into stok(nama,jumlah,harga) values('taro',1,8000)"
        #val=(inp2.value)
        cur.execute(sql)
        db.commit()
        db.close
        page.update()
        
        

    def updatedata(e):      
        db = sqlite3.connect("teadb.db")
        cur= db.cursor()    
        sql = f'update stok set jumlah={inp2.value} where id={t.value}'
        #val=(inp2.value)
        cur.execute(sql)
        db.commit()
        db.close
        page.update()

    
    def coled():
        db = sqlite3.connect("teadb.db")
        cur= db.cursor()    
        sql = "select * from stok "
        cur.execute(sql)
        result= cur.fetchall()
        cold= Column()       
        
        for i in result:
            
            cold.controls.append(
                  Container(
                  padding=10,height=120,
                  content=Row([
                      
                      Container(
                          padding=padding.only(left=10,bottom=10),width=150,margin=margin.only(top=7,bottom=0),
                          height=100,border_radius=20,border=border.all(width=2,color="blue"), 
                          content=Column(
                            [
                              Image(src=f'{i[1]}.jpg',fit=ImageFit.CONTAIN,width=100,height=60),
                              Container( padding=padding.only(left=35),
                              content=Text(i[1]))
                            ]
                        )
                        
                      ),
                     Container(
                        
                         padding=padding.only(left=10,bottom=10),width=110,margin=margin.only(top=7,bottom=0),
                         height=40,border_radius=20,border=border.all(width=2,color="blue"), 
                         content= inp2
    
                      ),
                      ElevatedButton("update",on_click=lihat,data=i)
                      ]
                      )
              ),
            )
        db.commit()
        db.close()
        
        return cold 
     
    page.update()
   
   # def inputan(e):
      #page.open(mod)
                       
                       
                       
                      
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
                                                                                                                         
                                                 content=Text("STOK BARANG",color="white")
                                      
                               ), Icon(name=icons.STORE,color="white")
                             ],alignment=MainAxisAlignment.CENTER
                           )                      
                                                      
                           ),

          coled(),

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
                                    CircleAvatar(IconButton(icon=icons.SAVE,on_click=inputan),radius=30)],MainAxisAlignment.CENTER
                                  )
                                 
                              )
                              
                                   ]
                               )
                           )
                          
                              
                              
                                )

            ],bgcolor="white",padding=0,spacing=0,scroll="always",adaptive=True
            
    
    )
    
