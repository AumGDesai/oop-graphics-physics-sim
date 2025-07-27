import graphicsPlus as gr
import physics_objects as pho

win = gr.GraphWin( "Ball test", 500, 500)

rect = pho.Block(win,1,1)
#rect = gr.Rectangle(gr.Point(245.0, 245.0), gr.Point(255.0, 255.0))
rect.setPosition(25, 25)

rect.draw()

win.getMouse()
win.close()
