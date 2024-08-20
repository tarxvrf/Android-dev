from flet import *
import sqlite3
import datetime

def omsetview(page:Page,params=None):
    tim =Text("")
    datatot=Text("")
    
    hasiljual =Text(f'Total Omset = Rp 0',size=16,weight=FontWeight.BOLD) 
    
    
    def tot():
        db = sqlite3.connect("teadb.db")
        cur= db.cursor()    
        sql = "select * from penjualan"
        cur.execute(sql)
        result= cur.fetchall()        
        datap=0

        for x in result:
            datap=datap+int(x[3])
            
        datatot.value= str(datap)
        hasiljual.value= f'Rp. {datatot.value}'
        
        print(datatot.value,type(datatot.value))   
        db.commit()
        db.close
        return datatot
    
    def simpandong(e):
         db= sqlite3.connect("teadb.db")
         cur = db.cursor()
         sql = "insert into omset(total) values(2)"
         #val= (datatot.value)
         cur.execute(sql)
         db.commit()
         db.close()
         page.update()
         print("tersimpan")

    


    tim.value= datetime.datetime.now().strftime("%d-%m-%Y")
    db = sqlite3.connect("teadb.db")
    cur= db.cursor()    
    sql = "select * from penjualan"    
    cur.execute(sql)
    result= cur.fetchall()
    
    db.commit()
    db.close
    
    def coled():
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
                              Container( padding=padding.only(left=20),
                              content=Text(f'{i[1]} x {i[2]}'))
                            ]
                        )
                        
                      ),
                     Container(
                         padding=padding.only(left=10,bottom=10),width=120,margin=margin.only(top=7,bottom=0),
                         height=30,border_radius=20,border=border.all(width=2,color="blue"), 
                         content= Text(f'Rp. {i[3]}',size=14,weight=FontWeight.BOLD)
                      ),
                      ]
                      )
              ),
            )
        
        return cold

    page.update()
#=============================================================================================================
    return View(

            "/store/:id",
            controls=[
                #colom1 ==========================                      
                     #colom1 ========================== APPBAR =================================
        AppBar(bgcolor="#ff91e0f4",toolbar_height=100
                           ,shape=RoundedRectangleBorder(radius=border_radius.only(bottom_left=20,bottom_right=20)),
                           title=
                           Column([
                                Row(
                               controls= [
                                   Container(
                                    padding=padding.only(left=5),
                                    content=Text("OMSET PENJUALAN",color="white")
                                      
                               ), Icon(name=icons.STORE,color="white"),tim
                             ],alignment=MainAxisAlignment.CENTER
                           ),
                           Row(
                               [
                                   Container(
                                       margin=margin.only(right=10),border=border.all(width=2,color="yellow"),
                                       padding=5,bgcolor="white",
                                       content=hasiljual
                                   )
                                   
                               ],MainAxisAlignment.CENTER
                           )
                            

                           ])
                                              
                                                      
                           ),
    
      #=========fungsi====================== #
                        coled(),
                       Container(
                            margin=margin.only(bottom=10),
                            content=tot()
                       ) 
                    ,
        #=========fungsi==================== #
                FloatingActionButton(icon=icons.SAVE,on_click=simpandong),
    #======BOTOOM APPBAR=================
              BottomAppBar(
                            bgcolor="#ff91e0f4",height=60,                                         
                            padding=0,

                            content= Container(
                                
                                content=Stack(
                                   [
                              ])))

            ],bgcolor="white",padding=0,spacing=0,scroll="always",adaptive=True
            
    
    )
    
