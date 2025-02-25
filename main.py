import turtle
import math

# Setting up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Solar System Animation")
wn.tracer(0)  # Optimized for smoother animation

# Create the Sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3)

# Create planet properties (color, distance, size, speed, name)
planets = [
    {"color": "gray", "distance": 50, "size": 0.5, "speed": 1, "name": "Mercury"},
    {"color": "orange", "distance": 80, "size": 0.8, "speed": 0.5, "name": "Venus"},
    {"color": "red", "distance": 120, "size": 0.7, "speed": 0.3, "name": "Mars"},
    {"color": "blue", "distance": 160, "size": 0.6, "speed": 0.2, "name": "Earth"},
    {"color": "green", "distance": 200, "size": 0.9, "speed": 0.1, "name": "Jupiter"},
    {"color": "yellow", "distance": 250, "size": 0.7, "speed": 0.08, "name": "Saturn"}
]

# Create turtles for planets and labels
planet_turtles = []
label_turtles = []

for planet in planets:
    # Create planet turtle
    t = turtle.Turtle()
    t.shape("circle")
    t.color(planet["color"])
    t.shapesize(planet["size"])
    t.penup()
    t.goto(planet["distance"], 0)
    planet_turtles.append(t)

    # Create label turtle
    label = turtle.Turtle()
    label.hideturtle()
    label.color("white")
    label.penup()
    label_turtles.append(label)

# Function to animate planets and labels
angle = 0
def animate_orbits():
    global angle
    angle += 1

    for i, planet in enumerate(planets):
        # Calculate the new position of each planet
        x = planet["distance"] * math.cos(math.radians(angle * planet["speed"]))
        y = planet["distance"] * math.sin(math.radians(angle * planet["speed"]))
        planet_turtles[i].goto(x, y)

        # Update labels to follow the planets
        label_turtles[i].goto(x + 15, y + 10)
        label_turtles[i].clear()
        label_turtles[i].write(planet["name"], align="left", font=("Arial", 8, "normal"))

    # Rotate the Sun slightly
    sun.right(0.2)

    # Smooth animation loop
    wn.update()
    wn.ontimer(animate_orbits, 20)

# Start the animation
animate_orbits()

# Exit the program when clicked
wn.exitonclick()
