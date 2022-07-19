import turtle



t = turtle.Turtle()

colors = "yellow, gold, orange, red, maroon, violet, magenta, purple, navy, blue, skyblue, cyan, turquoise, lightgreen, green, darkgreen, chocolate, brown, black, gray, white".split(
    ", "
)

for i in range(2500):
    t.speed(i*2)
    t.pensize(1 / 10 + 1)
    t.pencolor(colors[i % len(colors)])
    t.forward(i)
    t.left(59)

turtle.exitonclick()