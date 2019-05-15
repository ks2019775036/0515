import turtle as t

def draw_pos(x,y):
    t.clear()
    t.setpos(x,y)
    t.stamp()

    hl=-(t.window_height()/2)

    tm=0
    while True:
        d=(9.8*tm**2)/2
        ny=y-int(d)
        if ny>hl:
            t.goto(x,ny)
            t.stamp()
            tm+=0.3
        else:
            break

t.setup(500,600)
t.shape("circle")
t.shapesize(0.3,0.3,0)
t.penup()
s=t.Screen()
s.onscreenclick(draw_pos)
s.listen()
