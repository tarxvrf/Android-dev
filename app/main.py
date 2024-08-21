import flet 
from flet import *

from views.edit import editview
from views.stok import stokiew
from views.home import homeview
from views.omset import omsetview

def main(page: Page):
    page.spacing=0,
    page.padding=0
    page.theme_mode="light"
    page.adaptive=True
    
    def rute(route):
        troute = TemplateRoute(page.route)
        page.views.clear()
        page.views.append(
            homeview(page=page)
        )
        
        if troute.match("/omset/:id"):
            page.views.append(
               omsetview(page=page,params=troute.id)
            )
        elif troute.match("/stok/:id"):
            page.views.append(
                stokiew(page=page,params=troute.id)
            )
        elif troute.match("/edit/:id"):
            page.views.append(
                editview(page=page,params=troute.id)
            )
        page.update()

    
    def popview(view):
        page.views.pop()
        back = page.views[-1]
        page.go(back.route)
    
    
    page.on_route_change=rute
    page.on_view_pop=popview
    

    
    page.go(page.route)


          
app(target=main,assets_dir="assets")

