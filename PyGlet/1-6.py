import pyglet as pg

win = pg.window.Window(width=640,height=480)
win.set_caption("Pyglet Ex1-6")


xCenter = win.width//2
yCenter = win.height//2
text="<font face='Tahoma' size=12pt color=#FFFF00><b><i>Hello, World</i></b></font>"
txtHello = pg.text.HTMLLabel(text, x=xCenter, y=yCenter, anchor_x='center', anchor_y='center')

@win.event
def on_draw():
    win.clear()
    txtHello.draw()

if __name__=='__main__':
    pg.app.run()
