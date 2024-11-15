import turtle
import tkinter
from tkinter import*
from PIL import Image,ImageTk
import random
import time
from turtle import*


line=turtle.Turtle()
pika=turtle.Turtle()
cactus=turtle.Turtle()
scoring=turtle.Turtle()
bestscoring=turtle.Turtle()
over=turtle.Turtle()

line.speed(0)
pika.speed(0)
cactus.speed(0)
over.speed(0)
bestscoring.speed(0)

pika.up()
cactus.up()
over.up()
bestscoring.up()
cactusy=70

line.ht()
cactus.ht()
over.ht()
bestscoring.ht()
bestscoring.goto(100,960)

wn=turtle.Screen()
wn.bgcolor("white")
wn.setup(height=2040,width=1020,startx=0,starty=0)

pikapic="/storage/emulated/0/Pythonimage/pyimg/pikachu.gif"
cactuspic="/storage/emulated/0/Pythonimage/pyimg/cactus.gif"
right=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/pyimg/Right.png")
left=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/pyimg/Left.png")
up=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/pyimg/Up.png")
restart=ImageTk.PhotoImage(file="/storage/emulated/0/Pythonimage/pyimg/restart.png")

global x1
x1=-400
global x2
x2=70
global score
score=0
global bestscore
bestscore=0

wn.register_shape(pikapic)
wn.register_shape(cactuspic)

pika.shape(pikapic)
cactus.shape(cactuspic)

def drawline():
	line.pensize(15)
	line.up()
	line.goto(-500,0)
	line.down()
	line.goto(500,0)
	line.up()
	line.goto(-500,370)
	line.down()
	line.goto(500,370)

cactus.setpos(550,cactusy)
cactusx=random.randint(510,550)

def bg():
	cactus.st()
	cactus.setpos(cactusx,cactusy)

def up1():
	global x2	
	x2+=50
def left1():
	global x1
	x1-=50	
def right1():
	global x1
	x1+=50

scoring.ht()
scoring.up()
scoring.goto(-500,960)

def write():
	global score
	scoring.write("Score :",font=("freesansbold",10,"bold"))
	if cactus.xcor()<=-470:
	    scoring.clear()
	    score+=1
	    scoring.write("Score :{}".format(score),font=("freesansbold",10,"bold"))
	    
def bestwrite():
	global bestscore
	global score
	bestscoring.write("BestScore :",font=("freesansbold",10,"bold"))
	
	

global run
run=False


def gameover():
	over.up()
	over.goto(-200,500)
	over.write("GameOver",font=("freesansbold",15,"bold"))	

def restart1():
	global score
	score=0
	scoring.clear()
	over.clear()
	global x1
	global x2
	x2=70
	pika.goto(x1,x2)
	global cactusx
	global cactusy
	cactusx=random.randint(510,570)
	cactus.setpos(cactusx,cactusy)
	global run
	run =False


drawline()

canvas=wn.getcanvas()
button=Button(canvas.master,text='',bg='aqua',bd=10,image=left,command=left1).place(x=100,y=1500,height=256,width=256)
button=Button(canvas.master,text='',bd=10,bg="aqua",image=right,command=right1).place(x=612,y=1500,height=256,width=256)
button=Button(canvas.master,text='',bg='aqua',bd=10,image=up,command=up1).place(x=356,y=1244,height=256,width=256)

button=Button(canvas.master,text='',bg='aqua',bd=10,image=restart,command=restart1).place(x=356,y=1500,height=256,width=256)

while not run:
	wn.update()
	bg()
	if pika.xcor()>cactus.xcor():
		write()
	if pika.distance(cactus)<130:
		gameover()
		if bestscore<score:
			bestscore=score
			bestscoring.clear()
			bestwrite()
			bestscoring.write("BestScore :{}".format(bestscore),font=("freesansbold",10,"bold"))
		continue
	
	pika.setpos(x1,x2)
	x2-=5
	if x2<=70:
		x2=70
	
	if pika.ycor()>300:
		gameover
		x2=100
		pika.goto(x1,x2)
		
	if pika.xcor()>400 or pika.xcor()<-400:
		gameover()
		write()
		x1=-400
		x2=70
		pika.goto(x1,x2)
	
	cactusx-=50
	if cactusx<-500:
		cactusx=random.randint(510,570)
		cactus.setpos(cactusx,cactusy)
		

	
wn.mainloop()