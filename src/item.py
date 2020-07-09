import itertools as it

class Item:
  new_id = it.count()
  def __init__(self, name, description):
    self.id = next(self.new_id)
    self.name = name
    self.description = description
    
  def __str__(self):
    return f"{self.name}: {self.description}"