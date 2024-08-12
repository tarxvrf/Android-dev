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
                                    CircleAvatar(IconButton(icon=icons.MONETIZATION_ON,on_click=lambda _:page.go("/omset/:id")),bgcolor="#D50000",color="white"),
                                                 Text("OMSET")]
                                                            ), 
                                                                                                           
                                  Column(
                                  controls=[
                                   CircleAvatar(IconButton(icon=icons.CALCULATE,on_click=lambda _:page.go("/stok/:id")),bgcolor="#D50000",color="white"),
                                                Text("STOK")]
                                                            ),
                                 Column(
                                     controls=[
                                         CircleAvatar(IconButton(icon=icons.HOTEL),bgcolor="#D50000",color="white"),
                                                Text("")    ]
                                                            ),
                                                                            
                                    Column(
                                       controls=[
                                        CircleAvatar(IconButton(icon=icons.COMMUTE),bgcolor="#D50000",color="white"),
                                                Text("")  ]
                                                            )
                                              ],alignment=MainAxisAlignment.SPACE_EVENLY

                                   ),margin=margin.only(top=20,bottom=10) 
                                     )
                                  )                             
                              )
    return menufloat  
                            
