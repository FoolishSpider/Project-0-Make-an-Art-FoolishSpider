import turtle


turtle.tracer(0,0)

print(turtle.position())

for i in range(25):
  turtle.left(10)
  turtle.forward(5)

for i in range(5):
  turtle.right(10)
  turtle.forward(5)

for i in range(9):
  turtle.left(20)
  turtle.forward(5)

turtle.right(10)
turtle.forward(50)
turtle.right(80)

for i in range(30):
  turtle.forward(5)
  turtle.left(5)
 
turtle.forward(50)

for i in range(34):
  turtle.right(6)
  turtle.forward(1)

turtle.left(25)
turtle.forward(50)

for i in range(20):
  turtle.right(5)
  turtle.forward(10)

for i in range(10):
  turtle.right(10)
  turtle.forward(5)

turtle.forward(30)
turtle.left(25)
turtle.forward(15)

turtle.up()
turtle.goto(20,0)
turtle.down()


for n in range(5):
  for iteration in range(n):
    turtle.forward(20/n)
    turtle.right(120)
  print(turtle.position())

dino_spot_size=20
dino_spike_size=20

def make_dino_spike(base, height):
  area= base * height
  return area

def make_dino_spot(radius):
  circle= π*radius**2
  return circle

for n in range(10):
  for iteration in range(n):
    turtle.circle(dino_spot_size-n)
turtle.up()
turtle.goto(0,100)
turtle.down()
for i in range(20):
  turtle.forward(2)
  turtle.right(10)
for i in range(10):
  turtle.forward(2)
  turtle.left(10)
for i in range(20):
  turtle.forward(1)
  turtle.right(10)
for i in range(20):
    turtle.forward(2)
    turtle.right(1)
turtle.goto(0,100)
    # turtle.goto(move_down_dino)
    

# def dino_spike(base, height):
#   for area = base * height
#   return area

# dino_spike(10,5)
turtle.update()
