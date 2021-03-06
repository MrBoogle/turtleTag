import turtle
import random
import time
import math





#Game Functions

def pwrUpStarter():

  global takeable
  print("PowerUP!")
  pwrUp.showturtle()
  pwrUp.setpos(random.randint(-150, 150), random.randint(-150, 150))
  takeable = True
  
  screen.ontimer(pwrUpStarter, 12000)

def reset():
  p1.setpos(random.randint(-150, 150), random.randint(-150, 150))
  p2.setpos(random.randint(-150, 150), random.randint(-150, 150))

def drawborder(rounds):
  globrounds = rounds
  border.clear()
  border.speed(0)
  if rounds % 2 == 0:
   border.color('blue')
  else:
    border.color('red')
  for i in range(4):
    border.forward(360)
    border.left(90)
  
def powerUpIndicatorB():
  global tp, theLine, rounds
  
  if rounds % 2 == 0:
    pwrUpIndBlue.clear()
    
    
  else:
    pwrUpIndBlue.clear()
    pwrUpIndBlue.write(str(tp), False, 'right', font=('Candara', 15, 'bold'))
    
  for num in range(0,5):
        pwrUpIndBlue.color("white")
        pwrUpIndBlue.color('blue')

def powerUpIndicatorR():
  global tp, theLine, rounds
  
  if rounds % 2 == 0:
    pwrUpIndRed.clear()
    
  else:
    pwrUpIndBlue.clear()
    pwrUpIndRed.write(str(tp), False, 'right', font=('Candara', 15, 'bold'))
  for num in range(0,5):
        pwrUpIndRed.color("white")
        pwrUpIndRed.color('red')
  


def p1fd():
  p1.forward(avgspeed)


def p1bd():
  p1.backward(avgspeed)
  

def p1rt():
  p1.right(avgspeed)


def p1lt():
  p1.left(avgspeed)


def p2fd():
  p2.forward(avgspeed)


def p2bd():
  p2.backward(avgspeed)
  

def p2rt():
  p2.right(avgspeed)


def p2lt():
  p2.left(avgspeed)


def brdrcllsnx(player):
  x1, y1 = player.pos()
  player.up()
  if player.xcor() < -170:
    player.setpos(170, y1)
  elif player.xcor() > 170:
    player.setpos(-170, y1)
    

def brdrcllsny(player):
  player.up()
  x, y = player.pos()
  if player.ycor() < -170:
    player.setpos(x, 170)
  elif player.ycor() > 170:
    player.setpos(x, -170)
    
def checkP(player):
  global takeable, pwrUpP1, pwrUpP2, tp, length
  if abs(player.xcor() - pwrUp.xcor()) <= 15:
    if abs(player.ycor() - pwrUp.ycor()) <= 15:
      if takeable == True:
        if player == p1:
          pwrUp.ht()
          pwrUpP1 = True
          takeable = False
          if tp == 3:
            tp = 0
          if length >= 30:
            length += 15
          return takeable, pwrUpP1, tp, length
        if player == p2:
          pwrUp.ht()
          pwrUpP2 = True
          takeable = False
          if tp == 3:
            tp = 0
          if length >= 30:
            length += 15
          return takeable, pwrUpP2, tp, length
          
def p2Pwr():
    global rounds, tp, pwrUpP2
    if pwrUpP2:
      if rounds % 2 != 0:
        p2.down()
        if len(theLine) < length:
          theLine.append((p2.xcor(), p2.ycor()))
          powerUpIndicatorR()
        else:
          p2.up()
          pwrUpP2 = False
          return pwrUpP2
      else:
        if tp < 3:
          p2.setpos(random.randint(-150, 150), random.randint(-150, 150))
          tp += 1
          powerUpIndicatorR()
        else: 
          pwrUpP2 = False
          return pwrUpP2

def p1Pwr():
    global rounds, tp, pwrUpP1
    if pwrUpP1:
      if rounds % 2 == 0:
        p1.down()
        if len(theLine) < length:
          theLine.append((p1.xcor(), p1.ycor()))
          powerUpIndicatorB()
        else:
          p1.up()
          pwrUpP1 = False
          return pwrUpP1
      else:
        if tp < 3:
          p1.setpos(random.randint(-150, 150), random.randint(-150, 150))
          tp += 1
          powerUpIndicatorB()
        else: 
          pwrUpP1 = False
          return pwrUpP1

  
def subtractAndCheck(t1, t2):
  x1, y1 = t1
  x2, y2 = t2
  x3 = abs(x1-x2) 
  y3 = abs(y1-y2)
  if x3 <= 15:
    if y3 <= 15:
      return True
      
def flash(posx, posy, text, color1, color2, intrvl, times, size):
  for num in range (0,times):
        screenWriter(posx, posy, text, color1, size)
        time.sleep(intrvl)
        screenWriter(posx, posy, text, color2, size)
        bigWriter.setpos(0,0)
        bigWriter.color("white")
        
def mainmenu():
  
  screenWriter(0, 50, "Start Game", "white", 30)
  screenWriter(0, 0, "Rules", "white", 30)
  bigWriter.setpos(0,0)

      
def clicked(x,y):
  global game, menu, twoPlayer
  print((x,y))
  if abs(x) <= 100 and game == False:
    if y >= 45 and y <= 80 and menu == True:
      
      
      flash(0, 50, "Start Game", "blue", "red", 0.1, 3, 30)
      
      bigWriter.clear()
      
      bigWriter.setpos(0,75)
      bigWriter.write("1 player", False, 'center', font=('Candara', 15, 'bold'))
      
      bigWriter.setpos(0,25)
      bigWriter.write("2 player", False, 'center', font=('Candara', 15, 'bold'))
      
      menu = False
      x = None
      y = None
    
    if y <= 90 and y >= 60 and menu == False:
      flash(0,75, "1 player", "blue", "red", 0.1, 3, 15)
      twoPlayer = False
      game = True
      
    if y <= 50 and y >= 20:
      flash(0,25, "2 player", "blue", "red", 0.1, 3, 15)
      twoPlayer = True
      game = True
    
          
    
    
    elif y >= -5 and menu == True:
      menu = False
      flash(0, 0, "Rules", "blue", "red", 0.1, 3, 30)
      bigWriter.clear()
      
      
      
      bigWriter.setpos(-290, 260)
      bigWriter.write("Back", False, 'left', font=('Candara', 20, 'bold'))
      
      bigWriter.setpos(0,190)
      bigWriter.write("-Color of border indicates who is 'it'", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(0,160)
      bigWriter.write("This is a 2 player game", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(0,130)
      bigWriter.write("-The objective is to 'catch' the other turtle, or player", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(0,100)
      bigWriter.write("-There are 4 rounds, 2 rounds with the first player having", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(0,80)
      bigWriter.write("to catch the second, and vice versa", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(0,50)
      bigWriter.write("-The longer you stay uncaught,", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(0,30)
      bigWriter.write("the more points you accumulate.", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(0,0)
      bigWriter.write("-Whoever has the most points after", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(0,-20)
      bigWriter.write("4 rounds wins", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(0,-50)
      bigWriter.write("-Players can pass through walls", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(0,-80)
      bigWriter.write("-Orange circles are powerups", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(0,-110)
      bigWriter.write("-If you are 'it', the powerup", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(0,-130)
      bigWriter.write("leaves a trail behind you which will trap the player", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(0,-160)
      bigWriter.write("-Otherwise, you can teleport away from the player", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(0,-180)
      bigWriter.write("trying to catch you 3 times", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(-166, -220)
      bigWriter.write("W", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(-136, -250)
      bigWriter.write("D", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(-196, -250)
      bigWriter.write("A", False, 'center', font=('Candara', 15, 'bold'))
       
      bigWriter.setpos(0, -220)
      bigWriter.write("^", False, 'center', font=('Candara', 15, 'bold'))
      
      bigWriter.setpos(30, -250)
      bigWriter.write(">", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(-30, -250)
      bigWriter.write("<", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(166, -220)
      bigWriter.write("Power Ups:", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(166, -250)
      bigWriter.color("red")
      bigWriter.write("'Space'", False, 'center', font=('Candara', 15, 'bold'))
      bigWriter.setpos(166, -280)
      bigWriter.color("blue")
      bigWriter.write("'P'", False, 'center', font=('Candara', 15, 'bold'))
      
  if menu == False and x <= -230 and y >= 220:
      bigWriter.clear()
      menu = True
      game = False
      mainmenu()
    

  
  
def screenWriter(posx, posy, text, color, size):
    bigWriter.setpos(posx,posy)
    bigWriter.color(color)
    bigWriter.write(text, False, 'center', font=('Candara', size, 'bold'))



      




#Initialize Screen
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor((60,174,163))






#Hide unused turtle
turtle.ht()


#Init & draw border
border = turtle.Turtle()
border.speed(0)
border.up()
border.setpos((-180, -180))
border.down()

border.width(3)


redscore = 0
bluescore = 0
indicator = turtle.Turtle()
indicator.speed(0)
indicator.up()
indicator.setpos((-230, 200))
indicator.ht()


bigWriter = turtle.Turtle()
bigWriter.up()
bigWriter.ht()


# eraser = turtle.Turtle()
# eraser.ht()
# eraser.up()
# eraser.color((240, 240, 255))


drawborder(1)
border.ht()


red = turtle.Turtle()
blue = turtle.Turtle()
blue.speed(0)
red.speed(0)
blue.up()
red.up()
blue.color('blue')
red.up()
red.color('red')
red.setpos(-165, 250)
blue.setpos(0, 250)
red.shape('square')
blue.shape('square')

pwrUpIndBlue = turtle.Turtle()
pwrUpIndBlue.up()
pwrUpIndBlue.speed(0)
pwrUpIndBlue.setpos(0, -250)
pwrUpIndBlue.shape('turtle')
pwrUpIndBlue.color('blue')
pwrUpIndBlue.left(90)
pwrUpIndRed = turtle.Turtle()
pwrUpIndRed.up()
pwrUpIndRed.speed(0)
pwrUpIndRed.setpos(-165, -250)
pwrUpIndRed.shape('turtle')
pwrUpIndRed.color('red')
pwrUpIndRed.left(90)
    
#Initialize player 1
p1 = turtle.Turtle()
p1.shape("turtle")
p1.color('blue')
p1.width(3)
p1.up()
p1.speed(0)
p1.right(random.randint(0, 360))
p1.setpos(random.randint(-115, 150), random.randint(-150, 150))


#Init player 2
p2 = turtle.Turtle()
p2.shape("turtle")
p2.color('red')
p2.width(3)
p2.up()
p2.speed(0)
p2.right(random.randint(0, 360))
p2.setpos(random.randint(-150, 150), random.randint(-150, 150))


#Init PowerUp
pwrUp = turtle.Turtle()
pwrUp.ht()
pwrUp.up()
pwrUp.shape("circle")
pwrUp.color("orange")
pwrUp.speed(0)

red.write(" " * 20 + str(redscore), False, 'center', font=('Candara', 18, 'bold'))
blue.write(" " * 20 + str(bluescore), False, 'center', font=('Candara', 18, 'bold'))  


turtle.up()
p1speed = 0
p2speed = 0
avgspeed = 10


now = time.localtime()
sec = now.tm_sec
if sec > 44:
  sec = 1
print(sec)




rounds = 1
counter = rounds
countdown = 5

twoPlayer = None
menu = True
waiting = True
game = False
takeable = False
pwrUpP1 = False
pwrUpP2 = False
theLine = []
tp = 0
length = 30


mainmenu()


while waiting:
  

  
  screen.onscreenclick(clicked)
  
  if game == True:
    time.sleep(3)
    waiting = False
    menu = False
    


    pwrUpStarter()
  
while game:
  

  
  
  
  
  while countdown != 0 and countdown > 0:
    
    bigWriter.clear()
    bigWriter.write(str(countdown), False, 'center', font=('Candara', 30, 'bold'))
    countdown -= 1
    time.sleep(1)
    bigWriter.clear()
    if countdown == 0:
      # bigWriter.setpos(-290, 260)
      # bigWriter.write("Back", False, 'left', font=('Candara', 20, 'bold'))
      bigWriter.setpos(0,0)
        
  
  
  xCoor = abs(p1.xcor() - p2.xcor())
  yCoor = abs(p1.ycor() - p2.ycor())
  
  
  brdrcllsnx(p1)
  brdrcllsnx(p2)
  brdrcllsny(p1)
  brdrcllsny(p2)
  
  
  now = time.localtime()
  
  #Resets values for every round
  if rounds != counter:
    counter = rounds
    takeable = True
    theLine = []
    p1.clear()
    p2.clear()
    pwrUpP1 = False
    pwrUpP2 = False
    tp = 0
    lentgth = 30
    drawborder(rounds)
  
  # if now.tm_sec - sec == 10:
    
  #   sec = now.tm_sec
  #   print('powerUp!')
  #   if sec > 44:
  #     sec = 0
  #   pwrUp.showturtle()
  #   pwrUp.setpos(random.randint(-150, 150), random.randint(-150, 150))
  #   takeable = True
    
  checkP(p1)
  checkP(p2)
  
  
 
  if twoPlayer:
    if rounds % 2 == 0:
    
    
    #Round 1

      
      #Player 1 controls
      screen.onkey(p1fd, "Up")
      screen.onkey(p1bd, "Down")
      screen.onkey(p1lt, "Left")
      screen.onkey(p1rt, "Right")
      if pwrUpP1:
        screen.onkey(p1Pwr, "p")
        screen.listen()
      screen.listen()
      
  
      
      #Player 2 controls
      screen.onkey(p2fd, "w")
      screen.onkey(p2bd, "s")
      screen.onkey(p2lt, "a")
      screen.onkey(p2rt, "d")
      if pwrUpP2:  
        screen.onkey(p2Pwr, "Space")
        screen.listen()
      screen.listen()
      
    
      
      redscore += 1
      if xCoor <= 14:
        if yCoor <= 14:
          for i in range(0,3):
            screen.bgcolor('blue')
            p1.color("white")
            time.sleep(0.5)
            screen.bgcolor('black')
            p1.color("blue")
            time.sleep(0.5)
          rounds += 1 
          reset()
          
      for x, y in theLine:
        if subtractAndCheck(p2.position(), (x,y)):
          for i in range(0,3):
            screen.bgcolor('blue')
            p1.color("white")
            time.sleep(0.5)
            screen.bgcolor('black')
            p1.color("blue")
            time.sleep(0.5)
          rounds += 1
          reset()
          break
        
      
          
    else:
      
      
      #Player 1 controls
      screen.onkey(p1fd, "Up")
      screen.onkey(p1bd, "Down")
      screen.onkey(p1lt, "Left")
      screen.onkey(p1rt, "Right")
      if pwrUpP1:
        screen.onkey(p1Pwr, "p")
        screen.listen()
      screen.listen()
   
      
      #Player 2 controls
      screen.onkey(p2fd, "w")
      screen.onkey(p2bd, "s")
      screen.onkey(p2lt, "a")
      screen.onkey(p2rt, "d")
      if pwrUpP2:
        screen.onkey(p2Pwr, "Space")
        screen.listen()
      
      screen.listen()
      
      
      bluescore += 1
      if xCoor <= 14:
        if yCoor <= 14:
          for i in range(0,3):
            screen.bgcolor('red')
            p2.color("white")
            time.sleep(0.5)
            screen.bgcolor('black')
            p2.color("red")
            time.sleep(0.5)
          rounds += 1   
          reset()
          
      for x, y in theLine:
        if subtractAndCheck(p1.position(), (x,y)):
          for i in range(0,3):
            screen.bgcolor('red')
            p2.color("white")
            time.sleep(0.5)
            screen.bgcolor('black')
            p2.color("red")
            time.sleep(0.5)
          rounds += 1
          p2.setpos(random.randint(-150, 150), random.randint(-150, 150))
          break
      
        
      
    red.clear()
    blue.clear()
    red.write(" " * 20 + str(redscore), False, 'center', font=('Candara', 18, 'bold'))
    blue.write(" " * 20 + str(bluescore), False, 'center', font=('Candara', 18, 'bold'))
  
    
    
    
    if rounds == 5:
      if bluescore > redscore:
        bigWriter.color("blue")
        bigWriter.write("Blue Wins!", False, 'center', font=('Candara', 30, 'bold'))
        game = False
      
    
    if rounds == 5:
      if redscore > bluescore:
        bigWriter.color("red")
        bigWriter.write("Red Wins!", False, 'center', font=('Candara', 30, 'bold'))
        game = False      
  else:
    if rounds % 2 == 0:
        
        
        #Round 1
    
          
        #Player 1 controls
        screen.onkey(p1fd, "Up")
        screen.onkey(p1bd, "Down")
        screen.onkey(p1lt, "Left")
        screen.onkey(p1rt, "Right")
        if pwrUpP1:
          screen.onkey(p1Pwr, "p")
          screen.listen()
        screen.listen()
        
    
        
        #Player 2 controls
        
        p1x, p1y = p1.pos()
        p2x, p2y = p2.pos()
    
    #Player 2 controls
        if p2x - p1x >= 150 or p2y - p1y >= 150: 
          p2.seth(p2.towards(p1.pos()))
          p2.forward(avgspeed)
        else:
    
          p2.seth(p2.towards(p1.pos())+180)
          p2.forward(avgspeed)
          p1x, p1y = p1.pos()
          p2x, p2y = p2.pos()
        
        
        redscore += 1
        if xCoor <= 14:
          if yCoor <= 14:
            for i in range(0,3):
              screen.bgcolor('blue')
              p1.color("white")
              time.sleep(0.5)
              screen.bgcolor('black')
              p1.color("blue")
              time.sleep(0.5)
            rounds += 1 
            reset()
            
        for x, y in theLine:
          if subtractAndCheck(p2.position(), (x,y)):
            for i in range(0,3):
              screen.bgcolor('blue')
              p1.color("white")
              time.sleep(0.5)
              screen.bgcolor('black')
              p1.color("blue")
              time.sleep(0.5)
            rounds += 1
            reset()
            break
          
        
            
    else:
      
      
      #Player 1 controls
      screen.onkey(p1fd, "Up")
      screen.onkey(p1bd, "Down")
      screen.onkey(p1lt, "Left")
      screen.onkey(p1rt, "Right")
      if pwrUpP1:
        screen.onkey(p1Pwr, "p")
        screen.listen()
      screen.listen()
   
      
      #Player 2 controls
      
      
      p1x, p1y = p1.pos()
      p2x, p2y = p2.pos()
      
      #Player 2 controls
      if p2x - p1x >= 150 or p2y - p1y >= 150: 
        p2.seth(p2.towards(p1.pos())+180)
        p2.forward(avgspeed)
        
      else:
        p2.seth(p2.towards(p1.pos()))
        p2.forward(avgspeed)
      
    
    #Player 2 controls
      
      
      
      bluescore += 1
      if xCoor <= 14:
        if yCoor <= 14:
          for i in range(0,3):
            screen.bgcolor('red')
            p2.color("white")
            time.sleep(0.5)
            screen.bgcolor('black')
            p2.color("red")
            time.sleep(0.5)
          rounds += 1 
          reset()
          
          
      for x, y in theLine:
        if subtractAndCheck(p1.position(), (x,y)):
          for i in range(0,3):
            screen.bgcolor('red')
            p2.color("white")
            time.sleep(0.5)
            screen.bgcolor('black')
            p2.color("red")
            time.sleep(0.5)
          rounds += 1
          reset()
          break
      
        
      
    red.clear()
    blue.clear()
    red.write(" " * 20 + str(redscore), False, 'center', font=('Candara', 18, 'bold'))
    blue.write(" " * 20 + str(bluescore), False, 'center', font=('Candara', 18, 'bold'))
  
    
    
    
    if rounds == 5:
      if bluescore > redscore:
        bigWriter.color("blue")
        bigWriter.write("Blue Wins!", False, 'center', font=('Candara', 30, 'bold'))
        game = False
      
    
    if rounds == 5:
      if redscore > bluescore:
        bigWriter.color("red")
        bigWriter.write("Red Wins!", False, 'center', font=('Candara', 30, 'bold'))
        game = False          
