import turtle


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

def create_flower():
  for i in range(12):
    if (i % 2) == 0:
      turtle.left(2)
      create_petal(15)
    else:
      turtle.left(34)
      create_petal(16)


def create_flower_stem(angle_st,type_,angle_th,long):
  turtle.left(angle_st)
  for i in range(12):
    if type_ == "r":
      turtle.right(angle_th)
    elif type_ == "l":
      turtle.left(angle_th)
    turtle.forward(long)

def create_flower_t1():
  for i in range(16):
    turtle.left(8)
    create_petal(15)

def create_flower_t2():
    for i in range(14):
      turtle.left(8)
      create_petal(16)

create_flower()
create_flower_stem(145,"r",2,20)
create_flower_stem(200,"l",3,30)
create_flower_t1()
turtle.penup()
turtle.left(203)
turtle.forward(355)
turtle.pendown()
create_flower_stem(110,"l",2.8,32)
create_flower_t2()
turtle.left()
turtle.mainloop()
