import pyglet as pg

win = pg.window.Window(width=800,height=600)
win.set_caption("PyGlet Ex1-2")
bFullScreen = False

@win.event
def on_draw():
    win.clear()

@win.event
def on_key_press( symbol, modifiers ):
    global bFullScreen
    if (symbol == ord('f')):
        if (bFullScreen):
            bFullScreen = False
        else:
            bFullScreen = True
        win.set_fullscreen( bFullScreen )

if __name__=='__main__':
    pg.app.run()
