import chomp
import utils

# Why these?  Beucase these are easier that covers most of edge cases and
# we can come with list all possible winning strategies

test_data_2_3 = [[(1, 2), (1, 0), (0, 1)], [(1, 2), (0, 1), (1, 0)], [(1, 2), (1, 1), (0, 2), (1, 0), (0, 1)],
                 [(1, 2), (0, 2), (1, 1), (1, 0), (0, 1)], [(1, 2), (1, 1), (0, 2), (0, 1), (1, 0)],
                 [(1, 2), (0, 2), (1, 1), (0, 1), (1, 0)]]

test_data_3_2 = [[(2, 1), (0, 1), (1, 0)], [(2, 1), (1, 0), (0, 1)], [(2, 1), (1, 1), (2, 0), (1, 0), (0, 1)],
                 [(2, 1), (1, 1), (2, 0), (0, 1), (1, 0)], [(2, 1), (2, 0), (1, 1), (0, 1), (1, 0)],
                 [(2, 1), (2, 0), (1, 1), (1, 0), (0, 1)]]

test_data = [((2, 3), test_data_2_3), ((3, 2), test_data_3_2)]

players = [utils.ChompConstants.RANDOM_PLAYER, utils.ChompConstants.MINIMAL_STEP_PLAYER,
           utils.ChompConstants.ALPHABETA_PLAYER]


def test_play():
    """
    This is used to do automatic testing of the package
    :param capsys: Pytest package  to read output
    :
    """

    for player in players:
        print "Performing test for players ", player
        for data in test_data:
            player, sequence = chomp.play(data[0][0], data[0][1], utils.ChompConstants.ALPHABETA_PLAYER, player)
            assert sequence in data[1]
            assert player == utils.ChompConstants.ALPHABETA_PLAYER
