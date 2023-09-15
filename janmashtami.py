#_________ WELCOME ALL OF YOU ON COMPUTER SOFT SKILLS CHANNEL __________
#...................... KRISHNA JANMASHTAMI USING PYHON TURTLE GRAPHICS ......................


import turtle
from sketchpy import canvas
wn = turtle.Screen()
wn.setup(width=1100, height=750)
wn.title("COMPUTER SOFT SKILLS :- KRISHNA JANMASHTAMI")
turtle.Screen().bgcolor("AQUAMARINE")
t=turtle.Turtle()

# WRITE TEXT
t.penup()
t.goto(-175,-5)
t.pendown()
t.color('DARKBLUE')
style = ('ARIAL BLACK',50,'bold')
t.write('HAPPY', font=style, align='RIGHT',move=True)
t.hideturtle()

t.penup()
t.goto(-130,-70)
t.pendown()
style = ('ARIAL BLACK',50,'bold')
t.color('RED')
t.write('KRISHNA', font=style, align='right',move=True)
t.hideturtle()

t.penup()
t.goto(-90,-125)
t.pendown()
t.color('DARKGREEN')
style = ('ARIAL BLACK',40,'bold')
t.write('JANMASHTAMI', font=style, align='right', move=True)
t.hideturtle()


#Krishna Ji sketch in .svg file
ab = canvas.sketch_from_svg("D:\\python\\krishnaji.svg",scale=385)
ab.draw()

turtle.done()











