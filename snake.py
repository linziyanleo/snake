from tkinter import *
#import tkMessageBox,sys
import random
class Display:
    def __init__(self):
        self.root = Tk()
        self.canvas=Canvas(self.root,height=480,width=640,bg='black')
        self.canvas.pack()
        self.game = Game()
        self.root.bind('<Key>',self.keyPress)


    def Draw(self):        
        self.width = 10
        Foodpos = self.game.food.getFoodPos()
        self.canvas.create_rectangle(Foodpos[0],Foodpos[1],Foodpos[0]+self.width,Foodpos[1]+self.width,fill = 'green')
        for (x,y) in self.game.snake.body:
            self.canvas.create_rectangle(x,y,x+self.width,y+self.width,fill = 'white')
    def score(self):
        self.canvas_id = self.canvas.create_text(10,10,anchor = "nw")
        self.canvas.itemconfig(self.canvas_id, text = "score" + str(len(self.game.snake.body)-3))
    
    def Refresh(self):
        self.canvas.delete('all')
        self.Draw()
        self.score()
        if self.game.snake.life == 1:
            self.game.Update()
        else:
            self.canvas.delete('all')
            self.canvas.create_text(320,240,font = 100,anchor = "center",text = "Game over!")
        self.root.after(150,self.Refresh)

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

    def  Update(self):        
        self.snake.snakeEat(self.food)
        self.snake.snakeMove()
        self.snake.ifSnakeAlive()

class Snake:
    def __init__(self):
        self.direction = 4
        self.body = [(230,310),(240,310),(250,310)]
        self.life = 1
        self.snakewidth=10
        self.flag = 0
                
    def snakeEat(self,food):
        if self.body[-1] == food.foodPos:
            food = food.appearFood()
            self.flag = 1

    def snakeMove(self):
        # 1 up, 2 down, 3 left, 4 right
        if self.direction == 1:
            snakePos = (self.body[-1][0],self.body[-1][1]-self.snakewidth)
        elif self.direction == 2:
            snakePos = (self.body[-1][0],self.body[-1][1]+self.snakewidth)
        elif self.direction == 3:
           snakePos = (self.body[-1][0]-self.snakewidth,self.body[-1][1])
        elif self.direction == 4:
            snakePos = (self.body[-1][0]+self.snakewidth,self.body[-1][1])
        self.body.append(snakePos)

        if self.flag == 0:
            self.body = self.body[1:]                
        else:
            self.flag = 0


    def ifSnakeAlive(self):
        if self.body[-1][0]>630 or self.body[-1][0]<0 or self.body[-1][1]>470 or self.body[-1][1]<0:
            self.life = 0
        if self.body[-1] in self.body[:-1]:
            self.life = 0

class Food:
        
    def __init__(self,vecter):
        self.snakeList = vecter
        self.foodPos = self.appearFood()
    def appearFood(self):
        self.randomX = 10*random.randint(0,63)
        self.randomY = 10*random.randint(0,47)
        if (self.randomX,self.randomY) in self.snakeList:
            self.appearFood()
        else:
            self.foodPos = (self.randomX,self.randomY)
        return self.foodPos


    def getFoodPos(self):                
        return self.foodPos


        
d = Display()
d.Refresh()
d.root.mainloop()