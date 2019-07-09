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

def roll_or_bank(list):
    for num in keepers: 
        dice_keeper_numbers[num] += 1

    print(f'**You now have {dice_keeper_numbers[num]} dice that you are keeping. **')

    score = int(input(UPDATE_SCORE_PROMPT))
    round_scores.append(score)

    print(f'**Your total score so far is {sum(round_scores)}')

def roll_the_dice():
    random_dice=[random.randint(1, 6) for _ in range(6)]
    print(random_dice)

def reroll(list):
    n = 6 -len(keepers_two)
    random_dice=[random.randint(1, 6) for _ in range(n)]
    print(random_dice)

def bank_it(total_points, round):
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

        roll_or_bank(keepers)
        # breakpoint()
        roll_again = input(SECOND_ROLL_PROMPT)
    if keep_or_bank == 'b':
        bank_it(total_points, round)
    
    if roll_again == 'y':
        reroll(keepers)
        second_keep = input(ROLL_OR_BANK_PROMPT)
        roll_or_bank(keepers)
    if roll_again != 'y':
        prompt = 'please enter "y" to roll or "quit" to exit the game.'

    if second_keep == 'y':
        reroll(keepers)
        second_keep = input(SECOND_ROLL_PROMPT)
        roll_or_bank(keepers)
    if second_keep == 'b':
        bank_it(total_points, round)

    