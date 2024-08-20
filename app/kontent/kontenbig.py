from flet import *

def datakontbig(page:Page):
    kontentbig = Row(scroll="always")
    img= ["Coklat","cola","Red Velvet","Taro","Mangga","Teh"]           
    for i in range (0,6):
        kontentbig.controls.append(
             Card(
                         color="white",elevation=10,
                          content=Column(
                            controls= [
                                Container(
                                border=border.all(width=2,color="blue"),border_radius=10,
                                 padding=5,ink=True,on_click=lambda _:print("kontbig"),
                                 content=Column(
                                 controls=[
                                 
                                 Image(src=f'{img[i]}.jpg',fit=ImageFit.FIT_WIDTH,height=100,width=150,border_radius=border_radius.all(10)),                               
                                 Text(f'Rasa {img[i]}',style=TextStyle(size=20,font_family="Comicsans",)),
                                 Card(color="blue",
                                     content=Container(padding=5,
                                        content= Text("IDR 10,000",color="white")
                                     )
                                     
                                     
                                 )
                                 ]),
                                    )
                             ]
                         )
                     )

        )


    return kontentbig
      
    
      