from rules import Rules, Alternate
import random

welcome = """
**************************************
**       Try your luck at foo!      **
**    Roll the dice and track your  **
**             points               **
** To quit at any time, type "quit" **
**************************************
"""

game_prompt = """
***********************************
**      Ready to roll? Y/N       **
***********************************
"""
instructions = """
*******************************************************************
** Roll all six dice at the same time and remove at least one    **
** "point dice," meaning any dice that are worth points, that    **
** you want to keep. You can then either roll the remaining dice **
** or bank your points. If you get points from all 6 dice then   **
** you may roll all six again until you either lose or you bank. **
**                                                               **
**                     -POINTS-                                  **
**        A roll of a 1 is worth 100 points.                     **
**        A roll of a 5 is worth 50 points.                      **
**        Three of a kind is worth 100 times the face value.     **
*******************************************************************
"""

ROLL_OR_BANK_PROMPT = """
*************************************
**       Play at least one die     **
**  to roll again, or bank points  **
**           please type:          **
** 'b' to bank  or 'r' to choose   **
**      the dice to keep and       **
**         roll again              **
*************************************
"""

dice_keepers_prompt = """
*************************************
**    Please type which numbers    **
**  from the dice that you would   **
**           like to keep:         **
*************************************
"""

reroll_dice_keepers_prompt = """
*************************************
**    Please type which numbers    **
**  from the dice that you would   **
**    like to keep or type 'b'     **
**   to bank your points and end   **
**        your turn:               **
*************************************
"""

SECOND_ROLL_PROMPT = """
*************************************
**    Press 'y' to roll your       **
**       remaining dice.           **
*************************************
"""

UPDATE_SCORE_PROMPT = """
*************************************
**    Please tally your score      **
**      and input the total:       **
*************************************
"""


# dice_keeper_numbers = {
#     '1' : 0,
#     '2' : 0,
#     '3' : 0,
#     '4' : 0,
#     '5' : 0,
#     '6' : 0,
# }

print(welcome, instructions)
total_points = 0
grand_score = 0
round = 1
keepers_two = []

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
    print(f'your score is {score}')
    grand_score += score
    return score


# NEW RULES
def getNewRules():
  contents = ''
  alternate_score = {}

  with open('house_rules.txt') as file:
    contents = file.read()

  contents = contents.split("\n")

  for rule in contents:
    new_rule = rule.split(":")
    alternate_score[new_rule[0]] = new_rule[1]
    # breakpoint()
  return alternate_score


default_score = Rules()
new_score = Alternate()
# getNewRules()

# DEFAULT WIKI RULES

default_score = {
    'ONE_ONE_SCORE':default_score.ONE_ONE_SCORE,
    'ONE_FIVE_SCORE':default_score.ONE_FIVE_SCORE,
    'STRAIGHT_SCORE':default_score.STRAIGHT_SCORE,
    'THREE_PAIR_SCORE':default_score.THREE_PAIR_SCORE,
}
# def print_score():
        
#     with open(path) as file:
#     path = 

#     contents += ' - has been read'

#     with open('output.txt', 'w') as outputfile:
#         outputfile.write(contents)

#     print('write complete')       
def keep_or_bank():
    keep_or_bank = input(ROLL_OR_BANK_PROMPT)
    return keep_or_bank


def roll_or_bank():
    # for num in keepers: 
    #     dice_keeper_numbers[num] += 1
    if len(keepers) == 6:
        print("You get 6 dice back! Great work.")
        keepers.clear()
        roll_the_dice()
        roll_or_bank()

    print(f'**You now have {len(keepers)} dice that you are keeping. **')


    # score = int(input(UPDATE_SCORE_PROMPT))
    # round_scores.append(score)

    print(f'**Your total score so far is {grand_score}')

def roll_the_dice():
    random_dice=[random.randint(1, 6) for _ in range(6)]
    print(random_dice)

def reroll():
    n = 6 -len(keepers)
    random_dice=[random.randint(1, 6) for _ in range(n)]
    print(random_dice)

def bank_it():
    global total_points
    global round
    # score = int(input(UPDATE_SCORE_PROMPT))
    total_points += sum(round_scores)
    keepers_two.clear()
    round += 1
    print(f'**You have banked your {grand_score}. Round {round - 1} is now over. Time for round {round}!')  
    reroll()

def game_over():
    print(f'You have finished your third and final round! Your grand score was {grand_score}' )

if __name__ == "__main__":
    while True:
        round_scores = []
        game_prompt = input(game_prompt)

        if game_prompt == 'quit' or game_prompt == 'q':
            break
        if game_prompt == 'y' or game_prompt == 'Y':
            roll_the_dice()
            keep_or_bank = input(ROLL_OR_BANK_PROMPT)

        if keep_or_bank == 'r' or keep_or_bank == 'R' or keep_or_bank == 'y' or keep_or_bank == 'Y':
            keeper_response = input(dice_keepers_prompt)
            tally_score(keeper_response)
            keepers = list(keeper_response)
            keepers_two.append(keepers)

            roll_or_bank()
            roll_again = input(SECOND_ROLL_PROMPT)
        if keep_or_bank == 'b' or keep_or_bank == 'B':
            bank_it()
        
        if roll_again == 'y' or roll_again == 'Y':
            reroll()
            reroll_keeper_response = input(reroll_dice_keepers_prompt)
            tally_score(reroll_keeper_response)
            keepers = list(keeper_response)
            keepers_two.extend(keepers)

            roll_or_bank()
            second_keep = input(ROLL_OR_BANK_PROMPT)
        if roll_again != 'y' or roll_again != 'Y':
            bank_it()

        if reroll_keeper_response == 'b' or second_keep == 'b':
            bank_it()
            game_prompt = input(game_prompt)


        if second_keep == 'y' or second_keep =='Y':
            reroll()
            reroll_keeper_response = input(reroll_dice_keepers_prompt)
            tally_score(reroll_keeper_response)
            keepers_reroll = list(keeper_response)
            keepers_two.extend(keepers_reroll)
            roll_or_bank()
            second_keep = input(SECOND_ROLL_PROMPT)

        if round == 4:
            game_over()
 