import pyglet as pg
from pyglet import gl

class MyWindow(pg.window.Window):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.set_size(640,480)
        self.set_caption("Pyglet Ex1-4")
        self.set_exclusive_mouse(True)
        self.set_exclusive_keyboard(True)

    def on_draw(self):
        self.clear()
    
    def on_key_press( self, symbol, modifers ):
        if symbol == pg.window.key.Q:
            self.close()
        elif symbol == pg.window.key.R:
            gl.glClearColor(1.0,0.0,0.0,1.0)
        elif symbol == pg.window.key.G:
            gl.glClearColor(0.0,1.0,0.0,1.0)
        elif symbol == pg.window.key.B:
            gl.glClearColor(0.0,0.0,1.0,1.0)

if __name__=='__main__':
    win = MyWindow()
    pg.app.run()
