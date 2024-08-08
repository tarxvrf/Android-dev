from flet import *

def datakontmint(page:Page):
    img= ["coklat","cola","merah","taro"]  
    kontentmin= Row(scroll="Always")
    star= Row()
    ic= Icon(name=icons.STAR,color="yellow",size=15)
    for x in range(0,5):
        star.controls.append(
            ic
        )
    for i in range(0,4):
        kontentmin.controls.append(
            Container(                 
                  margin =margin.only(left=10,top=10,bottom=10),
                  content=Card(
                  color="white",elevation=30,
                  content=Container(
                      width=300,padding=10,border_radius=10,
                      content=Column(
                          [
                          ListTile(
                              leading=Image(src=f'{img[i]}.jpg',fit=ImageFit.FIT_HEIGHT),
                              title=Text("Wiwit",size=20,weight=FontWeight.BOLD),
                              subtitle=Text("Wah Rasanya enak banget gak bakalan nyesesl beli ini"),
                            
                          ),Row(
                              controls=[
                                  ElevatedButton("lihat",on_click=lambda _:print("kontmint"),bgcolor="#C62828",color="white"),
                                  star
                              ],alignment=MainAxisAlignment.CENTER
                          )
                          ]
                      )

                  )

                )
                )
        )
        



    
               
    return kontentmin

          