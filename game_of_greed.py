from rules import Rules, Alternate
import random
keepers = []
grand_score = 0
total_points = int(0)
round = 1

def roll_the_dice():
    random_dice=[random.randint(1, 6) for _ in range(6)]
    print(random_dice)

def reroll():
    n = 6 -len(keepers)
    random_dice=[random.randint(1, 6) for _ in range(n)]
    print(random_dice)

def print_score():
  with open('score.txt', 'w') as file:
      file.write(f'Your final score was: {total_points}')
  print('You can find your score saved in score.txt')

def getNewRules():
  contents = ''
  alternate_score = {}

  with open('house_rules.txt') as file:
    contents = file.read()

  contents = contents.split("\n")

  for rule in contents:
    new_rule = rule.split(":")
    alternate_score[new_rule[0]] = new_rule[1]
  return alternate_score

def start_game():

    rule_prompt =  """
    **************************************
    **       Try your luck at foo!      **
    **    Roll the dice and track your  **
    **             points               **
    **************************************
    #####################################################

    Would you like to play with a custom rules set? Y/N
   
    #####################################################
   """
   
    rule_prompt = input(rule_prompt) 
    if rule_prompt.lower() == 'n' or rule_prompt.lower == 'no':
      roll_the_dice()
      let_em_roll()
    if rule_prompt.lower() == 'y' or rule_prompt.lower == 'yes':
      roll_the_dice()
      getNewRules()
      let_em_roll_alternate()
    else:
      print('please type Y/N')
      start_game()

default_score = Rules()
default_score = {
    'ONE_ONE_SCORE':default_score.ONE_ONE_SCORE,
    'ONE_FIVE_SCORE':default_score.ONE_FIVE_SCORE,
    'STRAIGHT_SCORE':default_score.STRAIGHT_SCORE,
    'THREE_PAIR_SCORE':default_score.THREE_PAIR_SCORE,
}

def let_em_roll():

    ROLL_OR_BANK_PROMPT = """
    ***************************************
    If you want to roll again you need to
    play at least one die. Are there any
    die here that you would like to credit
    towards your score? Type Y/N        
    ***************************************
    """
    roll_or_bank = input(ROLL_OR_BANK_PROMPT)
    if roll_or_bank.lower() == 'y' or roll_or_bank.lower() == 'yes':
      which_to_keep  = """
      *************************************
      **    Please type which numbers    **
      **  from the dice that you would   **
      **           like to keep:         **
      *************************************
      """
      keepers_response_one = input(which_to_keep)
      keepers_response = list(keepers_response_one)
      keepers.extend(keepers_response) 
      tally_score(keepers_response_one)

      if len(keepers) == 6:
          print("You get 6 dice back! Great work.")
          keepers.clear()
          roll_the_dice()
          let_em_roll()
      if len(keepers) < 6:
          reroll()
          let_em_roll()
       
    if roll_or_bank.lower() == 'n' or roll_or_bank.lower() == 'no':
        bank_it()
    else:
      print('uh oh! Are you alright? Please type y/n next time.')
      let_em_roll()

def let_em_roll_alternate():

    ROLL_OR_BANK_PROMPT = """
    ***************************************
    If you want to roll again you need to
    play at least one die. Are there any
    die here that you would like to credit
    towards your score? Type Y/N        
    ***************************************
    """
    roll_or_bank = input(ROLL_OR_BANK_PROMPT) 
    if roll_or_bank.lower() == 'y' or roll_or_bank.lower() == 'yes':
      which_to_keep  = """
      *************************************
      **    Please type which numbers    **
      **  from the dice that you would   **
      **           like to keep:         **
      *************************************
      """
      keepers_response_one = input(which_to_keep)
      keepers_response = list(keepers_response_one)
      keepers.extend(keepers_response) 
      tally_score_alternate(keepers_response_one)

      if len(keepers) == 6:
          print("You get 6 dice back! Great work.")
          keepers.clear()
          roll_the_dice()
          let_em_roll()
      if len(keepers) < 6:
          reroll()
          let_em_roll()    
    if roll_or_bank.lower() == 'n' or roll_or_bank.lower() == 'no':
        bank_it()
    else:
      print('uh oh! Are you alright? Please type y/n next time.')
      let_em_roll_alternate()

def tally_score(inpt):
    global grand_score
    counts = {}
    score = 0
    pair_counter = 0
  
    for die in inpt:
        counts[die] = counts.get(die, 0) + 1
        if counts[die] == 2: pair_counter += 1
        if pair_counter < 3 and len(counts) < 6:
            if die == '1':
                if counts[die] == 6: score += 1000
                if counts[die] == 5: score += 1000
                if counts[die] == 4: score += 1000
                if counts[die] == 3: score += 800
                if counts[die] in [1, 2]: score += default_score['ONE_ONE_SCORE']
            if die == '5':
                if counts[die] in [1, 2]: score += default_score['ONE_FIVE_SCORE']
                if counts[die] == 3: score += 400
                if counts[die] == 4: score += 500
                if counts[die] == 5: score += 500
                if counts[die] == 6: score += 500
            if die == '2':
                if counts[die] == 3: score += 200
                if counts[die] == 4: score += 200
                if counts[die] == 5: score += 200
                if counts[die] == 6: score += 200
            if die == '3':
                if counts[die] == 3: score += 300
                if counts[die] == 4: score += 300
                if counts[die] == 5: score += 300
                if counts[die] == 6: score += 300
            if die == '4':
                if counts[die] == 3: score += 400
                if counts[die] == 4: score += 400
                if counts[die] == 5: score += 400
                if counts[die] == 6: score += 400
            if die == '6':
                if counts[die] == 3: score += 600
                if counts[die] == 4: score += 600
                if counts[die] == 5: score += 600
                if counts[die] == 6: score += 600

    if pair_counter == 3:
        score = 0
        score += default_score['THREE_PAIR_SCORE']
        print(score)
    if len(counts) == 6: 
      score = 0
      score += default_score['STRAIGHT_SCORE']
    # breakpoint()
    print(f'your score for this batch is {score}')
    grand_score += score
    return score

alternate_score = Alternate()
alternate_score = {
    'STRAIGHT_SCORE':alternate_score.STRAIGHT_SCORE,
    'THREE_PAIR_SCORE':alternate_score.THREE_PAIR_SCORE,
}

def tally_score_alternate(inpt):
    global grand_score
    counts = {}
    score = 0
    pair_counter = 0
  
    for die in inpt:
        counts[die] = counts.get(die, 0) + 1
        if counts[die] == 2: pair_counter += 1
        if pair_counter < 3 and len(counts) < 6:
            if die == '1':
                if counts[die] == 6: score += 1000
                if counts[die] == 5: score += 1000
                if counts[die] == 4: score += 1000
                if counts[die] == 3: score += 800
                if counts[die] in [1, 2]: score += default_score['ONE_ONE_SCORE']
            if die == '5':
                if counts[die] in [1, 2]: score += default_score['ONE_FIVE_SCORE']
                if counts[die] == 3: score += 400
                if counts[die] == 4: score += 500
                if counts[die] == 5: score += 500
                if counts[die] == 6: score += 500
            if die == '2':
                if counts[die] == 3: score += 200
                if counts[die] == 4: score += 200
                if counts[die] == 5: score += 200
                if counts[die] == 6: score += 200
            if die == '3':
                if counts[die] == 3: score += 300
                if counts[die] == 4: score += 300
                if counts[die] == 5: score += 300
                if counts[die] == 6: score += 300
            if die == '4':
                if counts[die] == 3: score += 400
                if counts[die] == 4: score += 400
                if counts[die] == 5: score += 400
                if counts[die] == 6: score += 400
            if die == '6':
                if counts[die] == 3: score += 600
                if counts[die] == 4: score += 600
                if counts[die] == 5: score += 600
                if counts[die] == 6: score += 600

    if pair_counter == 3:
        score = 0
        score += alternate_score['THREE_PAIR_SCORE']
        print(score)
    if len(counts) == 6: 
      score = 0
      score += alternate_score['STRAIGHT_SCORE']
    # breakpoint()
    print(f'your score for this batch is {score}')
    grand_score += score
    return score

def bank_it():
  while True:
    global total_points
    global round
    global grand_score
    # score = int(input(UPDATE_SCORE_PROMPT))
    total_points += grand_score
    keepers.clear()
    # breakpoint()
    round += 1
    if round <= 3:
      print(f'You have banked your {total_points}. Round {round - 1} is now over. Time for round {round}!')  
      roll_the_dice()
      let_em_roll()
    if round > 3:
      print(f'Congrats! You ended round three with a total score of {total_points}.')
      print_score()
      again_prompt = 'Would you like to play again?'
      again = input(again_prompt)
      if again.lower() == 'y' or again.lower() == 'yes':
        grand_score = 0
        start_game()
      if again.lower() == 'n' or again.lower() == 'no':
        print('thanks for playing.')

while True:  
  start_game()
