from flet import *
import sqlite3
import datetime

def omsetview(page:Page,params=None):
    tim =Text("")
    
    db = sqlite3.connect("teadb.db")
    cur= db.cursor()    
    sql = "select * from omset"
    cur.execute(sql)
    result= cur.fetchall()

    data=0
    for j in result:       
            
        data= (j[1])+data
        hasiljual =Text(f'Total Omset = Rp {data}',size=16,weight=FontWeight.BOLD)   
    db.commit()
    db.close() 
    
    def tot():
        db = sqlite3.connect("teadb.db")
        cur= db.cursor()    
        sql = "select * from omset"
        cur.execute(sql)
        result= cur.fetchall()
        coltot = Column()
        for x in result:
                coltot.controls.append(
                 Container(
                      content= Row([
                          Container(
                          border=border.all(width=2,color="blue"),
                          padding=padding.only(left=10,right=10),
                          content=Row([
                                 Text(str(f'Hari Ke {x[0]}'),size=20,weight=FontWeight.BOLD),
                                 Text(str(f'Total = Rp. {x[1]}'),size=20,weight=FontWeight.BOLD),
                        ]
                     )
                     )
                         ],MainAxisAlignment.END)
                 )
               
             )
                
        
                
        db.commit()
        db.close
        return coltot
       
        

    


    tim.value= datetime.datetime.now().strftime("%d-%m-%Y")
    db = sqlite3.connect("teadb.db")
    cur= db.cursor()    
    sql = "select * from stok"    
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
                         content= Text(f'Rp. {str(int(i[2])*int(i[3]))}',size=14,weight=FontWeight.BOLD)
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
                        tot(),
                    
        #=========fungsi==================== #
                
    #======BOTOOM APPBAR=================
              BottomAppBar(
                            bgcolor="#ff91e0f4",height=60,                                         
                            padding=0,

                            content= Container(
                                padding=padding.symmetric(-20),
                                content=Stack(
                                   [
                              ])))

            ],bgcolor="white",padding=0,spacing=0,scroll="always",adaptive=True
            
    
    )
    
