import turtle

# create a unique petal
def create_petal(n):
  a,b,c,d =  2,3,3,3
  if n == 16:
    a,b,c,d = 3,2.2,5,4.1
  turtle.left(90+ 45)
  for i in range(33):
    if i  < 24:
      turtle.right(3)
      turtle.forward(3)
    else:
      turtle.left(2)
      turtle.forward(3)
  turtle.right(180)
  for i in range(33):
    if i < n :
      turtle.left(a)
      turtle.forward(b)
    else:
      turtle.right(c)
      turtle.forward(d)

#create a mixed flower
def create_flower():
  for i in range(12):
    if (i % 2) == 0:
      turtle.left(2)
      create_petal(15)
    else:
      turtle.left(34)
      create_petal(16)


#parameter: "angle_st" is the first move that resets the old position.
#parameter: "type_" sets the direction of the curve.
#parameter: "angle_th" is the rate at which the angle changes during forward motion.
#parameter: "long" is the distance that you want to move
def create_flower_stem(angle_st,type_,angle_th,long):
  turtle.left(angle_st)
  for i in range(12):
    if type_ == "r":
      turtle.right(angle_th)
    elif type_ == "l":
      turtle.left(angle_th)
    turtle.forward(long)

# create a flower type1
def create_flower_t1():
  for i in range(16):
    turtle.left(8)
    create_petal(15)
#create a flower type2
def create_flower_t2():
    for i in range(14):
      turtle.left(8)
      create_petal(16)

if __name__ == "__main__":
  create_flower()  #create flower mix together between t1 and t2
  create_flower_stem(145,"r",2,20) #function for create a stem 1
  create_flower_stem(200,"l",3,30) #function for create a stem 2
  create_flower_t1() #create flower t2

  turtle.penup() #reset a pen
  turtle.left(203)
  turtle.forward(355) #move the cursor to start point
  turtle.pendown() #wirte
  
  create_flower_stem(110,"l",2.8,32) #create a stem 3
  create_flower_t2() #create a flower type 3
  turtle.left()

  turtle.mainloop() #show slide
