import pyglet as pg
win = pg.window.Window(width=320,height=240, 
        caption='Pyglet Ex1-1', 
        style=pg.window.Window.WINDOW_STYLE_TOOL)

@win.event
def on_draw():
    win.clear()
if __name__=='__main__':
    pg.app.run()
