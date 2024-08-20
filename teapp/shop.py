from flet import *
import sqlite3


def main(page: Page):
    

    def home(e):
        page.open()

    def shop(e):
        page.open()
    btn1= ElevatedButton("home",on_click=home)
    btn2=ElevatedButton("shop",on_click=shop)
    page.add(btn1,btn2)


app(main)
