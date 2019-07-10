from game_of_greed import score

def test_score(1 1 1 5 5 5, 6):
    expected = 1500
    actual = score()
    assert actual == expected