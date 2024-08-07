from flet import *



def storeview(page:Page,params=""):
    t= Text("")
    dd= Dropdown(width=100)
    t.value = params
    

    page.update()

    return View(

            "/store/:id",
            controls=[
                #colom1 ==========================                      
                     #colom1 ========================== APPBAR =================================
                    AppBar(bgcolor="#ff91e0f4",toolbar_height=80
                           ,shape=RoundedRectangleBorder(radius=border_radius.only(bottom_left=20,bottom_right=20)),
                           title=Row(
                               controls= [
                                   Container(
                                                width=220,height=40,
                                                margin=margin.only(left=0),
                                                 bgcolor="white",
                                                 border_radius=20,                                                                                              
                                                 content=TextField(prefix_icon=icons.SEARCH,border="None",label="Cari")
                                      
                               ), Icon(name=icons.STORE,color="white")
                             ],alignment=MainAxisAlignment.SPACE_BETWEEN
                           )                      
                                                      
                           ),FloatingActionButton(icon=icons.ADD),

          Column([
              Container(
                  content=Row([
                     Dropdown(
                         width=100,options=[
                             dropdown.Option("OREO"),
                             dropdown.Option("matcha"),
                             
                         ]
                     )
               ])
              ),
              ElevatedButton("klik",on_click=lambda _:page.go("/store/1")),
             
              t.value

            ])
                             

            ],spacing=0,padding=0
    
    )
    
