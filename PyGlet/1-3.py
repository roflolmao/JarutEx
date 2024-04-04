import pyglet as pg

win = pg.window.Window(width=800,height=600)
win.set_caption("PyGlet Ex1-3")
win.set_mouse_visible(True)
cursors = [win.CURSOR_CROSSHAIR, win.CURSOR_DEFAULT, win.CURSOR_HAND, win.CURSOR_HELP, win.CURSOR_NO, win.CURSOR_SIZE, win.CURSOR_SIZE_DOWN, win.CURSOR_SIZE_DOWN_LEFT, win.CURSOR_SIZE_DOWN_RIGHT, win.CURSOR_SIZE_LEFT, win.CURSOR_SIZE_LEFT_RIGHT, win.CURSOR_SIZE_RIGHT, win.CURSOR_SIZE_UP, win.CURSOR_SIZE_UP_DOWN, win.CURSOR_SIZE_UP_LEFT, win.CURSOR_SIZE_UP_RIGHT, win.CURSOR_TEXT, win.CURSOR_WAIT, win.CURSOR_WAIT_ARROW]
current_cursor = 0
last_cursor = len(cursors)

@win.event
def on_draw():
    win.clear()

@win.event
def on_mouse_press(x,y,buttons,modifers):
    global cursors
    global current_cursor
    global last_cursor
    if (buttons == pg.window.mouse.RIGHT):
        cursor = win.get_system_mouse_cursor(cursors[current_cursor])
        win.set_mouse_cursor(cursor)
        current_cursor = current_cursor + 1
        if current_cursor>=last_cursor:
            current_cursor = 0

if __name__=='__main__':
    print(last_cursor)
    pg.app.run()
