from flet import *
import flet as ft

from kontent.detail import detail
from kontent.menufloat import datafloat
from kontent.kontentmin import datakontmint
from kontent.kontenbig import datakontbig
def homeview(page:Page):
    def togle(e):
        e.control.selected= not e.control.selected
        e.control.update()
        

    return View(
                     
                    "/",
                    controls=[
  #colom1 ========================== APPBAR =================================
                    AppBar(bgcolor="#D50000",toolbar_height=60
                           ,shape=RoundedRectangleBorder(radius=border_radius.only(bottom_left=10,bottom_right=10)),
                           title=Row(
                               controls= [Container(
                                       
                                            content=Row(
                                          [
                                               Container(
                                                margin=margin.only(top=10),
                                                 padding=padding.only(bottom=10),
                                                 bgcolor="white",
                                                 border_radius=20,                                           
                                                 height=30,width=200,                                                
                                                 content=TextField(prefix_icon=icons.SEARCH,border="None",hint_text="Cari",text_size=12)
                                               ),
                                               Icon(name=icons.PERSON,color="white")
                                          ]
                                     )
                               )
                             ],alignment=MainAxisAlignment.CENTER
                           )                      
                                                      
                           ),    
                                                              
 #Colom ke2================ MENU APLIKASI FLOATING=============================                       
                    Column(
                        [
                            datafloat(page=page)
                        ]
                    ),
                    
  #================================================      
    Column(
        [
        Card(
           color="#ff492811", 
           content=Container(
               margin=margin.only(left=10,top=5,bottom=5),
               content= Text("Review Pembeli ",size=12,font_family="ROBOTO",weight=FontWeight.BOLD,color="white")
           ))
        ]
    ),

    Column(
        [
            datakontmint(page=page)

        ]
    ),
        
  #====================================================
   Column(
        [
        Card(
           color="#ff492811",
           content=Container(
                margin=margin.only(left=10,top=5,bottom=5),
               content= Text("Mungkin Kalian Bisa lihat yg ini ",size=12,font_family="ROBOTO",weight=FontWeight.BOLD,color="white")
           ))
        ]
    ),

#=======================================
    Column(
        [
             Container(
                     margin =margin.only(left=10,top=10,bottom=10),                    
                     content= datakontbig(page=page)
                     )
    
           
        ]
    ),

    #=====================================================
 Column(
        [
        Card(
          color="#ff492811",
           content=Container(
               margin=margin.only(left=10,top=5,bottom=5),
               content= Text("Mungkin Kalian Bisa lihat yg ini ",size=12,font_family="ROBOTO",weight=FontWeight.BOLD,color="white")
           ))
        ]
    ),
Column(
        [
             Container(
                     
                     margin =margin.only(left=10,top=10,bottom=10),  
                     content= detail(page=page)
                     )
    
           
        ]
    ),



#================ BOTTOM BAR ========================================================                             

            
                        BottomAppBar(
                            bgcolor="#D50000",height=80,
                                         
                            padding=0,

                           content= Container(
                                padding=padding.symmetric(-10),
                                content=Stack(
                                   [
                                Container( 
                                    
                                    height=60,
                                    margin=0,    
                                
                                    
                                     
                                     content=Row(
                                        controls=[                                        
                                        IconButton(icon=icons.MENU, icon_color=colors.WHITE),                                        
                                        IconButton(icon=icons.FAVORITE, selected_icon_color="red",on_click=togle,selected=False,
                                                   style=ButtonStyle(color={"selected":colors.RED,"":colors.WHITE}),
                                                   ),
                                            ],alignment=MainAxisAlignment.SPACE_BETWEEN
                                )
                                ),
                               Container(
                                 padding=padding.symmetric(-10),
                                 content= Row(
                                     [
                                    CircleAvatar(IconButton(icon=icons.SEARCH),radius=25)],MainAxisAlignment.CENTER
                                  )
                                 
                              )
                              
                                   ]
                               )
                           )
                          ,
                              
                              
                                )
                          
                    ],bgcolor="white",padding=0,spacing=0,scroll="always",adaptive=True
                )

