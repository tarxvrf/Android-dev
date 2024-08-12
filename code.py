 def coled():
        cold= Column()
        nama=["cola","coklat","buahnaga","taro","merah","merah"]
        
        for i in range(0,6):
            cold.controls.append(
                  Container(
                  padding=10,height=120,
                  content=Row([
                      
                      Container(
                          padding=padding.only(left=10,bottom=10),width=150,margin=margin.only(top=7,bottom=0),
                          height=100,border_radius=20,border=border.all(width=2,color="blue"), 
                          content=Column(
                            [
                              Image(src=f'{nama[i]}.jpg',fit=ImageFit.CONTAIN,width=100,height=60),
                              Container( padding=padding.only(left=35),
                              content=Text(nama[i]))
                            ]
                        )
                        
                      ),
                     Container(
                         padding=padding.only(left=10,bottom=10),width=110,margin=margin.only(top=7,bottom=0),
                         height=40,border_radius=20,border=border.all(width=2,color="blue"), 
                         content= TextField(hint_text="msukan jumlah",keyboard_type="NUMBER",border="None",text_size=12,text_align=TextAlign.CENTER,
                                           on_focus=lambda e:lihat(nama[i]))
    
                      ),
                      ]
                      )
              ),
            )
        return cold