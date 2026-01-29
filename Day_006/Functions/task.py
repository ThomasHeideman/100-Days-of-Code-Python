print("Hello World")

def my_function():
  print("Hello")
  print("Bye")
my_function()


def jump():
  turn_left()
  while wall_on_right() == True:
    move()
  turn_right()
  move()
  turn_right()
  while front_is_clear():
    move()
  turn_left()