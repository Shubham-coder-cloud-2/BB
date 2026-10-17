import turtle
import math
import random

# ---------------- SCREEN ----------------
screen = turtle.Screen()
screen.setup(width=1000, height=750)
screen.bgcolor("black")
screen.title("Happy Birthday Pranjal ❤️")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

# ---------------- HEART ----------------
def draw_heart():
    pen.goto(0, -155)
    pen.color("#ff1744")
    pen.pensize(4)
    pen.pendown()

    # Parametric heart curve
    for i in range(361):
        t = math.radians(i)
        x = 16 * math.sin(t) ** 3
        y = (13 * math.cos(t)
             - 5 * math.cos(2 * t)
             - 2 * math.cos(3 * t)
             - math.cos(4 * t))

        pen.goto(x * 13, y * 13 - 5)

    pen.penup()

    # Small highlight on the outline
    pen.goto(-12, 115)
    pen.dot(5, "#ff8aab")


# ---------------- BIRTHDAY TEXT ----------------
def write_birthday():
    pen.goto(0, 12)
    pen.color("#ffb6c1")
    pen.write(
        "Happy Birthday",
        align="center",
        font=("Georgia", 27, "bold")
    )

    pen.goto(0, -28)
    pen.color("#ffffff")
    pen.write(
        "PRANJAL",
        align="center",
        font=("Georgia", 32, "bold")
    )

    pen.goto(0, -65)
    pen.color("#ff4d88")
    pen.write(
        "♡  Make a wish  ♡",
        align="center",
        font=("Georgia", 15, "italic")
    )


# ---------------- FLOWERS ----------------
def draw_flower(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.color(color)

    # Five petals
    for _ in range(5):
        pen.penup()
        pen.goto(x, y)
        pen.setheading(_ * 72)
        pen.forward(size * 0.6)
        pen.pendown()
        pen.dot(size, color)

    # Flower centre
    pen.penup()
    pen.goto(x, y)
    pen.dot(size * 0.45, "#ffd166")


# ---------------- BUTTERFLIES ----------------
def draw_butterfly(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.color(color)
    pen.pensize(2)

    # Upper and lower wings
    pen.goto(x - size * 0.1, y)
    pen.dot(size * 0.18, "#ffffff")

    pen.goto(x - size * 0.12, y + size * 0.18)
    pen.dot(size * 0.55, color)

    pen.goto(x - size * 0.12, y - size * 0.18)
    pen.dot(size * 0.4, color)

    pen.goto(x + size * 0.35, y + size * 0.18)
    pen.dot(size * 0.55, color)

    pen.goto(x + size * 0.35, y - size * 0.18)
    pen.dot(size * 0.4, color)

    # Body
    pen.goto(x + size * 0.1, y - size * 0.23)
    pen.dot(size * 0.12, "#ffffff")

    # Antennae
    pen.goto(x + size * 0.1, y)
    pen.setheading(75)
    pen.pendown()
    pen.forward(size * 0.25)
    pen.penup()

    pen.goto(x + size * 0.1, y)
    pen.setheading(105)
    pen.pendown()
    pen.forward(size * 0.25)
    pen.penup()


# ---------------- SPARKLES ----------------
def sparkle(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.dot(size)


# ---------------- DRAW EVERYTHING ----------------

# Tiny stars scattered around the page
random.seed(10)

for _ in range(75):
    x = random.randint(-470, 470)
    y = random.randint(-340, 340)

    # Leave the main heart area relatively clear
    if abs(x) < 225 and abs(y) < 225:
        continue

    sparkle(
        x, y,
        random.choice([2, 3, 4]),
        random.choice(["#ffffff", "#ff8fab", "#8ecae6", "#ffd166"])
    )

# Butterflies in the four corners
draw_butterfly(-390, 280, 48, "#ff69b4")
draw_butterfly(350, 280, 42, "#b388ff")
draw_butterfly(-390, -275, 42, "#64dfdf")
draw_butterfly(350, -275, 48, "#ff9e80")

# Flowers around the borders
draw_flower(-300, 100, 15, "#ff69b4")
draw_flower(300, 90, 17, "#c77dff")
draw_flower(-300, -100, 16, "#ff85a1")
draw_flower(300, -110, 15, "#80ed99")
draw_flower(-170, 275, 13, "#ffd166")
draw_flower(180, -280, 14, "#ff69b4")
draw_flower(100, 290, 12, "#80ed99")
draw_flower(-120, -290, 13, "#c77dff")

# Main heart and message
draw_heart()
write_birthday()

# Final little accents
sparkle(-100, 175, 8, "#ffb6c1")
sparkle(105, 175, 8, "#ffb6c1")
sparkle(-125, -180, 6, "#ffd166")
sparkle(125, -180, 6, "#ffd166")

screen.update()
turtle.done()
