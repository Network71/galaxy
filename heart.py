import math as m
import random as r
import turtle as t

SCALE = 100
s = t.Screen()
s.setup(600, 700)
s.bgcolor("#050002")
s.tracer(0)

p = t.Turtle()
p.hideturtle()
p.penup()


def heart(u):
    x = 1.6 * (m.sin(u) ** 3)
    y = (
        1.3 * m.cos(u)
        - 0.5 * m.cos(2 * u)
        - 0.2 * m.cos(3 * u)
        - 0.1 * m.cos(4 * u)
    )
    return x, y


N = 450
pts = []
for _ in range(N):
    u = r.uniform(0, 2 * m.pi)
    hx, hy = heart(u)
    rad = m.sqrt(r.random())
    x, y = hx * rad, hy * rad
    z = 1.1 * (1 - rad) * r.uniform(-1, 1)
    pts.append((x, y, z))


def get_col(f):
    f = max(0.0, min(1.0, f))
    r1, g1, b1 = 70, 0, 10
    r2, g2, b2 = 255, 30, 50
    return (
        f"#{int(r1 + (r2 - r1) * f):02x}"
        f"{int(g1 + (g2 - g1) * f):02x}"
        f"{int(b1 + (b2 - b1) * f):02x}"
    )


step = 0


def loop():
    global step
    p.clear()
    t_val = 1.0 + 0.3 * m.sin(step * 0.1)

    if t_val <= 1.6:
        p.width(1)

        head = min(1.0, t_val)
        tail = max(0.0, t_val - 0.35)
        fade = max(0.0, 1.0 - (t_val - 0.7)) if t_val > 0.7 else 1.0

        red_c = max(0, min(255, int(170 * fade)))
        base_col = f"#{red_c:02x}001a"
        p.color(base_col)

        for hx, hy, _hz in pts:
            x1, y1 = hx * tail * SCALE, hy * tail * SCALE
            x2, y2 = hx * head * SCALE, hy * head * SCALE

            p.penup()
            p.goto(x1, y1)
            p.pendown()
            p.goto(x2, y2)

            if t_val < 0.9:
                p.penup()
                p.goto(x2, y2)
                p.color("#ff1a40")
                p.dot(1.8)
                p.color(base_col)

    s.update()
    step += 1
    s.ontimer(loop, 16)


loop()
t.mainloop()