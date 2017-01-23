from Tkinter import *
import tkMessageBox,sys
import random

class Display:
	def __init__(self):
		self.root = Tk()
		self.canvas=Canvas(self.root,height=480,width=640,bg='white')
		self.canvas.pack()
		self.game = Game()
		self.root.bind('<Key>',self.keyPress)

	def Draw(self):	
		self.width = 10
		Foodpos = self.game.food.getFoodPos()
		self.canvas.create_rectangle(Foodpos[0],Foodpos[1],Foodpos[0]+self.width,Foodpos[1]+self.width,fill = 'green')
		for (x,y) in self.game.snake.body:
			self.canvas.create_rectangle(x,y,x+self.width,y+self.width,fill = 'white')
		
		

	def Refresh(self):
		self.canvas.delete('all')
		self.Draw()
		self.root.after(150,self.Refresh)
		self.score()
		if self.game.ifSnakeAlive() == 1:
			self.game.Update()
		else:
			self.canvas.delete('all')
			self.canvas.create_text(320,240,font = 100,anchor = "center",text = "Game over!")
			

	def score(self):
		self.canvas_id = self.canvas.create_text(10,10,anchor = "nw")
		self.canvas.itemconfig(self.canvas_id, text = "score" + str(len(self.game.snake.body)-3))
		

	def keyPress(self,event):
		Snake = self.game.snake
		if event.keysym == 'Up' and Snake.direction!=2:
            		Snake.direction = 1
        	elif event.keysym == 'Down' and Snake.direction!=1:
            		Snake.direction = 2
        	elif event.keysym == 'Left' and Snake.direction!=4:
            		Snake.direction = 3
        	elif event.keysym == 'Right' and Snake.direction!=3:
           		Snake.direction = 4
		
		
class Game:
	def __init__(self):
		self.snake = Snake()
		self.food = Food(self.snake.body)
		self.flag = 0
		self.snakewidth = 10
		self.gameover = False

	
	def  Update(self):	
		self.snakeEat()
		self.snakeMove(self.flag)
		self.ifSnakeAlive()
		
	def snakeEat(self):
		if self.snake.body[-1] == self.food.foodPos:
			food = self.food.appearFood()
			self.flag = 1
	
	def snakeMove(self,flag):
                # 1 up, 2 down, 3 left, 4 right
		if self.snake.body[-1][0]>620 or self.snake.body[-1][0]<0 or self.snake.body[-1][1]>460 or self.snake.body[-1][1]<0:
			if self.snake.direction == 1:
				snakePos = (self.snake.body[-1][0],460-self.snake.body[-1][1]-self.snakewidth)
			elif self.snake.direction == 2:               	           				snakePos = (self.snake.body[-1][0],self.snake.body[-1][1]+self.snakewidth-460)
			elif self.snake.direction == 3:                       				snakePos = (620-self.snake.body[-1][0]-self.snakewidth,self.snake.body[-1][1])
			elif self.snake.direction == 4:
				snakePos = (self.snake.body[-1][0]+self.snakewidth,self.snake.body[-1][1]-620)
			self.snake.body.append(snakePos)
	
		else:
                	if self.snake.direction == 1:
				snakePos = (self.snake.body[-1][0],self.snake.body[-1][1]-self.snakewidth)
			elif self.snake.direction == 2:               	           				snakePos = (self.snake.body[-1][0],self.snake.body[-1][1]+self.snakewidth)
			elif self.snake.direction == 3:                       				snakePos = (self.snake.body[-1][0]-self.snakewidth,self.snake.body[-1][1])
			elif self.snake.direction == 4:
				snakePos = (self.snake.body[-1][0]+self.snakewidth,self.snake.body[-1][1])
			self.snake.body.append(snakePos)

		if self.flag == 0:
			self.snake.body = self.snake.body[1:]		
		else:
			self.flag = 0
	def ifSnakeAlive(self):
		if self.snake.body[-1][0]>630 or self.snake.body[-1][0]<0 or self.snake.body[-1][1]>470 or self.snake.body[-1][1]<0:
			self.snake.life = 1
		if self.snake.body[-1] in self.snake.body[:-1]:
			self.snake.life = 0
		return self.snake.life


	

class Snake:
        def __init__(self):
                self.direction = 4
		self.body = [(230,310),(240,310),(250,310)]
		self.life = 1
		
	

			
		
        	

class Food:
        
        def __init__(self,vecter):
                self.snakeList = vecter
		self.foodPos = self.appearFood()
        def appearFood(self):
                self.randomX = 10*random.randint(0,63)
                self.randomY = 10*random.randint(0,47)
                if (self.randomX,self.randomY) in self.snakeList:
                        appearFood()
                else:
                        self.foodPos = (self.randomX,self.randomY)
		return self.foodPos

	def getFoodPos(self):		
		return self.foodPos

	
d = Display()
d.Refresh()
d.root.mainloop()
	
