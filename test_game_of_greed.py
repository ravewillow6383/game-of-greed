from game_of_greed import tally_score

def test_single_one():
    assert tally_score('1') == 100
    assert tally_score('11') == 200
    assert tally_score('111') == 1000
    assert tally_score('1111') == 2000
    assert tally_score('11111') == 3000
    assert tally_score('111111') == 4000

def test_various_twos():
    assert tally_score('222') == 200
    assert tally_score('2222') == 400
    assert tally_score('22222') == 600
    assert tally_score('222222') == 800

def test_various_threes():
    assert tally_score('333') == 300
    assert tally_score('3333') == 600
    assert tally_score('33333') == 900
    assert tally_score('333333') == 1200

def test_various_fours():
    assert tally_score('444') == 400
    assert tally_score('4444') == 800
    assert tally_score('44444') == 1200
    assert tally_score('444444') == 1600

def test_various_fives():
    assert tally_score('5') == 50
    assert tally_score('55') == 100
    assert tally_score('555') == 500
    assert tally_score('5555') == 1000
    assert tally_score('55555') == 1500
    assert tally_score('555555') == 2000


def test_various_sixes():
    assert tally_score('666') == 600
    assert tally_score('6666') == 1200
    assert tally_score('66666') == 1800
    assert tally_score('666666') == 2400

def test_zilch():
    assert tally_score('2') == 0
    assert tally_score('22') == 0
    assert tally_score('3') == 0
    assert tally_score('33') == 0
    assert tally_score('4') == 0
    assert tally_score('44') == 0
    assert tally_score('6') == 0
    assert tally_score('66') == 0

def test_straight():
    assert tally_score('123456') == 1500

def test_three_pairs():
    assert tally_score('112233') == 1000
    assert tally_score('334455') == 1000
    assert tally_score('662233') == 1000
