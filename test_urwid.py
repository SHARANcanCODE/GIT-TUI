import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

txt = urwid.Text("Hello World! Press 'q' to quit.", align='center')
fill = urwid.Filler(txt, valign='middle')

loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()
