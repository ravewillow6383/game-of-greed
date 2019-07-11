from game_of_greed import tally_score

def test_single_one():
    assert tally_score('1' == 100)

# def test_various_twos():
#     assert tally_score('222' == 200)
#     assert tally_score('2222' == 400)
#     assert tally_score('22222' == 600)

# def test_various_threes():
#     assert tally_score('333' == 300)
#     assert tally_score('3333' == 600)
#     assert tally_score('33333' == 900)

# def test_various_fours():
#     assert tally_score('444' == 400)
#     assert tally_score('4444' == 800)
#     assert tally_score('44444' == 1200)

# def test_various_fives():
#     assert tally_score('444' == 400)
#     assert tally_score('4444' == 800)
#     assert tally_score('44444' == 1200)







# test_zilch
# non scoring roll should return 0
# test_fours
# rolls with various number of 4s should return correct score
# test_fives
# rolls with various number of 5s should return correct score
# test_sixes
# rolls with various number of 6s should return correct score
# test_straight
# 1,2,3,4,5,6 should return correct score
# test_three_pairs
# 3 pairs should return correct score
# test_leftover_ones
# 1s not used in set of 3 (or greater) should return correct score
# test_leftover_fives
# 5s not used in set of 3 (or greater) should return correct score
# test_two_trios
# 2 sets of 3 should return correct score
# test_roll
# doing a roll with x number of dice should return sequence of x length random integers between 1 and 6 inclusive