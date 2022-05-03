from Shape import Shape
class Square(Shape):
  numSides = 4
  color = ''

  def __init__(self, sideLength, color):
    self.sideLength = sideLength
    self.color = color

  # the below constructor includes default values for the init parameters
  # def __init__(self, sideLength=1, color='blue'):
  #   self.sideLength = sideLength
  #   self.color = color

# TASK 1: Write a method that returns the sideLength of the Square
# TASK 2: Write a method that sets the sideLength of the Square and returns nothing
# TASK 3: Write a method that returns an the area of the square as an integer. Call this method getArea.
