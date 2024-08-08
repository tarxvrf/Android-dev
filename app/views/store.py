from flet import *

def storeview(page:Page,params=None):


    dd = Dropdown(
                         width=100,options=[
                             dropdown.Option("OREO"),
                             dropdown.Option("matcha"),
                             
                         ]
                     )
    t = Text("")  
    inp1=TextField(hint_text="masukan nama",border="None",text_size=12,text_align=TextAlign.CENTER)
    inp2=TextField(hint_text="msukan jumlah",border="None",text_size=12,text_align=TextAlign.CENTER)
    def coled():
        cold= Column()
        nama=["cola","starbak","lotte"]
        for i in range(0,3):
            cold.controls.append(
                  Container(
                  padding=10,height=120,
                  content=Row([
                      
                      Container(
                          padding=padding.only(left=10,bottom=10),width=150,margin=margin.only(top=7,bottom=0),
                          height=100,border_radius=20,border=border.all(width=2,color="blue"), 
                          content=Column(
                            [
                              Image(src="cola.png",fit=ImageFit.CONTAIN,width=100,height=60),
                              Container( padding=padding.only(left=35),
                              content=Text(nama[i]))
                            ]
                        )
                        
                      ),
                     Container(
                         padding=padding.only(left=10,bottom=10),width=150,margin=margin.only(top=7,bottom=0),
                         height=40,border_radius=20,border=border.all(width=2,color="blue"), 
                         content= inp2
                      ),
                      ]
                      )
              ),
            )
        return cold

    def klik(e):
        t.value=f'jumlah penjualan {dd.value}={inp2.value}'
        
        
        
        page.update()
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
                                                                                                                         
                                                 content=Text("LAPORAN PENJUALAN",color="white")
                                      
                               ), Icon(name=icons.STORE,color="white")
                             ],alignment=MainAxisAlignment.CENTER
                           )                      
                                                      
                           ),FloatingActionButton(icon=icons.ADD),

          coled()

             
              

            
                             

            ],bgcolor="white",padding=0,spacing=0,scroll="always",adaptive=True
            
    
    )
    
