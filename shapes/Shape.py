from abc import ABC, abstractmethod

class Shape(ABC):

  @property
  @abstractmethod
  def color():
    pass
    
  @abstractmethod
  def getArea():
    pass
    
  def getColor(self):
    return self.color