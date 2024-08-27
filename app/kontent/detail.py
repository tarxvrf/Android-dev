from flet import *
import sqlite3
def detail(page:Page):
    detail= Row(scroll="always")
    db = sqlite3.connect("teadb.db")
    cur= db.cursor()    
    sql = f'select * from stok'
    cur.execute(sql)
    res= cur.fetchall()     
    for i in res:
        detail.controls.append(
             Card(
                         color="white",
                          content=Column(
                            controls= [
                                Container(
                                    border=border.all(width=2,color="blue"),border_radius=10,
                                    padding=5,ink=True,on_click=lambda _:print("kontbig"),
                                   content= Row([
                                        Container(
                                            Column(
                                                [
                                                    Text(f'Rasa {i[1]}',style=TextStyle(size=20,font_family="Comicsans",)),
                                                     Card(color="blue",
                                                            content=Container(padding=5,
                                                                content= Text(f'IDR {i[3]}',color="white")
                                     )
                                     
                                     
                                 )
                                                ]
                                            )
                                        ),                                       
                                        Container(
                                             Image(src=f'{i[1]}.jpg',fit=ImageFit.FIT_WIDTH,height=100,width=150,border_radius=border_radius.all(10))
                                        )
                                       ]
                                        )
                                
                                 
                                    )
                             ]
                         )
                     )

        )


    return detail
      
    
      