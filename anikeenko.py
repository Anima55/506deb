import turtle

window = turtle.Screen()
window.bgcolor("white")

star = turtle.Turtle()
star.color("black")
star.speed(2)

def draw_star(size):
    for _ in range(5):
        star.forward(size)
        star.right(144)

draw_star(100)

turtle.done()
