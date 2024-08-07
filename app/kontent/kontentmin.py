from flet import *

def datakontmint(page:Page):

    kontentmin= Row(scroll="Always")

    for i in range(0,3):
        kontentmin.controls.append(
            Container(                 
                  margin =margin.only(left=10),
                  content=Card(
                      color="white",
                  content=Container(
                      width=300,padding=10,
                      content=Column(
                          [
                          ListTile(
                              leading=Image(src="pemandagan.jpg",fit=ImageFit.CONTAIN),
                              title=Text("Pemandangan Alam"),
                              subtitle=Text("Ini bagian dari kuassa tuhan"),
                            
                          ),Row(
                              controls=[
                                  ElevatedButton("lihat",on_click=lambda _:print("kontmint"),bgcolor="#C62828",color="white")
                              ],alignment=MainAxisAlignment.CENTER
                          )
                          ]
                      )

                  )

                )
                )
        )
        



    
               
    return kontentmin

          