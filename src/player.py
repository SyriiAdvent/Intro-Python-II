# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, loc, items=[], hasLight=False):
    self.loc = loc
    self.items = items
    self.hasLight = hasLight