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
    
    # def __init__(self):
    #   def getNewRules():
    #     contents = ''
    #     alternate_score = {}

    #     with open('house_rules.txt') as file:
    #       contents = file.read()

    #     contents = contents.split("\n")

    #     for rule in contents:
    #       new_rule = rule.split(":")
    #       alternate_score[new_rule[0]] = new_rule[1]
    #       # breakpoint()
    #     return alternate_score
