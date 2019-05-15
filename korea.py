import turtle as t

def draw_pos(x,y):
    t.hideturtle
    t.clear()
    t.setpos(x,y)
    t.stamp()
    t.write("y:%5d"%y)

    hl=-(t.window_height()/2)

    tm=0
    while True:
        d=(9.8*tm**2)/2
        ny=y-int(d)
        if ny > hl:
            t.goto(x,ny)
            t.stamp()
            t.write("y:%5d, d:%5d"%(ny,d))
            tm+=0.3
        else:
            break
t.setup(500,600)
t.shape("circle")
t.shapesize(0.3,0.3,0)
t.penup()
t.ht
s=t.Screen()
s.onscreenclick(draw_pos)
s.listen()
