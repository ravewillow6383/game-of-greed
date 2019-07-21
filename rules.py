class Rules:
  def __init__(self):     
    self.ONE_ONE_SCORE = 100
    self.ONE_FIVE_SCORE = 50
    self.STRAIGHT_SCORE = 1500
    self.THREE_PAIR_SCORE = 1000

class Alternate(Rules):
    def __init__(self):
      self.STRAIGHT_SCORE = 2500
      self.THREE_PAIR_SCORE = 2000
    