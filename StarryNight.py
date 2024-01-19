
# --------------------------------------------------------
#        Name: <Allison Reel>
# Course Info: CSC111 - Fall 2021
# Description: Pumpkin Patch
#        Date: <11/5/21>
# --------------------------------------------------------
# INSTRUCTIONS do this

import graphics
import random

class Star:
  def __init__(self, x=0, y=0, r=1):
    self.x = x
    self.y = y
    self.r = r
    self.cir = graphics.Circle(graphics.Point(self.x, self.y), self.r)
    self.cir.setFill("yellow")

  def draw_star(self,window):
    self.cir.draw(window) 

class Moon:
  def __init__(self, x=0, y=0, r1=20, r2 = 18, ang = "up", c1 = "white", c2= "blue"):
    self.x = x
    self.y = y
    self.r1 = r1
    self.r2 = r2

    # makes the main moon circle (r1 and color c1 at x, y)
    self.cir1 = graphics.Circle(graphics.Point(self.x, self.y), self.r1)
    self.cir1.setFill(c1) 

    # ang lets you place the "blocker" circle to the right, left, bottom, or top

    # code for "right" 
    x2 = self.x
    y2 = self.y
    if ang == "right":
      x2 = self.x + 2*(self.r1 - self.r2)
    #TODO 1: complete for other three positions
    elif ang == "up":
      y2 = self.y + 2*(self.r1 - self.r2)
    elif ang == "left":
      x2 = self.x - 2*(self.r1 - self.r2)
    elif ang == "down":
      y2 = self.y - 2*(self.r1 - self.r2)

    # makes the blocker circle  
    self.cir2 = graphics.Circle(graphics.Point(x2, y2), self.r2)
    self.cir2.setFill(c2)
    self.cir2.setOutline(c2)

  def draw_moon(self,window):
    self.cir1.draw(window)
    self.cir2.draw(window)



class Pumpkin:
  def __init__(self, x=0, y=0, r= 30):
    self.x = x
    self.y = y
    self.r = r
    # Makes an orange circle
    self.cir = graphics.Circle(graphics.Point(self.x, self.y), self.r)
    self.cir.setFill("orange")

    # TODO 5.1: Add a "top" blocked small moon inside the pumpkin


    # TODO 5.2: Add a polygon eye to the left side of the pumpkin


    # TODO 5.3: Add a polygon eye to the right side of the pumpkin
    

    # TODO 5.4: Add a yellow stem to the top of the pumpkin
    

  # TODO 5.5: Draw all the parts of the pumpkin
  def draw_pumpkin(self,window):
    self.cir.draw(window)


def main():
  # build window
  width = 500
  height = 500
  win = graphics.GraphWin('Pumpkin', width, height)
  win.setBackground( "blue" )
  win.setCoords(-(width/2), -(height/2), (width/2), (height/2))

  # draw ground
  ground = graphics.Rectangle(graphics.Point(-(width/2), -(height/2)), graphics.Point((width/2), 0))
  ground.setFill("green")
  ground.draw(win)

  # call test function that builds starfield
  stars = draw_stars(width, height, win)
  
  # draw moon
  # TODO 2: test different placements of blocker
  moon = Moon(-(width/4), (height/4),  (width/10), (width/10)-(width/100), "up")
  moon.draw_moon(win)

  # p1 = Pumpkin(0,0,40)
  # p1.draw_pumpkin(win)
  # call test function that draws pumpkins
  pumpkins = draw_pumpkins(width, height, win)

  # Wait for a click to close the window
  p = win.getMouse()
  # Close the window
  win.close()
    

def draw_stars(width, height, w):
  n_stars = 100
  strs = list()
  for i in range(n_stars):
    x = random.randint(-(width/2), (width/2))
    y = random.randint(0, (height/2))
    r = random.randint(1, 3)
    s1 = Star(x,y,r)
    s1.draw_star(w)
    strs.append(s1)
  return strs



def draw_pumpkins(width, height, w):
  n_pums = 30
  pums = list()
  # default pumpkin  parameter initialization 
  # in the future for modifying, access an item in the list
  xs = [0] * n_pums
  ys = [0] * n_pums
  rs = [20] * n_pums
  for i in range(n_pums):
    x1 = random.randint(-(width/2), (width/2))
    xs[i] = x1
    y1 = random.randint(-(height/2), (0))
    ys[i] = y1
    r1 = random.randint(20, 30)
    rs[i] = r1
    ############################## END Version 1

  ############################## START Fix placement    
  # Draw from back to front  (top-down)
  ys.sort(reverse=True)
  rs.sort()

  ############################## END Version 2

  for i in range(n_pums):
    p1 = Pumpkin(xs[i],ys[i],rs[i])
    p1.draw_pumpkin(w)
    pums.append(p1)

  return pums  

# step 1
if __name__ == "__main__":
  main()
