from flet import *


def datafloat(page:Page):
    menufloat =  Container(
                                  
                margin=10,
                 content = Card(
                 color="white",
                 elevation=15,                                  
                 content=Container(
                 height=70,
                 content=Row(
                             [

                                                   
                                                               
                               Column(
                                    controls=[
                                    CircleAvatar(IconButton(icon=icons.MOTORCYCLE,on_click=lambda _:page.go("/store/:id")),bgcolor="#D50000",color="white"),
                                                 Text("Ojek")]
                                                            ), 
                                                                                                           
                                  Column(
                                  controls=[
                                   CircleAvatar(IconButton(icon=icons.SHOPPING_BASKET),bgcolor="#D50000",color="white"),
                                                Text("Belanja")]
                                                            ),
                                 Column(
                                     controls=[
                                         CircleAvatar(IconButton(icon=icons.HOTEL),bgcolor="#D50000",color="white"),
                                                Text("Hotel")    ]
                                                            ),
                                                                            
                                    Column(
                                       controls=[
                                        CircleAvatar(IconButton(icon=icons.COMMUTE),bgcolor="#D50000",color="white"),
                                                Text("Bus Suttle")  ]
                                                            )
                                              ],alignment=MainAxisAlignment.SPACE_EVENLY

                                   ),margin=margin.only(top=20,bottom=10) 
                                     )
                                  )                             
                              )
    return menufloat  
                            
