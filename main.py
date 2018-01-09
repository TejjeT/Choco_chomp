import logging
import sys
from chomp_pkg import chomp, utils


def main():
    """
    The main class is used only fo adhoc running
    We can susbstitue this with the flask/django server etc to make it web accessible
    utils.ChompConstants has various player types that we allow.
    :return: None
    """
    rows, columns = 4, 4  # Default values , but code still raises error for invalid values
    player = utils.ChompConstants.RANDOM_PLAYER
    try:
        print "please enter number of rows and columns in the format rows,columns"

        line = sys.stdin.readline()
        rows, columns = int(line.split(',')[0]), int(line.split(',')[1])

    except ValueError:
        logging.error("Unable to read the arguments rows,columns")
        exit(0)

    print "Please enter whether you want to play or you want computer play. Press 1 if you want to play , " \
          "2 if you want to play random computer startergy," \
          "3 if you want to play minimal strategy, " \
          "4 if you want to play minimal strategy"
    line = sys.stdin.readline()

    if line and int(line) == 1:
        player = utils.ChompConstants.ACTUAL_PLAYER

    elif line and int(line) == 2:
        player = utils.ChompConstants.RANDOM_PLAYER

    elif line and int(line) == 3:
        player = utils.ChompConstants.MINIMAL_STEP_PLAYER

    elif line and int(line) == 4:
        player = utils.ChompConstants.ALPHABETA_PLAYER

    else:
        logging.error("please enter a valid value for play strategy")

    print  "The player %s has won with the moves %s " % (
    chomp.play(rows, columns, utils.ChompConstants.ALPHABETA_PLAYER, player))


if __name__ == "__main__":
    main()
