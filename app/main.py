import flet 
from flet import *


from views.home import homeview
from views.store import storeview

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
        if page.route =="/store":          
        
            page.views.append(
                storeview(page=page)
            )
        elif troute.match("/store/:id"):
            page.views.append(
                storeview(page=page,params=troute.id)
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

