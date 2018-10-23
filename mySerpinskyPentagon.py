import turtle

#Create a Turtle and Title
puffy = turtle.Turtle()
turtle.title("Thoe's Serpenski's Pentagon")

#Speed up the turtle
puffy.speed(0)
turtle.delay(0)   #Comment out this line to see the turtle move

#Move Turtle to the top of the Screen
puffy.pu()
puffy.goto(0,300)
puffy.pd()

#Draw a equilateral pentagon
def pent(x):
      puffy.begin_fill()
      for i in range(5):
            puffy.forward(x)
            puffy.left(72)
      puffy.end_fill()

def pentPent(x):      
      for i in range(5):
            if (i == 0):
                  puffy.color("Blue")#I just did this to identify the first pentagon
            else:
                  puffy.color("Black")
            pent(x)
            puffy.forward(x)
            puffy.right(72)
            
#This is used to move the turtle to the correct starting positions      
def move(theta,x):
      puffy.pu()
      puffy.right(theta)
      puffy.forward(4*x + (2*x*.14))
      puffy.left(theta)
      puffy.pd()
      
def super(theta,x):  
      move(theta,x)
      pentPent(x)

def duper(x):
      for i in range(5):
            super(36 + i*72,x)

# Finally I realized that I could just nest this pattern into seperate loops...
def wow(x):
      for j in range(5):
            for n in range(5):  
                  for i in range(5):
                        duper(x)
                        move(36 + i*72, 2.62*x)
                  move(36 + n*72, 2.62**2*x)
            move(36 + j*72, 2.62**3*x)
wow(3)


