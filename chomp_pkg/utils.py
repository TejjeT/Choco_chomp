import os
import logging

inf = float('inf')


class ChompConstants(object):
    """
    The Class consists of all the constants to avoid typos and also it is easier to refactor something
    """
    RANDOM_PLAYER = "_random"
    MINIMAL_STEP_PLAYER = "_minimal_step"
    ACTUAL_PLAYER = '_person'
    ALPHABETA_PLAYER = '_alpha_beta'
    CHOCOLATE_ATE_VALUE = '.'
    CHOCOLATE_POISON_VALUE = 'X'
    CHOCOLATE_SWEET_VALUE = 'O'


class ChompSettings:
    """
    This class consists of all the settings for this app. We can move this to Yaml file if needed.
    We can also use @property but that also gives setters.
    """

    def __init__(self):
        pass

    BASE_ROOT = os.getcwd()  # should be under 'actual project. Need to change this if you want to run  inside package'
    APPLICATION_ROOT = os.path.join(BASE_ROOT, 'chomp_pkg')
    LOGGING_DIR = os.path.join(APPLICATION_ROOT, "configs")
    LOGGING_FILE_CONFIG = os.path.join(LOGGING_DIR, "logging.ini")
    LOG_PATH = os.path.join(BASE_ROOT, "logs")
    LOCAL_LOG_PATH = os.path.join(LOG_PATH, "choco_chomp.log")


def argmax(seq, fn):
    """Return an element with highest fn(seq[i]) score; tie goes to first one.
    >>> argmax(['one', 'to', 'three'], len)
    'three'
    """

    return argmin(seq, lambda x: -fn(x))


def argmin(seq, fn):
    """Return an element with lowest fn(seq[i]) score; tie goes to first one.
    >>> argmin(['one', 'to', 'three'], len)
    'to'
    """
    best = seq[0];
    best_score = fn(best)
    for x in seq:
        x_score = fn(x)
        logging.debug("The seq %s and value is %s", x, x_score)
        if x_score < best_score:
            best, best_score = x, x_score
    return (best, best_score)


