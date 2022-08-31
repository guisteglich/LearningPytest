from src.game import play
from src.math import *

def test_when_play_receive_1_then_return_cheese():
    # inp = 1
    # expected = 1
    # res =  play(1)
    assert  play(1) == 1

def test_when_play_receive_2_then_return_2():
    assert play(2) == 2

def test_sum():
    assert sum(1, 2) == 3

def test_sub():
    assert sub(3, 0) == 3

def test_mult():
    assert mult(5, 2) == 10

def test_div():
    assert div(10, 5) == 2


