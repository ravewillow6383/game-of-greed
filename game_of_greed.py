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


dice_keeper_numbers = {
    '1' : 0,
    '2' : 0,
    '3' : 0,
    '4' : 0,
    '5' : 0,
    '6' : 0,
}

print(welcome, instructions)
total_points = 0
round = 1
keepers_two = []

def tally_score(inpt):
    counts = {}
    score = 0
    # for i in range(inpt):
    for die in inpt:
        counts[die] = counts.get(die, 0) + 1
        print('!!!!!!!!!!!!!!!!', die, counts[die])
        if die == '1':
            if counts[die] == 1: score +=  100
            if counts[die] == 6: score += 2200
            if counts[die] == 5: score += 2100
            if counts[die] == 4: score += 2000
            if counts[die] == 3: score += 1000
            if counts[die] in [1, 2]: score += (1 * 100)
        if die == 5:
            if counts[die] in [1, 2]: score += (counts[die] * 50)
        else:
            print('not yet')
            # if counts >= 4: score += (die * 200)
            # if counts >= 3: score += (die * 100)
            # if (die == '5' and count != 3): score += (count * 50)
    print(f'your score is {score}')
    return score

keeper_response = input(dice_keepers_prompt)

tally_score(keeper_response)

def roll_or_bank():
    for num in keepers: 
        dice_keeper_numbers[num] += 1

    print(f'**You now have {len(keepers)} dice that you are keeping. **')

    score = int(input(UPDATE_SCORE_PROMPT))
    round_scores.append(score)

    print(f'**Your total score so far is {sum(round_scores)}')

def roll_the_dice():
    random_dice=[random.randint(1, 6) for _ in range(6)]
    print(random_dice)

def reroll():
    n = 6 -len(keepers)
    random_dice=[random.randint(1, 6) for _ in range(n)]
    print(random_dice)
    for num in keepers: 
        dice_keeper_numbers[num] += 1

def bank_it():
    global total_points
    global round
    score = int(input(UPDATE_SCORE_PROMPT))
    round_scores.append(score)
    total_points += sum(round_scores)
    keepers_two.clear()
    round += 1
    print(f'**You have banked your {total_points}. Round {round - 1} is now over. Time for round {round}!')  

while True:
    import random
    round_scores = []
    game_prompt = input(game_prompt)

    if game_prompt == 'quit':
        break

    if game_prompt == 'y':
        roll_the_dice()
        keep_or_bank = input(ROLL_OR_BANK_PROMPT)

    if keep_or_bank == 'r':
        keeper_response = input(dice_keepers_prompt)
        keepers = list(keeper_response)
        keepers_two.append(keepers)

        roll_or_bank()
        # breakpoint()
        roll_again = input(SECOND_ROLL_PROMPT)
    if keep_or_bank == 'b':
        bank_it()
    
    if roll_again == 'y':
        reroll()
        reroll_keeper_response = input(reroll_dice_keepers_prompt)
        keepers = list(keeper_response)
        keepers_two.extend(keepers)

        roll_or_bank()
        second_keep = input(ROLL_OR_BANK_PROMPT)
    if roll_again != 'y':
       bank_it()

    if reroll_keeper_response == 'b' or second_keep == 'b':
        bank_it()

    if second_keep == 'y':
        reroll()
        reroll_keeper_response = input(reroll_dice_keepers_prompt)
        keepers_reroll = list(keeper_response)
        keepers_two.extend(keepers_reroll)
        roll_or_bank()
        second_keep = input(SECOND_ROLL_PROMPT)
 
