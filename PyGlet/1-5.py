import pyglet as pg

win = pg.window.Window(width=640,height=480)
win.set_caption("Pyglet Ex1-5")
xCenter = win.width//2
yCenter = win.height//2
text="Hello, World"
txtHello = pg.text.Label(text, font_name="Tahoma", bold=True, italic=True, font_size=12, x=xCenter, y=yCenter, anchor_x='center', anchor_y='center', color=(255,255,0,255))

@win.event
def on_draw():
    win.clear()
    txtHello.draw()

if __name__=='__main__':
    pg.app.run()
