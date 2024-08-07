from flet import *

def datakontbig(page:Page):
    kontentbig = Row(scroll="always")
               
    for i in range (0,10):
        kontentbig.controls.append(
             Card(
                         color="white",
                          content=Column(
                            controls= [
                                Container(
                                 padding=5,ink=True,on_click=lambda _:print("kontbig"),
                                 content=Column(
                                 controls=[
                                 Image(src="pemandagan.jpg",fit=ImageFit.FIT_WIDTH,height=100,width=200,border_radius=border_radius.all(10)),                               
                                 Text("Makannan1",text_align=TextAlign.CENTER)])  )
                             ]
                         )
                     )

        )


    return kontentbig
      
    
      